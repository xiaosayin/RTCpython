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

import info
from printLog import printLog
import os
from rtcGym.alphartc_gym.peerconnection3RTC import appRecvProxy, appSendProxy, processR, processS,processEncLine, processDecLine, \
                                        fetch_stats, request_estimated_bandwidth, find_estimator_class, addT, getTime

class GymStat3RTC(object):
    def __init__(self, jsonRange = 0):
        self.jsonRange = jsonRange
        self.recvProxy = None
        self.sendProxy = None
        self.trace = None
        self.gymPipe = None
        self.rtcPipe = None
        self.estimator = None
        self.startFlag = False
        self.lastSeq = 0
        print("init")


    def reset(self, argv, traceNum):
        self.recvProxy = None
        self.sendProxy = None
        self.trace = None
        self.gymPipe = None
        self.rtcPipe = None
        self.estimator = None
        self.startFlag = False
        self.lastSeq = 0
        estimator_class = find_estimator_class()
        self.estimator = estimator_class()

        (self.gymPipe, self.rtcPipe) = Pipe()
        # initiate allFrame with -777
        allFrame = Array('i', range(info.frameL * 30 * 60 * 2))
        for i in range(len(allFrame)):
            allFrame[i] = -777

        self.recvProxy = mp.Process(target=appRecvProxy, args=(argv[1], allFrame, self.rtcPipe, self.jsonRange))
        self.sendProxy = mp.Process(target=appSendProxy, args=(argv[0], allFrame, self.jsonRange))
        model_filename = "rtcGym.alphartc_gym.square." + f"trace{traceNum}"
        model_filename = "rtcGym.alphartc_gym.square." + f"trace{1}"
        modellib = importlib.import_module(model_filename)
        self.trace = mp.Process(target = modellib.link)

        self.recvProxy.start()
        time.sleep(5)
        self.trace.start()
        self.sendProxy.start()
        self.startFlag = False



    def step(self, bandwidth_bps: int):
        if not self.startFlag:
            msg = self.gymPipe.recv()

            print(msg)
            if msg == 1:    #"asking for bwe"
                [self.estimator, stat] = self.gymPipe.recv()
            self.startFlag = True
        printLog(f"send bwe to appRecv at ", info.logSwitch, None)
        self.gymPipe.send(int(bandwidth_bps))
        printLog(f"sent bwe to appRecv at ", info.logSwitch, None)

        if not self.recvProxy.is_alive():
            self.sendProxy.join()
            self.trace.join()
            return [], [], True

        #if not self.recvProxy.is_alive():
        #    self.sendProxy.join()
        #    self.trace.join()
        #    return [], [], True
        printLog(f"wait for recv string at ", info.logSwitch, None)
        msg = self.gymPipe.recv()
        printLog(f"recved string at ", info.logSwitch, None)
        print(msg)
        if msg == 0: #"Recv finished"
            self.sendProxy.join()
            self.trace.join()
            return [], [], True
        if msg == 1: #"asking for bwe"
            printLog(f"wait for recv [self.estimator, stat] at ", info.logSwitch, None)
            [self.estimator, stat] = self.gymPipe.recv()
            printLog(f"recved [self.estimator, stat] at ", info.logSwitch, None)

            #estimatorI = 0
            #if self.lastSeq != 0:
            #    while estimatorI < len(self.estimator.packets_list):
            #        if self.lastSeq < self.estimator.packets_list[estimatorI].sequence_number:
            #            break
            #        estimatorI += 1
            #estiPackList = self.estimator.packets_list[estimatorI:]


            #self.lastSeq = self.estimator.packets_list[-1].sequence_number
            return self.estimator.intervalPackets_list, stat, False



def main():
    mp.set_start_method('fork')
    portNum = 8000
    gym = GymStat3RTC()
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

