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
from threading import Timer
from tracemalloc import start

from torch import rand

from printLog import printLog
import signal
import psutil
import random
from CLCC.frame_info import *
RequestBandwidthCommand = "RequestBandwidth"
timeLog = " atTime: "
encLog = "KOYONYONG: encoded_image.size(): "
decLog = "KOYONYONG: decoded size: "

# same fifo error
SENDER_PIPE_PATH = "/home/yinwenpei/rtc_signal/sender_fifo"

import info

def map_actor_bwefactor(active_loss, width):
    if active_loss == 1:
        bwefactor = 1.2
        # bwefactor = 0.9 + width/1280/2
        # bwefactor = 0.9 + width/1280
    elif active_loss == 2 or active_loss == 3:
        # bwefactor = 1 + width/1280
        bwefactor = 1
    else:
        bwefactor = 1
    return bwefactor


def Action_Proxy(Sender_PIPE_PATH, Receive_pipe_from_RL):
    os.system("rm -rf "+Sender_PIPE_PATH)
    os.system("mkfifo "+Sender_PIPE_PATH)
    Sender_fd = os.open(Sender_PIPE_PATH, os.O_WRONLY)
    while True:
        msg_action = Receive_pipe_from_RL.recv()
        print("msg action: ", msg_action)
        try:
            os.write(Sender_fd, str(msg_action).encode())
        except:
            os.system("rm -rf " + Sender_PIPE_PATH)
            os.system("mkfifo " + Sender_PIPE_PATH)




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

def find_estimator_class():
    import rtcGym.alphartc_gym.HRCC.BandwidthEstimator_HRCC
    import rtcGym.alphartc_gym.HRCC.BandwidthEstimator_gcc
    #return HRCC.BandwidthEstimator_HRCC.Estimator
    return rtcGym.alphartc_gym.HRCC.BandwidthEstimator_gcc.GCCEstimator

def addT(T, type, time):
    if type != "is_KeyFrame":
        time = int(time / 1000)
        time = int(time % 1000000)
    if T == []:
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if type == "gotT":
        T[0] = time
    elif type == "beforeEncT":
        T[1] = time
    elif type == "sendT":
        T[2] = time
    elif type == "complete_frameT":
        T[3] = time
    elif type == "beforeDecT":
        T[4] = time
    elif type == "afterDecT":
        T[5] = time
    elif type == "beforeRenderT":
        T[6] = time
    elif type == "RenQueueRecved":
        T[7] = time
    elif type == "afterRenderT":
        T[8] = time
    return T

def getTime(line, log):
    return int(line[line.index(log) + len(log): ])


def appRecvProxy(argv, allFrame, pipe, recv_send_pipe):
    recvf = open(f"log/recv.txt", 'w')
    print("./peerconnection_serverless.origin " + argv, flush=True)
    appRecv = subprocess.Popen(
        # "./peerconnection_serverless.origin " + argv,
        argv,
        bufsize=1,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, shell=True)

    printLog(f"recv_trace_pipe.recv(): ", info.logSwitch, None)
    recv_send_pipe.send(1)  # to start appSend
    appSendPID = recv_send_pipe.recv()
    printLog(f"recv_send_pipe.recv(): ", info.logSwitch, None)
    print("2PID recved! ", flush=True)
    t = Timer(5, testConnection,
              args=[appRecv, appRecv.pid, appSendPID])  # make sure the connection is up, if not, kill it!
    t.start()

    decFrame = []
    completeFrame = []
    renderFrame = [0]
    inI = 0
    decI = 0
    renI = 0
    addI = 0
    writI = 0
    writDrop = 0
    try:
        flag = processR(appRecv.stdout, appRecv.stdin, recvf, decFrame, completeFrame, renderFrame,
                        allFrame, pipe, appRecv)
        if flag:
            appRecv.wait()
        else:
            print("bwe out of range! terminate!!", flush=True)
            kill_process_and_children(appRecv.pid)
            print("killed appRecv!!", flush=True)
            appRecv.wait()
            kill_process_and_children(appSendPID)
            print("killed appSend!!", flush=True)

        pipe.send(0)  # 0 end 1 asking for bwe

    except:
        appRecv.terminate()
        appRecv.wait()
        error_message = traceback.format_exc()
        error_message = "\n{}".format(error_message)
        sys.stderr.write(error_message)
        if len(sys.argv[1:]) == 0:
            return
        config_file = sys.argv[1]
        config_file = json.load(open(config_file, "r"))
        if "logging" not in config_file:
            return
        if "enabled" not in config_file["logging"] or not config_file["logging"]["enabled"]:
            return
        with open(config_file["logging"]["log_output_path"], "a") as log_file:
            log_file.write(error_message)



