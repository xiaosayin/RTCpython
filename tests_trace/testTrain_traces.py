#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import sizeof
import sys
import os
import subprocess
import traceback
import json
import time
import multiprocessing as mp
from multiprocessing import Array
import importlib
import pickle

from numpy import true_divide
from tests_trace.test_rtc_env_traces import GymEnv
from CLCC.RL.storage import Storage
from CLCC.RL.ppo_agent import PPO
import torch
import matplotlib.pyplot as plt
from printLog import printLog
import info
import random
sys.path.append(os.getcwd())
os.system("rm result/*")
os.system("rm result/tmp/*")
os.system("rm result/delay/*")
def drawPlt(xlabel, ylabel, pltName, x, y):
    plt.cla()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(pltName)

def testTrain(cc, testName, testQue, testLoss, testVideo, port):
    ############## Hyperparameters for the experiments ##############
    env_name = "AlphaRTC"
    sample_Maxnum = 1
    range1 = 50
    range2 = 60
    range3 = 70
    max_num_episodes = range1 + range2 + range3
    exploration_param = 0.7    # the std var of action distribution
    K_epochs = 15              # update policy for K_epochs
    ppo_clip = 0.1             # clip parameter of PPO
    gamma = 0.8                # discount factor

    lrMax = 3e-3               # Adam parameters
    lrMin = 3e-5
    betas = (0.9, 0.999)
    state_dim = 8
    state_length = 10
    action_dim = 1
    data_path = f'./data/' # Save model and reward curve here
    remotePath = os.getcwd() + '/remoteFiles/'

    recvRateTrack = []
    delayTrack = []
    lossTrack = []
    
    PSNRTrack = []
    FrameDelayTrack = []
    FrameSkipTrack = []
    timeTrack = []
    #############################################
    printSwitch = True

    if not os.path.exists(data_path):
        os.makedirs(data_path)
    env = GymEnv(200)
    storage = Storage() # used for storing data
    ppo = PPO(state_dim, state_length, action_dim, exploration_param, lrMax, lrMax, lrMin, max_num_episodes, betas, gamma, K_epochs, ppo_clip)
    checkpoint = torch.load(f'tests_trace/{cc}/{cc}.pth')
    ppo.policy.load_state_dict(checkpoint['model'])
    ppo.policy_old.load_state_dict(checkpoint['model'])

    this_exploration_param = 0.01
    ppo.policy_old.updateExploreVal(action_dim, this_exploration_param)
    ppo.policy.updateExploreVal(action_dim, this_exploration_param)

    time_step = 0
    sample_cnt = 0
    while True :
        done = False
        state = [0] * state_dim    #R3NET
        state = torch.Tensor(state).cuda()
        env.reset(testName, testQue, testLoss, testVideo, port)
        ppo.policy_old.reset()
        ppo.policy.reset()

        firstAction = True  #to record whether RNN needs a h0
        time_step = 0
        while not done:# and time_step < update_interval:
            action = ppo.select_action(state, storage, firstAction)
            firstAction = False
            print(f"give action {sample_cnt}============================")
            listState, reward, reward_recv, reward_delay, reward_loss, reward_frameDelay, done, \
                [recv_rate, delay, loss_ratio, framepsnr, frameDelay, frameSkip, bweRequestTime], _ = env.step(action)
            recvRateTrack.append(recv_rate)
            delayTrack.append(delay)
            lossTrack.append(loss_ratio)
            
            PSNRTrack.append(framepsnr)
            FrameDelayTrack.append(frameDelay)
            FrameSkipTrack.append(frameSkip)
            timeTrack.append(bweRequestTime)
            time_step += 1
            sample_cnt += 1
            state = state.clone().detach()
            
            ## with PSNR
            state[0] = listState[1]     #delay
            state[1] = listState[2]     #delayGradient
            state[2] = listState[4]     #burstLoss
            state[3] = listState[5]     #PSNR
            state[4] = listState[6]     #frameDelay
            state[5] = listState[7]     #frameDelayGradient
            state[6] = listState[9]     #width
            state[7] = listState[10]     #lastAction
            
            '''
            ## withOUT PSNR
            state[0] = listState[1]     #delay
            state[1] = listState[2]     #delayGradient
            state[2] = listState[4]     #burstLoss
            state[3] = listState[6]     #frameDelay
            state[4] = listState[7]     #frameDelayGradient
            state[5] = listState[10]     #lastAction
            '''
            
            '''
            ## only pkt recv, delay, loss
            state[0] = listState[1]     #delay
            state[1] = listState[2]     #delayGradient
            state[2] = listState[4]     #burstLoss
            state[3] = listState[10]     #lastAction
            '''

            # Collect data for update
            if not done:
                storage.rewards.append(reward)
                storage.rewardRecv.append(reward_recv)
                storage.rewardDelay.append(reward_delay)
                storage.rewardLoss.append(reward_loss)
                storage.rewardFrameDelay.append(reward_frameDelay)
                storage.is_terminals.append(done)
            else:
                sample_cnt -= 1
                if time_step != 1:
                    storage.actions.pop()
                    storage.values.pop()
                    storage.states.pop()
                    storage.logprobs.pop()
                    storage.firstAction.pop()
                    storage.is_terminals[-1] = True
                else:
                    storage.logprobs.pop()
                    storage.values.pop()
                    storage.states.pop()
                    storage.actions.pop()
                    storage.firstAction.pop()
                time_step = 0
            print("one action ended============================\n")
        print("one rtc ended============================\n")
        RTCrate, RTCdelay, RTCloss = env.getThisRTCTotalStat()
        print(f"In this RTC, recv_rate = {RTCrate}, delay = {RTCdelay}, loss = {RTCloss}")
        if done and sample_cnt > sample_Maxnum:
            break

    drawPlt('time', 'recvRate', f'tests_trace/{cc}/track/recvRateTrack.jpg', timeTrack, recvRateTrack)
    drawPlt('time', 'delay', f'tests_trace/{cc}/track/delayTrack.jpg', timeTrack, delayTrack)
    drawPlt('time', 'loss', f'tests_trace/{cc}/track/lossTrack.jpg', timeTrack, lossTrack)
    drawPlt('frame', 'PSNRTrack', f'tests_trace/{cc}/track/PSNRTrack.jpg', range(len(PSNRTrack)), PSNRTrack)
    drawPlt('frame', 'FrameDelayTrack', f'tests_trace/{cc}/track/FrameDelayTrack.jpg', range(len(FrameDelayTrack)), FrameDelayTrack)
    drawPlt('frame', 'FrameSkipTrack', f'tests_trace/{cc}/track/FrameSkipTrack.jpg', range(len(FrameSkipTrack)), FrameSkipTrack)
    print("len of all tracks: ", len(recvRateTrack), len(delayTrack), len(lossTrack),\
                     len(PSNRTrack), len(FrameDelayTrack), len(FrameSkipTrack))
    f=open(f'tests_trace/{cc}/track/trackPickle','wb')
    pickle.dump([[recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack], \
        env.packet_record], f, 0)
    f.close()
        
        
            
def main():
    1

if __name__ == "__main__":
    main()
