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
from CLCC.packet_info import PacketInfo
from CLCC.packet_record import PacketRecord
from CLCC.ProcessStat import ProcessStat
import matplotlib.pyplot as plt

import numpy as np
import importlib
import pickle
import psutil
from threading import Timer
import allDelay
import random
import bitRateAnalysis2
import plotResult
mp.set_start_method('fork')
sys.path.append(os.getcwd())
os.system("rm result/*")
os.system("rm result/tmp/*")
os.system("rm result/delay/*")
RequestBandwidthCommand = "RequestBandwidth"
timeLog = " atTime: "
encLog = "KOYONYONG: encoded_image.size(): "
decLog = "KOYONYONG: decoded size: "
import info

def fetch_stats(line: str, recvf)->dict:
    tmpLine = line[:]
    if "KOYONYONG" in line: #somtimes KOYONYONG log may add to cmdinfer log, cause bad loss cnt
        line = line[:line.index("KOYONYONG")]

    line = line.strip()
    try:
        stats = json.loads(line)
        if ( "KOYONYONG" in tmpLine):
            recvf.write(tmpLine[tmpLine.index("KOYONYONG"):])
            recvf.flush()
        return stats
    except json.decoder.JSONDecodeError:
        return None

def request_estimated_bandwidth(line: str)->bool:
    line = line.strip()
    if RequestBandwidthCommand in line:
        return True
    return False

def find_estimator_class(cc):
    if cc == 'gcc':
        import rtcGym.alphartc_gym.HRCC.BandwidthEstimator_gcc
        return rtcGym.alphartc_gym.HRCC.BandwidthEstimator_gcc.GCCEstimator
    if cc == 'hrcc':
        import rtcGym.alphartc_gym.HRCC.BandwidthEstimator_HRCC
        return rtcGym.alphartc_gym.HRCC.BandwidthEstimator_HRCC.Estimator

def addT(T, type, time):
    if type != "is_KeyFrame":
        time = int(time/1000)
        time = int(time % 1000000)
    if T == []:
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if type == "gotT":
        T[0] = time
    elif type == "beforeEncT":
        T[1] = time
    elif type == "is_KeyFrame":
        T[2] = time
    elif type == "afterEncT":
        T[3] = time
    elif type == "sendT":
        T[4] = time
    elif type == "recvT1":
        T[5] = time
    elif type == "recvT2":
        T[6] = time
    elif type == "beforeDecT":
        T[7] = time
    elif type == "afterDecT":
        T[8] = time
    elif type == "beforeRenderT":
        T[9] = time
    elif type == "RenQueueRecved":
        T[10] = time
    elif type == "afterRenderT":
        T[11] = time
    return T

def getTime(line, log):
    return int(line[line.index(log) + len(log): ])