def processEncLine(sendLine, tmpAll, encI, frameCnt, final):
    if "YINWENPEI: got frame ID" in sendLine:
        frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
        final[frameCnt * timelistL + NumI] = frameCnt
        final[frameCnt * timelistL + sizeI] = 1
        final[frameCnt * timelistL + psnrI] = 1
        final[frameCnt * timelistL + widthI] = 1
        final[frameCnt * timelistL + heightI] = 1
        final[frameCnt * timelistL + gotTI: frameCnt * timelistL + afterRenderTI + 1] = addT([], "gotT",
                                                                                             getTime(sendLine, timeLog))
        # print(sendLine)

    if "YINWENPEI: Before enc" in sendLine:
        # print(sendLine)
        frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
        final[frameCnt * timelistL + NumI] = frameCnt
        final[frameCnt * timelistL + widthI] = int(sendLine[sendLine.index("width") + 6:sendLine.index("height") - 2])
        final[frameCnt * timelistL + heightI] = int(sendLine[sendLine.index("height") + 7:sendLine.index("at") - 2])
        final[frameCnt * timelistL + beforeEncTI] = int((getTime(sendLine, timeLog) / 1000)) % 1000000

    if "YINWENPEI: PSNR" in sendLine:
        final[frameCnt * timelistL + psnrI] = int(float(sendLine[sendLine.index("AVERAGE: ") + len("AVERAGE: ") : ])* 10000)
        print("PSNR frameCnt:", frameCnt)
        # final[encI * info.frameL + info.PSNRI] = tmpAll[encI][info.PSNRI]

    # if "YINWENPEI after enc atTime" in sendLine:
    #     print(int((getTime(sendLine, timeLog) / 1000)) % 1000000)

    if "YINWENPEI: send encoded_image:" in sendLine:
        # print(sendLine)
        frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
        final[frameCnt * timelistL + NumI] = frameCnt
        final[frameCnt * timelistL + sizeI] = int(sendLine[sendLine.index("size") + 5:sendLine.index("at") - 2])
        final[frameCnt * timelistL + sendTI] = int((getTime(sendLine, timeLog) / 1000)) % 1000000

    if "KOYONYONG" in sendLine:
        print(sendLine)

    return frameCnt

