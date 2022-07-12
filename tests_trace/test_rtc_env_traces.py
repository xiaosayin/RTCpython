#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from re import fullmatch
import sys
import os
import random
import numpy as np
import glob
import time
import gym
import math
from gym import spaces

import rtcGym.alphartc_gym
from CLCC.packet_info import PacketInfo
from CLCC.packet_record import PacketRecord
from tests.test_ProcessStat import ProcessStat
from printLog import printLog
import info
printSwitch = True
UNIT_M = 1000000
MAX_BANDWIDTH_MBPS = 2
MIN_BANDWIDTH_MBPS = 0.5
LOG_MAX_BANDWIDTH_MBPS = np.log(MAX_BANDWIDTH_MBPS)
LOG_MIN_BANDWIDTH_MBPS = np.log(MIN_BANDWIDTH_MBPS)

setByLastBWE = True
l_to_l = 'BiLinear'   #['Linear', 'nonLinear', 'Sigmoid', 'BiLinear', 'InfSigmoid']
MIN_FACTOR = 0.7

sigmoidK = 8
if l_to_l == 'Linear':
    MAX_FACTOR = 1 / MIN_FACTOR
    MAX_FACTOR = 1.1
else:
    MAX_FACTOR = 1 / MIN_FACTOR
    MAX_FACTOR = 1.1
a_factor = MAX_FACTOR - MIN_FACTOR
b_factor = math.log(a_factor/(1-MIN_FACTOR),2)

REWARD_RECV_PSNR = True
REWARD_RECV_PSNRVAL = False
WIDTHCNT = 2

historyLength = 1
def liner_to_log(value):
    # from 10kbps~8Mbps to 0~1
    #value = np.clip(value / UNIT_M, MIN_BANDWIDTH_MBPS, MAX_BANDWIDTH_MBPS)
    #log_value = np.log(value)
    #return (log_value - LOG_MIN_BANDWIDTH_MBPS) / (LOG_MAX_BANDWIDTH_MBPS - LOG_MIN_BANDWIDTH_MBPS)

    #print("liner_to_log: ", value, (1/3 * (2* value - 1)) ** (1 / (math.log(6,2) - 1)))    #0.5 - 2
    #return (1/3 * (2* value - 1)) ** (1 / (math.log(6,2) - 1))
    #print("liner_to_log_value: ", value)
    if l_to_l == 'Linear':
        print("liner_to_log: ")#, (value - MIN_FACTOR) / (MAX_FACTOR - MIN_FACTOR))
        return (value - MIN_FACTOR) / (MAX_FACTOR - MIN_FACTOR)
    if l_to_l == 'nonLinear':
        print("liner_to_log: ")#, ((value - MIN_FACTOR) / a_factor) ** (1/b_factor))
        return ((value - MIN_FACTOR) / a_factor) ** (1/b_factor)
    if l_to_l == 'Sigmoid':
        result = -math.log(1 / ((value - (MAX_FACTOR + MIN_FACTOR) / 2) / (MAX_FACTOR - MIN_FACTOR) + 1 / 2) - 1) / sigmoidK  + 1 / 2
        clipR = np.clip(result, 0, 1)
        print("liner_to_log: ")#, clipR)
        return clipR
    if l_to_l == 'BiLinear':
        if value >= 1:
            return (value - 1) / 2 / (MAX_FACTOR - 1) + 0.5
        else:
            return (value - MIN_FACTOR) / 2 / (1 - MIN_FACTOR)