def processEncLine(sendLine, tmpAll, encI, frameCnt, final):
    if "KOYONYONG: got frame" in sendLine:
        tmpAll.append([frameCnt, 1, 1, 1, 1, addT([], "gotT", getTime(sendLine, timeLog)), 2])
        final[frameCnt * info.frameL + info.NumI] = frameCnt
        final[frameCnt * info.frameL + info.SizeI] = 1
        final[frameCnt * info.frameL + info.PSNRI] = 1
        final[frameCnt * info.frameL + info.widthI] = 1
        final[frameCnt * info.frameL + info.RtpI] = 1
        final[frameCnt * info.frameL + info.gotI : frameCnt * info.frameL + info.afterRenderI + 1] = addT([], "gotT", getTime(sendLine, timeLog))
        final[frameCnt * info.frameL + info.DroppedI] = 2
        frameCnt += 1
    if "Drop frame in order to respect" in sendLine:
        tmpAll[frameCnt - 1][info.tmpDroppedI] = 0
        final[frameCnt * info.frameL + info.DroppedI] = 0


    #drop before enc
    if "KOYONYONGDROP" in sendLine or "Same/old NTP timestamp" in sendLine:
        while tmpAll[encI][info.tmpDroppedI] == 0:
            encI += 1
        for i in range(info.SizeI, info.RtpI + 1):
            tmpAll[encI][i] = 0
        tmpAll[encI][info.tmpDroppedI] = 0
        for i in range(info.SizeI, info.RtpI + 1):
            final[encI * info.frameL + i] = 0
        final[encI * info.frameL + info.DroppedI] = 0
        encI += 1

    if "KOYONYONG: Before enc" in sendLine:
        while tmpAll[encI][info.tmpDroppedI] == 0:
            encI += 1
        tmpAll[encI][info.RtpI + 1] = addT(tmpAll[encI][info.RtpI + 1], "beforeEncT", getTime(sendLine, timeLog))
        tmpAll[encI][info.widthI] = int(sendLine[sendLine.index("KOYONYONG: Before enc: ") + len("KOYONYONG: Before enc: ") : sendLine.index(timeLog)])
        final[encI * info.frameL + info.gotI: encI * info.frameL + info.afterRenderI + 1] = tmpAll[encI][info.RtpI + 1]
        final[encI * info.frameL + info.widthI] = tmpAll[encI][info.widthI]

    if "KOYONYONG: this frame is KEYFRAME" in sendLine:
        tmpAll[encI][info.RtpI + 1] = addT(tmpAll[encI][info.RtpI + 1], "is_KeyFrame", True)
        final[encI * info.frameL + info.gotI: encI * info.frameL + info.afterRenderI + 1] = tmpAll[encI][info.RtpI + 1]
    elif "KOYONYONG: this frame is not KEYFRAME" in sendLine:
        tmpAll[encI][info.RtpI + 1] = addT(tmpAll[encI][info.RtpI + 1], "is_KeyFrame", False)
        final[encI * info.frameL + info.gotI: encI * info.frameL + info.afterRenderI + 1] = tmpAll[encI][info.RtpI + 1]

    if "KOYONYONG: PSNR:" in sendLine:
        tmpAll[encI][info.PSNRI] = int(float(sendLine[sendLine.index("AVERAGE: ") + len("AVERAGE: ") : ])* 10000)
        final[encI * info.frameL + info.PSNRI] = tmpAll[encI][info.PSNRI]

    if encLog in sendLine:
        tmpAll[encI][info.SizeI] = int(sendLine[sendLine.index(encLog) + len(encLog) : sendLine.index(timeLog)])
        final[encI * info.frameL + info.SizeI] = tmpAll[encI][info.SizeI]


    if "KOYONYONG: encoded_image sent:" in sendLine:
        tmpAll[encI][info.RtpI] = int(sendLine[sendLine.index(", rtpTimeStamp: ") + len(", rtpTimeStamp: ") : sendLine.index(timeLog)])%10000000
        tmpAll[encI][info.RtpI + 1] = addT(tmpAll[encI][info.RtpI + 1], "sendT", getTime(sendLine, timeLog))
        tmpAll[encI][info.tmpDroppedI] = 1
        final[encI * info.frameL + info.RtpI] = tmpAll[encI][info.RtpI]
        final[encI * info.frameL + info.gotI: encI * info.frameL + info.afterRenderI + 1] = tmpAll[encI][info.RtpI + 1]
        final[encI * info.frameL + info.DroppedI] = 1

    #dropped in enc
    if "NOTHING111" in sendLine:
        for i in range(info.SizeI, info.RtpI + 1):
            tmpAll[encI][i] = 0
        tmpAll[encI][info.tmpDroppedI] = 0
        for i in range(info.SizeI, info.RtpI + 1):
            final[encI * info.frameL + i] = 0
        final[encI * info.frameL + info.DroppedI] = 0

    if "KOYONYONG: After enc" in sendLine:
        tmpAll[encI][info.RtpI + 1] = addT(tmpAll[encI][info.RtpI + 1], "afterEncT", getTime(sendLine, timeLog))
        final[encI * info.frameL + info.gotI: encI * info.frameL + info.afterRenderI + 1] = tmpAll[encI][info.RtpI + 1]
        encI += 1

    return tmpAll, encI, frameCnt