# def processDecLine(recvLine, decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop):
#     if "KOYONYONG: first packet in:" in recvLine:
#         completeFrame.append([0, 0, int(getTime(recvLine, timeLog)/1000)% 1000000, 0])
#
#     if "KOYONYONG: last packet in:" in recvLine:
#         completeFrame[inI][info.cIn2I] = int(getTime(recvLine, timeLog)/1000)% 1000000
#
#     if "KOYONYONG: one complete frame" in recvLine:
#         completeFrame[inI][info.cSizeI] = int(recvLine[recvLine.index("KOYONYONG: one complete frame ") + len("KOYONYONG: one complete frame ") : recvLine.index(", frame->Timestamp(): ")])
#         completeFrame[inI][info.cRtpI] = int(recvLine[recvLine.index(", frame->Timestamp(): ") + len(", frame->Timestamp(): ") :])% 10000000
#         inI += 1
#
#     if "KOYONYONG: before decode:" in recvLine:
#         decFrame.append([0, 0, addT([], "beforeDecT", getTime(recvLine, timeLog)), 0])
#
#     if decLog in recvLine:
#         decFrame[decI][info.dSizeI] = int(recvLine[recvLine.index(decLog) + len(decLog):recvLine.index(", timeStamp: ")])
#         decFrame[decI][info.dRtpI] = int(recvLine[recvLine.index(", timeStamp: ") + len(", timeStamp: "):])%10000000
#
#     if "KOYONYONG: after decode:" in recvLine:
#         decFrame[decI][info.dRtpI + 1] = addT(decFrame[decI][info.dRtpI + 1], "afterDecT", getTime(recvLine, timeLog))
#         i = len(completeFrame) - 1
#         while i >= 0:
#             if completeFrame[i][info.cRtpI] == decFrame[decI][info.cRtpI]:
#                 decFrame[decI][info.dRtpI + 1][5:7] = completeFrame[i][info.cIn1I:]
#                 completeFrame.pop(i)
#                 inI -= 1
#                 break
#             i -= 1
#         decI += 1
#
#     if "KOYONYONG: IncomingVideoStream::OnFrame atTime:" in recvLine:
#         decFrame[renI][info.dRtpI + 1] = addT(decFrame[renI][info.dRtpI + 1], "beforeRenderT", getTime(recvLine, timeLog))
#         renI += 1
#
#     if "KOYONYONG: added frame: " in recvLine:
#         decFrame[addI][info.dRtpI + 1] = addT(decFrame[addI][info.dRtpI + 1], "RenQueueRecved", getTime(recvLine, timeLog))
#         addI += 1
#
#     if "KOYONYONG: Frame scheduled out of order," in recvLine \
#             or "KOYONYONG: Too old frame, " in recvLine\
#             or "KOYONYONG: Frame too long into the future," in recvLine:
#         decFrame[addI - 1][info.dDroppedI] = -3
#
#     if "KOYONYONG: ++frames_dropped_:" in recvLine:
#         writDrop += 1
#
#     if "KOYONYONG: written to frame:" in recvLine:
#         while (decFrame[writI][info.dDroppedI] == -3):
#             writI += 1
#         while writDrop > 0:
#             decFrame[writI][info.dDroppedI] = -3
#             writDrop -= 1
#             writI += 1
#         decFrame[writI][info.dRtpI + 1] = addT(decFrame[writI][info.dRtpI + 1], "afterRenderT", getTime(recvLine, timeLog))
#         decFrame[writI][info.dDroppedI] = 1
#         writI += 1
#     return decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop

def processDecLine(lineR, decFrame, completeFrame, renderFrame, allFrame, Recv_frame_id):
    if "YINWENPEI: one complete frame" in lineR:
        Recv_frame_id = int(lineR[lineR.index("ID") + 3:lineR.index(",")])
        allFrame[Recv_frame_id * timelistL + complete_frameI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
        completeFrame.append(Recv_frame_id)
        # print(lineR)
    if "YINWENPEI before decode frame" in lineR:
        # print(lineR)
        try:
            Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
            allFrame[Recv_frame_id * timelistL + beforeDecTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
        except:
            print(lineR)

    if "YINWENPEI: after decode frame" in lineR:
        # print(lineR)
        try:
            Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
            allFrame[Recv_frame_id * timelistL + afterDecTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
            decFrame.append(Recv_frame_id)
        except:
            print(lineR)

    if "YINWENPEI: IncomingVideoStream::OnFrame ID" in lineR:
        # print(lineR)
        Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
        allFrame[Recv_frame_id * timelistL + beforeRenderTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000

    if "YINWENPEI: RenderQueue frame ID" in lineR:
        # print(lineR)
        Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime") - 2])
        allFrame[Recv_frame_id * timelistL + RenQueueReceivedI] = int((getTime(lineR, timeLog) / 1000)) % 1000000

    if "YINWENPEI: written to frame" in lineR:
        print(lineR)
        Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime") - 2])
        allFrame[Recv_frame_id * timelistL + afterRenderTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
        renderFrame.append(Recv_frame_id)

    return decFrame, completeFrame, renderFrame



def appSendProxy(argv, allFrame, send_recv_pipe):
    sendf = open(f"log/send.txt", 'w')
    appSend = subprocess.Popen(
        #"mm-link mahiTraces/periodic/trace0.trace 12mbps.trace " + argv,
        argv,
        bufsize=1,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, shell= True)

    send_recv_pipe.send(appSend.pid)
    encI = 0
    frameCnt = 0
    tmpAll = []
    try:
        flag = processS(appSend.stdout, sendf, tmpAll, encI, frameCnt, allFrame)
        if flag:
            appSend.wait()
        else:
            appSend.terminate()
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

def main():
    mp.set_start_method('fork')
    # initiate allFrame with -777
    allFrame = Array('i', range(info.frameL * 30 * 60 * 2))
    for i in range(len(allFrame)):
        allFrame[i] = -777
    p1 = mp.Process(target=appRecvProxy, args=(sys.argv[2], allFrame))
    p2 = mp.Process(target=appSendProxy, args=(sys.argv[1], allFrame))

    mode = "square."
    model_filename = "traces." + mode + "trace2"
    modellib = importlib.import_module(model_filename)
    t1 = mp.Process(target = modellib.link)

    p1.start()
    time.sleep(1)
    t1.start()
    p2.start()

    p1.join()
    p2.join()
    t1.join()
    print("finish")



def processS(Sout, sendf, tmpAll, encI, frameCnt, allFrame):
    while True:
        lineS = Sout.readline()
        if not lineS :
            print("processS  break")
            return True
            break
        if isinstance(lineS, bytes):
            lineS = lineS.decode("utf-8")
            if "BYE" in lineS:
                sendf.write(lineS)
                sendf.flush()
                return False
        frameCnt = processEncLine(lineS, tmpAll, encI, frameCnt, allFrame)


        sendf.write(lineS)
        sendf.flush()
    #print("allFrame:")
    #for i in allFrame:
    #    print(i)

def processR(Rout, Rin, recvf, decFrame, completeFrame,renderFrame, allFrame, pipe, appRecv):
    debugf = open("log/debug.log", 'w')
    debugf.close()
    debugf = open("log/debug.log", 'a+')
    estimator_class = find_estimator_class()
    estimator = estimator_class('gcc')
    lastT = 0
    statDecI = 0
    statBeginI = 1  # avoid renderFrame[-1] = 0
    NextDecStartI = 0
    lastSeq = 0
    lastBWE = 300000 #used for testing the largest delay_gradient canbe
    lastExpandStatNum = None
    startTime = None
    tmpCnt = 0
    Recv_frame_id = 0
    last_bwe = 300000
    while True:
        starBeginI = statBeginI

        '''
        if not appRecv.poll():
            lineR = Rout.readline()
            print("got lineR", flush=True)
            print("appRecv_alive?: ", appRecv.poll(), flush=True)
        else:
            print("processR  break", flush=True)
            return True
            break
        '''
        lineR = Rout.readline()
        if not lineR:
            print("processR  break", flush=True)
            return True
            break
        if isinstance(lineR, bytes):
            lineR = lineR.decode("utf-8")
            if "Received unknown message. BYE" in lineR \
                or "(openssl_stream_adapter.cc:912): Cleanup" in lineR \
                or "No decodable frame in" in lineR \
                or "Channel disabled" in lineR \
                or "Network is unreachable" in lineR \
                or "Selected connection destroyed. Will choose a new one." in lineR:
                                # Binding request timed out from
                recvf.write(lineR)
                recvf.flush()
                return False

        decFrame, completeFrame, renderFrame = processDecLine(lineR, decFrame, completeFrame, renderFrame, allFrame,Recv_frame_id)
        # decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop = \
        #     processDecLine(lineR, decFrame, completeFrame, inI, decI, renI, addI, writI, writDrop)  #process every output line, record the frame information
        stats = fetch_stats(lineR, recvf)
        if stats:
            estimator.report_states(stats)
            continue
        request = request_estimated_bandwidth(lineR)
        # print("request:",request)
        if request:
            printLog(f"got request at ", info.logSwitch, None)


            lastT = round(time.time() * 1000)
            recvf.write(lineR)
            recvf.flush()
            printLog(f"after recvf.flush() at ", info.logSwitch, None)
            # if False:
            #     for i in printAllFrame:
            #         print(i)
            #     for i in decFrame:
            #         print(i)

            #sync dec and enc
            #synv till the last recved frame
            stat = []       #save the information of the frames received in the last 200ms
            # calculate the real encoded rate
            encodedSize = 0
            Encoded_count = 0
            while(statBeginI <= renderFrame[-1]):
                if statBeginI in renderFrame:
                    stat.append(allFrame[statBeginI * timelistL: statBeginI * timelistL + timelistL - 1])
                    encodedSize += allFrame[statBeginI * timelistL + sizeI]
                    Encoded_count += 1
                statBeginI += 1
            rate = encodedSize / (Encoded_count + 33) * 8 * 1000
            print("stat: 200ms: ", stat)
            print("Encoded_rate:", rate)




            # while statDecI < len(decFrame):
            #     if decFrame[statDecI][info.dDroppedI] == 0:
            #         break
            #     #this complete frame is decoded, find the encode log
            #     while allFrame[statAllI * info.frameL + info.DroppedI] == 0:
            #         stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
            #         statAllI += 1
            #     while decFrame[statDecI][info.dRtpI] != allFrame[statAllI * info.frameL + info.RtpI]:
            #         allFrame[statAllI * info.frameL + info.DroppedI] = -1
            #         stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
            #         statAllI += 1
            #         print(f"allFrame len: ", len(allFrame))
            #         print(f"allFrame[{statAllI * info.frameL + info.DroppedI}]")
            #         while allFrame[statAllI * info.frameL + info.DroppedI] == 0:
            #             stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
            #             statAllI += 1
            #     if decFrame[statDecI][info.dRtpI] == allFrame[statAllI * info.frameL + info.RtpI]:
            #         allFrame[statAllI * info.frameL + info.recv1I:statAllI * info.frameL + info.afterRenderI + 1] = decFrame[statDecI][info.dRtpI + 1][5:]
            #     if decFrame[statDecI][info.dDroppedI] == -3:
            #         allFrame[statAllI * info.frameL + info.DroppedI] = -3
            #     stat.append(allFrame[statAllI * info.frameL: statAllI * info.frameL + info.frameL - 1])
            #     statDecI += 1
            #     statAllI += 1
            #
            # printLog(f"while sync dec and enc at ", info.logSwitch, None)
            # expandStat = stat[:]    #get the encoder stat: encoded frame, return the bitrate in this interval
            # if statAllI == 0:
            #     expandI = 0
            # else:
            #     expandI = statAllI
            # print("allFrame[expand]: ", allFrame[expandI * info.frameL: expandI * info.frameL + info.frameL - 1])
            # while allFrame[expandI * info.frameL + info.NumI] != -777:
            #     expandStat.append(allFrame[expandI * info.frameL: expandI * info.frameL + info.frameL - 1])
            #     expandI += 1
            # if lastExpandStatNum != None:
            #     coveredI = 0
            #     if expandStat[coveredI][info.NumI] <= lastExpandStatNum:        #expandStat may recover the last expandStat when stat is []
            #         while coveredI < len(expandStat):
            #             if expandStat[coveredI][info.NumI] < lastExpandStatNum:
            #                 coveredI += 1
            #             elif expandStat[coveredI][info.NumI] == lastExpandStatNum:
            #                 break
            #         del (expandStat[0:coveredI + 1])
            #
            # printLog(f"after expand allFrame at ", info.logSwitch, None)
            # if expandStat != []:
            #     lastExpandStatNum = expandStat[-1][info.NumI]
            # for i in stat:
            #     print(f"stat: Num: {i[info.NumI]} ; Size: {i[info.SizeI]} ; AfterEncT: {i[info.afterEncI]} ; gotT: {i[info.gotI]} ; isKey: {i[info.isKeyI]}")
            # for i in expandStat:
            #     print(f"expandStat: Num: {i[info.NumI]} ; Size: {i[info.SizeI]} ; AfterEncT: {i[info.afterEncI]} ; gotT: {i[info.gotI]} ; isKey: {i[info.isKeyI]}")
            # print("len(stat) != len(expandStat): ", len(stat) ," ; ", len(expandStat))
            # printLog(f"after print expand stat at ", info.logSwitch, None)
            # firstExpandT = 0
            # lastExpandT = 0
            # expandSize = 0
            # firstFlag = False
            # for i in expandStat:
            #     if not firstFlag and i[info.gotI] != 0 :
            #         firstExpandT = i[info.gotI]
            #         firstFlag = True
            #     if i[info.gotI] != 0:
            #         lastExpandT = i[info.gotI]
            #     expandSize += i[info.SizeI]
            # printLog(f"after got expand size at ", info.logSwitch, None)
            # print("expandInterval: ", lastExpandT - firstExpandT, flush=True)
            # print("expandSize: ", expandSize, flush=True)
            # rate = expandSize / (lastExpandT - firstExpandT + 33) * 8 * 1000
            # print("encode rate: ", rate, flush=True)


            printLog(f"processed allFrame at ", info.logSwitch, None)
            printLog(f"send 'asking for bwe' at ", info.logSwitch, None)
            pipe.send(1) #0 end 1 asking for bwe
            printLog(f"sent 'asking for bwe' at ", info.logSwitch, None)
            printLog(f"send [estimator, stat] at ", info.logSwitch, None)
            pipe.send([estimator, stat, last_bwe])
            printLog(f"sent [estimator, stat] at ", info.logSwitch, None)

            # gcc
            bandwidth = estimator.get_estimated_bandwidth()

            #finalAll = statAllI
            #print("this stat: ")
            #for i in range(startAll, finalAll):
                #print(allFrame[i * info.frameL: i * info.frameL + info.frameL - 1])

            printLog(f"pc wait for bwe at ", info.logSwitch, None)
            bwe = pipe.recv()
            # bwe = bwe * 1000000
            print("pipe recv bwe:", bwe)

            # bwefactor = pipe.recv()
            # print("pipe recv bwefactor:", bwefactor)

            # according to frame loss rate, modify bitrate
            # try:
            #     bwefactor = map_actor_bwefactor(active_loss, stat[-1][widthI])
            # except:
            #     bwefactor = 1

            # bwe = bwefactor * bandwidth     #for test gcc

            last_bwe = int(bwe)

            # printLog(f"processed allFrame at ", info.logSwitch, None)
            # printLog(f"send 'asking for bwe' at ", info.logSwitch, None)
            # pipe.send(1) #0 end 1 asking for bwe
            # printLog(f"sent 'asking for bwe' at ", info.logSwitch, None)
            # printLog(f"send [estimator, stat] at ", info.logSwitch, None)
            # pipe.send([estimator, stat, bwe])
            # printLog(f"sent [estimator, stat] at ", info.logSwitch, None)
            
            #bwe = random.randint(100000, 3000000)     #for test gcc
            '''
            if tmpCnt < 100:
                bwe = lastBWE + 30000
            else:
                bwe = lastBWE - 30000
            lastBWE = bwe
            tmpCnt += 1
            '''
            '''
            if bwe < 5000 or bwe > 4000000:    #bwe out of range!kill!
                #return False
                if bwe < 5000:
                    bwe = 5000
                if bwe > 4000000:
                    bwe = 4000000
            '''
            lastT = round(time.time() * 1000)
            printLog(f"pc got bwe at ", info.logSwitch, None)
            print("bandwidth: ", bwe)
            #printLog(f"{int(bwe) / 1000} ; \n", True, debugf)
            #Rin.write("{}\n".format(int(bandwidth)).encode("utf-8"))   #gcc
            printLog(f"pc flushed at ", info.logSwitch, None)
            Rin.write("{}\n".format(int(bwe)).encode("utf-8"))   #DRL with PSNR
            Rin.flush()
            printLog(f"Bwe Sent: {round(time.time() * 1000) - lastT} at ", info.logSwitch, None)
            continue
        recvf.write(lineR)
        recvf.flush()

def testConnection(appRecv, appRecvPID, appSendPID):
    recvf = open("log/recv.txt", 'r')
    recvflines = recvf.readlines()
    count=len(recvflines)
    print("recvf lines: ", count, flush=True)
    if count <= 2 or recvflines[-1] == RequestBandwidthCommand:
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