def log_to_linear(value):
    # from 0~1 to 10kbps to 8Mbps
    value = np.clip(value.cpu(), 0, 1)
    #print("log_to_linear_value: ", value)
    #print("log_to_linear: ", value, 3 / 2 * value ** (math.log(6,2) - 1) + 1/2)    #0.5-2
    #return 3 / 2 * value ** (math.log(6,2) - 1) + 1/2

    #log_bwe = value * (LOG_MAX_BANDWIDTH_MBPS - LOG_MIN_BANDWIDTH_MBPS) + LOG_MIN_BANDWIDTH_MBPS   #R3Net
    #return np.exp(log_bwe) * UNIT_M

    print("log_to_linear: ")#, (MAX_FACTOR - MIN_FACTOR) * value + MIN_FACTOR)
    if l_to_l == 'Linear':
        return (MAX_FACTOR - MIN_FACTOR) * value + MIN_FACTOR
    if l_to_l == 'nonLinear':
        return a_factor * value ** b_factor + MIN_FACTOR
    if l_to_l == 'Sigmoid':
        print("log_to_linear: ")#, (-1/2 +  1 / (1 + math.exp(-sigmoidK * value + 1/2 * sigmoidK ))) * (MAX_FACTOR - MIN_FACTOR) + 1)
        return (-1/2 +  1 / (1 + math.exp(-sigmoidK * value + 1/2 * sigmoidK ))) * (MAX_FACTOR - MIN_FACTOR) + (MAX_FACTOR + MIN_FACTOR) / 2
    if l_to_l == 'BiLinear':
        if value >= 0.4:
            return (MAX_FACTOR - 1) / 0.6 * (value - 0.4) + 1
        else:
            return (1 - MIN_FACTOR) / 0.4 * value + MIN_FACTOR


