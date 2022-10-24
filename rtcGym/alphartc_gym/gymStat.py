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
from multiprocessing import Array, Pipe
import importlib

RequestBandwidthCommand = "RequestBandwidth"
timeLog = " atTime: "
encLog = "KOYONYONG: encoded_image.size(): "
decLog = "KOYONYONG: decoded size: "

FIFO_PATH = "/home/yinwenpei/rtc_signal/v_fifo"
ID_FIFO_PATH = "/home/yinwenpei/rtc_signal/id_fifo"

Defalut_overuse_flag = "ABNORMAL"

import info
from printLog import printLog
import os
from rtcGym.alphartc_gym.peerconnection import appRecvProxy, appSendProxy, processR, processS,processEncLine, processDecLine, \
                                        fetch_stats, request_estimated_bandwidth, find_estimator_class, addT, getTime

class GymStat(object):
    def __init__(self):
        self.recvProxy = None
        self.sendProxy = None
        self.gymPipe = None
        self.rtcPipe = None
        self.estimator = None
        self.startFlag = False
        # self.action_proxy_process = None
        self.lastSeq = 0
        print("init")


    def reset(self, argv):
        self.recvProxy = None
        self.sendProxy = None
        self.gymPipe = None
        self.rtcPipe = None
        self.estimator = None
        self.startFlag = False
        # self.action_proxy_process = None
        self.lastSeq = 0
        estimator_class = find_estimator_class()
        self.estimator = estimator_class('gcc')

        #two pipes
        # (RL_Pipe, Action_Proxy_Pipe) = Pipe()
        # (RL_Pipe, Action_Proxy_Pipe) = Pipe()
        (self.gymPipe, self.rtcPipe) = Pipe()       #for sending bitrate and receiving frame stat
        (recv_send_pipe, send_recv_pipe) = Pipe()   #for ensuring appRecvProxy runs later than appSendProxy 
        # initiate allFrame with -777
        allFrame = Array('i', range(info.frameL * 30 * 60 * 2))
        for i in range(len(allFrame)):
            allFrame[i] = -777

        # 运行消息中转进程
        # self.action_proxy_process = mp.Process(target=Action_Proxy, args=(SENDER_PIPE_PATH, Action_Proxy_Pipe))

        #运行RTC收发进程
        self.recvProxy = mp.Process(target=appRecvProxy, args=(argv[1], allFrame, self.rtcPipe, recv_send_pipe,))
        self.sendProxy = mp.Process(target=appSendProxy, args=(argv[0], allFrame, send_recv_pipe))


        recvf = open(f"log/recv.txt", 'w')
        recvf.close()
        recvf = open(f"log/recv.txt", 'r')
        self.recvProxy.start()
        '''
        while True:
            count=len(recvf.readlines())
            print("recvf lines: ", count)
            if count == 0:
                print("recv not opened, waiting...")
                time.sleep(1)
            else:
                print("recv opened!")
                recvf.close()
                break

        '''
        if send_recv_pipe.recv() == 1:
            print("appRecv started")
            time.sleep(3)
        self.sendProxy.start()
        self.startFlag = False



    # def step(self, bandwidth_bps: int):
    def step(self, bandwidth_bps: float):
        # printLog(f"send bwe to appRecv at ", info.logSwitch, None)
        # self.gymPipe.send(int(bandwidth_bps))
        # printLog(f"sent bwe to appRecv at ", info.logSwitch, None)
        if not self.startFlag:
            printLog(f"wait for recv string at ", info.logSwitch, None)
            while not self.gymPipe.poll():
                if not self.recvProxy.is_alive():
                    self.recvProxy.join()
                    self.sendProxy.join()
                    printLog(f"recv proxy is dead! stop waiting! ", info.logSwitch, None)
                    # return [], [], 0, True, Defalut_overuse_flag
                    return [], [], 0, True
            msg = self.gymPipe.recv()
            printLog(f"recved string at ", info.logSwitch, None)

            print(msg)
            if msg == 1:    #"asking for bwe"
                printLog(f"wait for recv [self.estimator, stat] at ", info.logSwitch, None)
                # [self.estimator, stat, rate] = self.gymPipe.recv()
                [self.estimator, stat, active_loss] = self.gymPipe.recv()
                printLog(f"recved [self.estimator, stat] at ", info.logSwitch, None)
            self.startFlag = True
        printLog(f"send bwe to appRecv at ", info.logSwitch, None)
        # self.gymPipe.send(int(bandwidth_bps))
        self.gymPipe.send(float(bandwidth_bps))
        printLog(f"sent bwe to appRecv at ", info.logSwitch, None)

        if not self.recvProxy.is_alive():
            self.recvProxy.join()
            self.sendProxy.join()
            # return [], [], 0, True, Defalut_overuse_flag
            return [], [], 0, True

        #if not self.recvProxy.is_alive():
        #    self.sendProxy.join()
        #    self.trace.join()
        #    return [], [], True
        printLog(f"wait for recv string at ", info.logSwitch, None)
        while not self.gymPipe.poll():
            if not self.recvProxy.is_alive():
                self.recvProxy.join()
                self.sendProxy.join()
                # return [], [], 0, True, Defalut_overuse_flag
                return [], [], 0, True
        msg = self.gymPipe.recv()
        printLog(f"recved string at ", info.logSwitch, None)
        print(msg)
        if msg == 0: #"Recv finished"
            self.recvProxy.join()
            self.sendProxy.join()
            # return [], [], 0, True, Defalut_overuse_flag
            return [], [], 0, True
        if msg == 1: #"asking for bwe"
            printLog(f"wait for recv [self.estimator, stat] at ", info.logSwitch, None)
            # [self.estimator, stat, rate] = self.gymPipe.recv()
            [self.estimator, stat, active_loss] = self.gymPipe.recv()
            printLog(f"recved [self.estimator, stat] at ", info.logSwitch, None)
            # self.estimator.get_estimated_bandwidth_by_delay()

            return self.estimator.intervalPackets_list, stat, active_loss, False
            # return self.estimator.intervalPackets_list, stat, bwe, False, self.estimator.overuse_flag



def main():
    mp.set_start_method('fork')
    portNum = 8000
    gym = GymStat()
    traceNum = 0
    while traceNum < 10:
        args = [f"./json/sender_pyinfer{portNum}.json", f"./json/receiver_pyinfer{portNum}.json"]
        gym.reset(args, traceNum)
        while True:
            if (gym.step()):
                break
            else:
                continue
        traceNum += 1
        portNum += 1

if __name__ == "__main__":
    main()