def processDecLine(recvLine, decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop):
    if "KOYONYONG: first packet in:" in recvLine:
        completeFrame.append([0, 0, int(getTime(recvLine, timeLog)/1000)% 1000000, 0])

    if "KOYONYONG: last packet in:" in recvLine:
        completeFrame[inI][info.cIn2I] = int(getTime(recvLine, timeLog)/1000)% 1000000

    if "KOYONYONG: one complete frame" in recvLine:
        completeFrame[inI][info.cSizeI] = int(recvLine[recvLine.index("KOYONYONG: one complete frame ") + len("KOYONYONG: one complete frame ") : recvLine.index(", frame->Timestamp(): ")])
        completeFrame[inI][info.cRtpI] = int(recvLine[recvLine.index(", frame->Timestamp(): ") + len(", frame->Timestamp(): ") :])% 10000000
        inI += 1

    if "KOYONYONG: before decode:" in recvLine:
        decFrame.append([0, 0, addT([], "beforeDecT", getTime(recvLine, timeLog)), 0])

    if decLog in recvLine:
        decFrame[decI][info.dSizeI] = int(recvLine[recvLine.index(decLog) + len(decLog):recvLine.index(", timeStamp: ")])
        decFrame[decI][info.dRtpI] = int(recvLine[recvLine.index(", timeStamp: ") + len(", timeStamp: "):])%10000000

    if "KOYONYONG: after decode:" in recvLine:
        decFrame[decI][info.dRtpI + 1] = addT(decFrame[decI][info.dRtpI + 1], "afterDecT", getTime(recvLine, timeLog))
        i = len(completeFrame) - 1
        while i >= 0:
            if completeFrame[i][info.cRtpI] == decFrame[decI][info.cRtpI]:
                decFrame[decI][info.dRtpI + 1][4:6] = completeFrame[i][info.cIn1I:]
                completeFrame.pop(i)
                inI -= 1
                break
            i -= 1
        decI += 1

    if "KOYONYONG: IncomingVideoStream::OnFrame atTime:" in recvLine:
        decFrame[renI][info.dRtpI + 1] = addT(decFrame[renI][info.dRtpI + 1], "beforeRenderT", getTime(recvLine, timeLog))
        renI += 1

    if "KOYONYONG: added frame: " in recvLine:
        decFrame[addI][info.dRtpI + 1] = addT(decFrame[addI][info.dRtpI + 1], "RenQueueRecved", getTime(recvLine, timeLog))
        addI += 1

    if "KOYONYONG: Frame scheduled out of order," in recvLine \
            or "KOYONYONG: Too old frame, " in recvLine\
            or "KOYONYONG: Frame too long into the future," in recvLine:
        decFrame[addI - 1][info.dDroppedI] = -3

    if "KOYONYONG: ++frames_dropped_:" in recvLine:
        writDrop += 1

    if "KOYONYONG: written to frame:" in recvLine:
        while (decFrame[writI][info.dDroppedI] == -3):
            writI += 1
        while writDrop > 0:
            decFrame[writI][info.dDroppedI] = -3
            writDrop -= 1
            writI += 1
        decFrame[writI][info.dRtpI + 1] = addT(decFrame[writI][info.dRtpI + 1], "afterRenderT", getTime(recvLine, timeLog))
        decFrame[writI][info.dDroppedI] = 1
        writI += 1
    return decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop

def appRecvProxy(argv, allFrame, recv_send_pipe, cc):
    estimator_class = find_estimator_class(cc)
    estimator = estimator_class('gcc')
    recvf = open("log/recv.txt", 'w')
    # appRecv = subprocess.Popen(
    #     "./peerconnection_serverless.origin " + argv,
    #     stdin=subprocess.PIPE,
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.STDOUT, shell=True)
    appRecv = subprocess.Popen(
        argv,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, shell=True)

    recv_send_pipe.send(1)
    appSendPID = recv_send_pipe.recv()
    t = Timer(5, testConnection, args = [appRecv, appRecv.pid, appSendPID])
    t.start()
    #make sure the connection is up, if not, kill it!

    decFrame = []
    completeFrame = []
    inI = 0
    decI = 0
    renI = 0
    addI = 0
    writI = 0
    writDrop = 0
    packet_record = PacketRecord()
    flag, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack = processR(appRecv.stdout, appRecv.stdin, recvf, decFrame, completeFrame, inI, decI, renI, addI, writI, allFrame, writDrop, estimator, packet_record, cc)
    if flag:
        appRecv.wait()
    else:
        print("bwe out of range! terminate!!", flush=True)
        kill_process_and_children(appRecv.pid)
        print("killed appRecv!!", flush=True)
        appRecv.wait()
        kill_process_and_children(appSendPID)
        print("killed appSend!!", flush=True)
    #trackAllFrame = allDelay.getAllFrame()
    #PSNRTrack = allDelay.getPSNR(trackAllFrame)
    #FrameDelayTrack = allDelay.getFrameDelay(trackAllFrame)
    #FrameSkipTrack = allDelay.frameSkip(trackAllFrame)
    drawPlt('time', 'recvRate', f'tests/{cc}/track/recvRateTrack.jpg', timeTrack, recvRateTrack)
    drawPlt('time', 'delay', f'tests/{cc}/track/delayTrack.jpg', timeTrack, delayTrack)
    drawPlt('time', 'loss', f'tests/{cc}/track/lossTrack.jpg', timeTrack, lossTrack)
    drawPlt('frame', 'PSNRTrack', f'tests/{cc}/track/PSNRTrack.jpg', range(len(PSNRTrack)), PSNRTrack)
    drawPlt('frame', 'FrameDelayTrack', f'tests/{cc}/track/FrameDelayTrack.jpg', range(len(FrameDelayTrack)), FrameDelayTrack)
    drawPlt('frame', 'FrameSkipTrack', f'tests/{cc}/track/FrameSkipTrack.jpg', range(len(FrameSkipTrack)), FrameSkipTrack)
    print("len of all tracks: ", len(recvRateTrack), len(delayTrack), len(lossTrack),\
                     len(PSNRTrack), len(FrameDelayTrack), len(FrameSkipTrack))
    f=open(f'tests/{cc}/track/trackPickle','wb')
    pickle.dump([[recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack], \
           packet_record], f, 0)
    f.close()


    totalLoss = packet_record.calculate_total_loss_ratio()
    totalDelay = packet_record.calculate_total_delay()
    totalRate = packet_record.calculate_total_receiving_rate()