class GymEnv:
    def __init__(self, step_time=200):
        self.gym_env = rtcGym.alphartc_gym.GymStat()
        self.step_time = step_time
        trace_dir = os.path.join(os.path.dirname(__file__), "traces")
        self.trace_set = glob.glob(f'{trace_dir}/**/*.json', recursive=True)
        self.action_space = spaces.Box(low=0.0, high=1.0, shape=(1,), dtype=np.float64)
        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0, 0.0]),
            high=np.array([1.0, 1.0, 1.0, 1.0]),
            dtype=np.float64)

        self.packet_record = PacketRecord()
        self.portNum = 8001
        self.lastRate = 0
        self.lastBWE = 300 * 1000
        self.lastEncRate = 300 * 1000
        self.started = False
        self.keyCompress = 3
        self.lastFrameDelay = 0
        self.lastRewardRecv = 0
        self.lastPSNR = 0
        self.actionCnt = 0
        self.widthCnt = 0
        halfL = 0.2
        fullL = 1
        halfR = 500000
        fullR = 1000000
        self.b = math.log(fullL/halfL, fullR/halfR)
        self.a = fullL / fullR ** self.b


    def reset(self, traceName, queLength, lossRate, video, port):
        self.processStat = ProcessStat(historyLength, REWARD_RECV_PSNRVAL)
        trace_dir = os.path.join(os.path.dirname(__file__), "traces")
        self.trace_set = glob.glob(f'{trace_dir}/**/*.json', recursive=True)
        self.action_space = spaces.Box(low=0.0, high=1.0, shape=(1,), dtype=np.float64)
        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, 0.0, 0.0]),
            high=np.array([1.0, 1.0, 1.0, 1.0]),
            dtype=np.float64)
        self.portNum = port
        #args = [f"./rtcGym/alphartc_gym/json/sender_pyinfer{self.portNum}.json", f"./rtcGym/alphartc_gym/json/receiver_pyinfer{self.portNum}.json"]
        print("trace: ", f"mm-link sampledTraces/chosenTraces/{traceName} 12mbps.trace --uplink-queue=droptail --uplink-queue-args=\"packets={queLength}\" mm-loss uplink {lossRate/100} ")
        videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
        videos = ["vidyo4"]
        args = [f"mm-link sampledTraces/chosenTraces/{traceName} 12mbps.trace --uplink-queue=droptail --uplink-queue-args=\"packets={queLength}\" mm-loss uplink {lossRate/100} " + \
            f"-- sh ./rtcGym/alphartc_gym/shs/sh_{videos[video]}/pcsend{self.portNum}.sh", \
                f"./rtcGym/alphartc_gym/jsons/json_{videos[video]}/receiver_pyinfer{self.portNum}.json"]

        self.gym_env.reset(args)
        self.packet_record.reset()
        self.portNum += 1
        if self.portNum == 8049:
            self.portNum = 8000
        self.lastBWE = 300 * 1000
        self.recv_ratef = open('log/recv_rate.txt', 'w')
        self.keyCompress = 3
        self.lastFrameDelay = 0
        self.lastRewardRecv = 0
        self.lastPSNR = 0
        self.actionCnt = 0
        self.widthCnt = 0
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    def step(self, action):
        # action: log to linear
        bweFactor = log_to_linear(action)
        printLog(f"log_to_linear action at ", info.logSwitch, None)
        if setByLastBWE:
            bandwidth_prediction = self.lastBWE * bweFactor
            #bandwidth_prediction = max(50000, bandwidth_prediction)
            #bandwidth_prediction = min(4000000, bandwidth_prediction)
            #bandwidth_prediction = 400000
        else:
            if self.keyCompress > 0:    #if I frame recved, there will be small rates shortly after
                bandwidth_prediction = self.lastBWE * bweFactor
            else:
                bandwidth_prediction = self.lastEncRate * bweFactor
        self.lastBWE = bandwidth_prediction

        # run the action
        printLog(f"step into gymStat at ", info.logSwitch, None)
        packet_list, stat, encRate, done = self.gym_env.step(bandwidth_prediction)
        self.actionCnt += 1
        if encRate > 0:
            self.lastEncRate = encRate
        else:   #if no frame was encoded in last interval
            self.lastEncRate = self.lastEncRate

        packet_list = sorted(packet_list, key = lambda x: x.receive_timestamp)
        printLog(f"sorted packlist at ", info.logSwitch, None)

        firstPkt = True     # the first pkt in this step
        for pkt in packet_list:
            packet_info = PacketInfo()
            packet_info.payload_type = pkt.payload_type
            packet_info.ssrc = pkt.ssrc
            packet_info.sequence_number = pkt.sequence_number
            packet_info.send_timestamp = pkt.send_timestamp
            packet_info.receive_timestamp = pkt.receive_timestamp
            packet_info.padding_length = pkt.padding_length
            packet_info.header_length = pkt.header_length
            packet_info.payload_size = pkt.payload_size
            packet_info.size = pkt.size
            packet_info.bandwidth_prediction = bandwidth_prediction
            self.packet_record.on_receive(packet_info, firstPkt)
            firstPkt = False

        printLog(f"processed packlist at ", info.logSwitch, None)
        bweRequestTime = round(time.time() * 1000)
        # calculate state
        states = []     #[receiving_rate, delay, delay_gradient, loss_ratio, psnr, frameDelay, frameSkip, lasetBWE]

        receiving_rate = self.packet_record.calculate_receiving_rate(interval=self.step_time)
        print("receiving_rate: ", receiving_rate)       #bps
        self.recv_ratef.write(f"{receiving_rate} ; {round(time.time()* 1000000)}\n")
        states.append(receiving_rate / 4000000)
        printLog(f"processed receiving_rate at ", info.logSwitch, None)

        delay = self.packet_record.calculate_average_delay(interval=self.step_time)
        print("delay: ", delay)
        states.append(min(delay / 500, 1))
        printLog(f"processed delay at ", info.logSwitch, None)

        delay_gradient = self.packet_record.calculate_delay_gradient(interval=self.step_time)
        print("delay_gradient: ", delay_gradient)
        if delay_gradient / 400 + 1/2 < 0:
            states.append(0)
        else:
            states.append(min(delay_gradient / 400 + 1/2, 1))
        printLog(f"processed delay_gradient at ", info.logSwitch, None)


        loss_ratio, burstLoss_ratio = self.packet_record.calculate_loss_ratio(interval=self.step_time)
        print("loss_ratio: ", loss_ratio)
        print("burstLoss_ratio: ", burstLoss_ratio)
        states.append(loss_ratio)
        states.append(min(4 * burstLoss_ratio, 1))
        printLog(f"processed loss_ratio at ", info.logSwitch, None)

        printLog(f"processed state0-2 at ", info.logSwitch, None)

        flag, psnrStat, delayStat, skipStat, isKey, width = self.processStat.processStat(stat, info.PSNRI, info.widthI, info.DroppedI, info.sendI, info.beforeDecI, info.isKeyI)
        statePSNR = 0
        stateFrameDelay = 0
        stateFrameDelayGradient = 1 / 2
        stateFrameSkip = 0
        stateWidth = width / 1280
        stateLastAction = 0
        stateEncLoss = 0
        rewardPSNR = 0
        rewardFrameDelay = 0
        rewardFrameSkip = 0
        rewardLastAction = 0
        rewardEncLoss = 0
        if flag:
            statePsnr, stateDelay, stateSkip = self.processStat.gotState(psnrStat[-1], delayStat[-1], skipStat[-1])
            if len(statePsnr) == historyLength:
                statePSNR = min(float(statePsnr[-1]) / 450000, 1)
                stateFrameDelay = (min(float(stateDelay[-1]/1000), 1))
                stateFrameSkip = (min(float(stateSkip[-1]/32), 1))
                #states.append(liner_to_log(bweFactor))
                stateLastAction = (np.clip(action.cpu(), 0, 1))
                stateEncLoss = (min(abs(encRate - self.lastBWE) / 1000000, 1))
                rewardPSNR = (float(statePsnr[-1]/600000)) * 16
                rewardFrameDelay = - 10 * stateDelay[-1] / 1000
                rewardFrameSkip = 0
                rewardLastAction = 0
                rewardEncLoss = -(1.5 / 1000000 ** 2) * (encRate - self.lastBWE) ** 2 * 10 ** (min(- self.keyCompress, 0))
                if (self.lastFrameDelay != 0):
                    
                    if (stateDelay[-1] - self.lastFrameDelay) / 400 + 1/2 < 0:
                        stateFrameDelayGradient = 0
                    else:
                        stateFrameDelayGradient = min((stateDelay[-1] - self.lastFrameDelay) / 400 + 1/2, 1)
                self.lastFrameDelay = stateDelay[-1]
        else:
            print("reward dont have psnr, skip, frame delay, cuz it havent started")
            

        states.append(statePSNR)
        states.append(stateFrameDelay)
        states.append(stateFrameDelayGradient)
        states.append(stateFrameSkip)
        states.append(stateWidth)
        states.append(stateLastAction)
        states.append(stateEncLoss)
        print("rtc_env_isKey: ", isKey)
        if isKey:
            self.keyCompress = 7
        else:
            self.keyCompress = max(self.keyCompress - 1, 0)


        print("receiving_rate in reward: ", receiving_rate / 1000000.0)
        print("encLoss in reward: ")
        trueRewardPSNR = receiving_rate / 1000000.0
        reward = trueRewardPSNR - delay * 16 / 1000.0 - 6 * burstLoss_ratio + rewardFrameDelay #+ encLoss
        
        if REWARD_RECV_PSNR:
            if stateWidth < 1:
                trueRewardPSNR = receiving_rate / 1000000.0
                self.lastRewardRecv = receiving_rate / 1000000.0
                self.lastPSNR = rewardPSNR
            else:
                if self.widthCnt < WIDTHCNT and REWARD_RECV_PSNRVAL:
                    trueRewardPSNR = receiving_rate / 1000000.0
                    self.lastRewardRecv = receiving_rate / 1000000.0
                    self.lastPSNR = rewardPSNR
                    self.widthCnt += 1
                else:
                    trueRewardPSNR = self.lastRewardRecv +  rewardPSNR - self.lastPSNR
        else:
            trueRewardPSNR = rewardPSNR
         
        reward = trueRewardPSNR - delay * 16 / 1000.0 - 6 * burstLoss_ratio + rewardFrameDelay #+ encLoss
        

        latest_prediction = self.packet_record.calculate_latest_prediction()
        printLog(f"processed state3-5 at ", info.logSwitch, None)

        printLog(f"linear_to_log at ", info.logSwitch, None)
        self.lastRate = receiving_rate
        return states, reward, trueRewardPSNR, - delay * 16 / 1000.0  , - 6 * burstLoss_ratio, rewardFrameDelay, done, \
                [receiving_rate, delay, loss_ratio, statePsnr[-1], stateDelay[-1], stateSkip[-1], bweRequestTime] if flag else [receiving_rate, delay, loss_ratio, 0, 0, 0, bweRequestTime], {}

        #return states, reward, receiving_rate, receiving_rate , receiving_rate, done, {}

    def getThisRTCTotalStat(self):
        return self.packet_record.calculate_total_receiving_rate(), self.packet_record.calculate_total_delay(), \
            self.packet_record.calculate_total_loss_ratio()

            