def appSendProxy(argv, allFrame, send_recv_pipe):
    sendf = open("log/send.txt", 'w')
    print("./peerconnection_serverless.origin " + argv)
    appSend = subprocess.Popen(
        argv,
        #"./peerconnection_serverless.origin " + argv,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, shell=True)
    send_recv_pipe.send(appSend.pid)
    encI = 0
    frameCnt = 0
    tmpAll = []
    try:
        processS(appSend.stdout, sendf, tmpAll, encI, frameCnt, allFrame)
        appSend.wait()
    except:
        appSend.terminate()
        appSend.wait()
        error_message = traceback.format_exc()
        error_message = "\n{}".format(error_message)
        sys.stderr.write(error_message)
        if len(argv) == 0:
            return
        config_file = argv
        config_file = json.load(open(config_file, "r"))
        if "logging" not in config_file:
            return
        if "enabled" not in config_file["logging"] or not config_file["logging"]["enabled"]:
            return
        with open(config_file["logging"]["log_output_path"], "a") as log_file:
            log_file.write(error_message)



def processS(Sout, sendf, tmpAll, encI, frameCnt, allFrame):
    while True:
        lineS = Sout.readline()
        if not lineS :
            break
        if isinstance(lineS, bytes):
            lineS = lineS.decode("utf-8")
        tmpAll, encI, frameCnt = processEncLine(lineS, tmpAll, encI, frameCnt, allFrame)


        sendf.write(lineS)
        sendf.flush()



def processR(Rout, Rin, recvf, decFrame, completeFrame, inI, decI, renI, addI, writI, allFrame, writDrop, estimator, packet_record, cc):
    #global estimator
    processStat = ProcessStat(1)
    lastT = 0
    statDecI = 0
    statAllI = 0
    NextDecStartI = 0
    delayTrack = []
    lossTrack = []
    recvRateTrack = []
    PSNRTrack = []
    FrameDelayTrack = []
    FrameSkipTrack = []
    timeTrack = []
    recv_ratef = open('log/recv_rate.txt', 'w')
    while True:
        startAll = statAllI
        lineR = Rout.readline()
        if not lineR :
            break
        if isinstance(lineR, bytes):
            lineR = lineR.decode("utf-8")
            if "Received unknown message. BYE" in lineR \
                or "(openssl_stream_adapter.cc:912): Cleanup" in lineR \
                or "No decodable frame in" in lineR \
                or "Channel disabled" in lineR \
                or "Selected connection destroyed. Will choose a new one." in lineR:
                                # Binding request timed out from
                recvf.write(lineR)
                recvf.flush()
                return False, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack

        decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop = processDecLine(lineR, decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop)
        stats = fetch_stats(lineR, recvf)
        if stats:
            estimator.report_states(stats)
            continue
        request = request_estimated_bandwidth(lineR)

        if request:
            print("RQT: gotRequest: ", round(time.time() * 1000)- lastT)
            lastT = round(time.time() * 1000)
            recvf.write(lineR)
            recvf.flush()
            if cc == 'gcc':
                packet_list = sorted(estimator.intervalPackets_list, key = lambda x: x.receive_timestamp)
            if cc == 'hrcc':
                packet_list = sorted(estimator.gcc_estimator.intervalPackets_list, key = lambda x: x.receive_timestamp)
            print("RQT: sorted: ", round(time.time() * 1000)- lastT)
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
                packet_info.bandwidth_prediction = 0    #unused in here
                packet_record.on_receive(packet_info, firstPkt)
                print(f"one pkt: {pkt.sequence_number} ; {pkt.receive_timestamp} at {round(time.time() * 1000)}")
                firstPkt = False
            print("RQT: for pkt: ", round(time.time() * 1000)- lastT)
            bweRequestTime = round(time.time() * 1000)
            timeTrack.append(bweRequestTime)
            receiving_rate = packet_record.calculate_receiving_rate(interval=200)
            recvRateTrack.append(receiving_rate)
            recv_ratef.write(f"{receiving_rate} ; {round(time.time()* 1000000)}\n")

            print("receiving_rate: ", receiving_rate)       #bps
            delay = packet_record.calculate_average_delay(interval=200)
            delayTrack.append(delay)
            print("delay: ", delay)
            loss_ratio, burstLoss_ratio = packet_record.calculate_loss_ratio(interval=200)
            lossTrack.append(loss_ratio)
            print("loss_ratio: ", loss_ratio)
            print("RQT: append: ", round(time.time() * 1000)- lastT)
            bandwidth = estimator.get_estimated_bandwidth()
            print("RQT: get_estimated_bandwidth: ", round(time.time() * 1000)- lastT)
            stat = []
            tmpAllFrame = allFrame
            tmpcnt = 0
            for i in tmpAllFrame:

                print(f"tmpAllFrame[{tmpcnt}] = ", i)
                tmpcnt += 1
                if tmpcnt > 20:
                    break
            tmpcnt = 0
            for i in allFrame:
                print(f"allFrame[{tmpcnt}] = ", i)
                tmpcnt += 1
                if tmpcnt > 20:
                    break

            while statDecI < len(decFrame):
                if decFrame[statDecI][info.dDroppedI] == 0:
                    break
                #this complete frame is decoded, find the encode log
                while allFrame[statAllI * info.frameL + info.DroppedI] == 0:
                    stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
                    statAllI += 1
                while decFrame[statDecI][info.dRtpI] != allFrame[statAllI * info.frameL + info.RtpI]:
                    allFrame[statAllI * info.frameL + info.DroppedI] = -1
                    stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
                    statAllI += 1
                    if (statAllI * info.frameL + info.DroppedI) > len(allFrame):
                        print(f"allFrame out of index error! Current track length is: {len(recvRateTrack)}")
                        return False, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack
                    while allFrame[statAllI * info.frameL + info.DroppedI] == 0:
                        stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
                        statAllI += 1
                        if (statAllI * info.frameL + info.DroppedI) > len(allFrame):
                            print(f"allFrame out of index error! Current track length is: {len(recvRateTrack)}")
                            return False, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack
                if decFrame[statDecI][info.dRtpI] == allFrame[statAllI * info.frameL + info.RtpI]:
                    allFrame[statAllI * info.frameL + info.recv1I:statAllI * info.frameL + info.afterRenderI + 1] = decFrame[statDecI][info.dRtpI + 1][5:]
                if decFrame[statDecI][info.dDroppedI] == -3:
                    allFrame[statAllI * info.frameL + info.DroppedI] = -3
                stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
                statDecI += 1
                statAllI += 1
            finalAll = statAllI
            print("RQT: finalAll: ", round(time.time() * 1000)- lastT)

            print("this stat: ")
            for i in range(startAll, finalAll):
                print(allFrame[i * info.frameL: i * info.frameL + info.frameL - 1])

            flag, psnrStat, delayStat, skipStat, isKey, width  = processStat.processStat(stat, info.PSNRI, info.widthI, info.DroppedI, info.sendI, info.beforeDecI, info.isKeyI)
            if flag:
                statePsnr, stateDelay, stateSkip = processStat.gotState(psnrStat[-1], delayStat[-1], skipStat[-1])
                if len(statePsnr) == 1:
                    PSNRTrack.append(statePsnr[-1])
                    FrameDelayTrack.append(stateDelay[-1])
                    FrameSkipTrack.append(stateSkip[-1])
            else:
                print("reward dont have psnr, skip, frame delay, cuz stat is empty")
                PSNRTrack.append(0)
                FrameDelayTrack.append(0)
                FrameSkipTrack.append(0)
            print("PSNR: ", PSNRTrack[-1])
            print("FrameDelay: ", FrameDelayTrack[-1])
            print("FrameSkip: ", FrameSkipTrack[-1])

            print("RQT: Frame: ", round(time.time() * 1000)- lastT)

            Rin.write("{}\n".format(int(bandwidth)).encode("utf-8"))
            Rin.flush()
            print("Bwe Sent: ", round(time.time() * 1000) - lastT)
            continue
        recvf.write(lineR)
        recvf.flush()
    return True, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack
    #print("decFrame:")
    #for i in decFrame:
    #    print(i)


def run(argv, cc):
    print(argv)

    sudoPW = "1"
    # initiate allFrame with -777
    allFrame = Array('i', range(info.frameL * 30 * 60 * 2))
    for i in range(len(allFrame)):
        allFrame[i] = -777

    (gymPipe, rtcPipe) = Pipe()
    (recv_send_pipe, send_recv_pipe) = Pipe()
    p1 = mp.Process(target=appRecvProxy, args=(argv[1], allFrame, recv_send_pipe, cc))
    p2 = mp.Process(target=appSendProxy, args=(argv[0], allFrame, send_recv_pipe))


    p1.start()
    if send_recv_pipe.recv() == 1:
        print("appRecv started")
        time.sleep(1)
        p2.start()

    p1.join()
    p2.join()
    for i in allFrame:
        print(i)
    print("finish")

def main():
    portNum = 8000
    traceRandom = random.randint(0, 999)
    if traceRandom < 500:
        traceType = 'random'
    else:
        traceType = 'periodic'
    traceNum = traceRandom % 500
    queLength = random.randint(6, 349)
    lossRate = float(random.randint(0, 500)) / 100
    video = random.randint(0, 4)
    videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
    traceType = 'periodic'
    traceNum = 438
    # args = [f"-- sh ./rtcGym/alphartc_gym/sh/pcsend8001.sh", f"./rtcGym/alphartc_gym/json/receiver_pyinfer8001.json"]
    # args = [f"mm-link mahiTraces/{traceType}/trace{traceNum}.trace 12mbps.trace --uplink-queue=droptail --uplink-queue-args=\"packets={queLength}\" mm-loss uplink {lossRate/100} " + \
    #         f"-- sh ./rtcGym/alphartc_gym/shs/sh_{videos[video]}/pcsend{portNum}.sh", \
    #             f"./rtcGym/alphartc_gym/jsons/json_{videos[video]}/receiver_pyinfer{portNum}.json"]
    args = [
        f"mm-link mahiTraces/{traceType}/trace{traceNum}.trace 12mbps.trace --uplink-queue=droptail --uplink-queue-args=\"packets={queLength}\" mm-loss uplink {lossRate / 100} " + \
        f"-- sh ./rtcGym/alphartc_gym/shs/sh_{videos[video]}/pcsend{portNum}.sh", \
        f"sh ./rtcGym/alphartc_gym/shs/sh_{videos[video]}/pcrecv{portNum}.sh"]
    # cc = 'hrcc'
    cc = 'gcc'
    run(args, cc)
    
    plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, plotTraceT, plotTrace, \
                    plotRecvT, plotRecv, mahiT, mahiRate = bitRateAnalysis2.getPLTlist(traceType, traceNum)
    plotResult.plt_track(plotTargetT, plotTarget, plotEncT, plotEnc, \
                    plotSetT, plotSet, plotTraceT, plotTrace, plotRecvT, plotRecv, mahiT, mahiRate,  f'tests/{cc}/track/track_{traceType[0]}:{traceNum}.jpg')




def drawPlt(xlabel, ylabel, pltName, x, y):
    plt.cla()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(pltName)

def testConnection(appRecv, appRecvPID, appSendPID):
    recvf = open("log/recv.txt", 'r')
    count=len(recvf.readlines())
    print("recvf lines: ", count, flush=True)
    if count <= 2:
        print("connection not up! kill!", flush=True)
        kill_process_and_children(appRecvPID)
        print("killed appRecv!!", flush=True)
        appRecv.wait()
        kill_process_and_children(appSendPID)
        print("killed appSend!!", flush=True)
        print("all killed!", flush=True)

    recvf.close()


def kill_process_and_children(pid: int, sig: int = 15):
    try:
        proc = psutil.Process(pid)
    except psutil.NoSuchProcess as e:
        # Maybe log something here
        print("fail in proc", flush=True)
        return

    for child_process in proc.children(recursive=True):
        try:
            child_process.send_signal(sig)
        except psutil.NoSuchProcess as e:
            # Maybe log something here
            print("fail in child_process", flush=True)
            continue
    try:
        proc.send_signal(sig)
    except psutil.NoSuchProcess as e:
        # Maybe log something here
        print("fail in proc.send_signal", flush=True)

if __name__ == "__main__":
    main()
