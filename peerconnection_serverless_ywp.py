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
# os.system("rm result/*")
os.system("rm result/tmp/*")
# os.system("rm result/delay/*")
RequestBandwidthCommand = "RequestBandwidth"
timeLog = " atTime: "
encLog = "KOYONYONG: encoded_image.size(): "
decLog = "KOYONYONG: decoded size: "
# import info
from CLCC.frame_info import *


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
    return int(line[line.index(log) + len(log):])


def fetch_stats(line: str, recvf) -> dict:
    tmpLine = line[:]
    if "KOYONYONG" in line:  # somtimes KOYONYONG log may add to cmdinfer log, cause bad loss cnt
        line = line[:line.index("KOYONYONG")]

    line = line.strip()
    try:
        stats = json.loads(line)
        if ("KOYONYONG" in tmpLine):
            recvf.write(tmpLine[tmpLine.index("KOYONYONG"):])
            recvf.flush()
        return stats
    except json.decoder.JSONDecodeError:
        return None


def request_estimated_bandwidth(line: str) -> bool:
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
    t = Timer(5, testConnection, args=[appRecv, appRecv.pid, appSendPID])
    t.start()
    # make sure the connection is up, if not, kill it!

    decFrame = []
    completeFrame = []
    renderFrame = [0]
    packet_record = PacketRecord()
    flag, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack = processR(
        appRecv.stdout, appRecv.stdin, recvf, decFrame, completeFrame, renderFrame, allFrame, estimator, packet_record, cc)
    # processR(appRecv.stdout, appRecv.stdin, recvf, decFrame, completeFrame, inI, decI, renI, addI, writI, allFrame,
    #          writDrop, estimator, packet_record, cc)
    RTCrate = packet_record.calculate_total_receiving_rate()
    packet_delay_list, RTCdelay = packet_record.base_calculate_total_delay()
    RTCloss = packet_record.calculate_total_loss_ratio()
    print(f"In this RTC, recv_rate = {RTCrate}, delay = {RTCdelay}, loss = {RTCloss}")
    if flag:
        appRecv.wait()
    else:
        total_frame_loss_rate = 1 - len(renderFrame)/renderFrame[-1]
        print("total_frame_loss_rate: ", total_frame_loss_rate)
        print("bwe out of range! terminate!!", flush=True)
        kill_process_and_children(appRecv.pid)
        print("killed appRecv!!", flush=True)
        appRecv.wait()
        kill_process_and_children(appSendPID)
        print("killed appSend!!", flush=True)
    # #trackAllFrame = allDelay.getAllFrame()
    # #PSNRTrack = allDelay.getPSNR(trackAllFrame)
    # #FrameDelayTrack = allDelay.getFrameDelay(trackAllFrame)
    # #FrameSkipTrack = allDelay.frameSkip(trackAllFrame)
    # drawPlt('time', 'recvRate', f'tests/{cc}/track/recvRateTrack.jpg', timeTrack, recvRateTrack)
    # drawPlt('time', 'delay', f'tests/{cc}/track/delayTrack.jpg', timeTrack, delayTrack)
    # drawPlt('time', 'loss', f'tests/{cc}/track/lossTrack.jpg', timeTrack, lossTrack)
    # drawPlt('frame', 'PSNRTrack', f'tests/{cc}/track/PSNRTrack.jpg', range(len(PSNRTrack)), PSNRTrack)
    # drawPlt('frame', 'FrameDelayTrack', f'tests/{cc}/track/FrameDelayTrack.jpg', range(len(FrameDelayTrack)), FrameDelayTrack)
    # drawPlt('frame', 'FrameSkipTrack', f'tests/{cc}/track/FrameSkipTrack.jpg', range(len(FrameSkipTrack)), FrameSkipTrack)
    # print("len of all tracks: ", len(recvRateTrack), len(delayTrack), len(lossTrack),\
    #                  len(PSNRTrack), len(FrameDelayTrack), len(FrameSkipTrack))
    # f=open(f'tests/{cc}/track/trackPickle','wb')
    # pickle.dump([[recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack], \
    #        packet_record], f, 0)
    # f.close()
    #
    #
    # totalLoss = packet_record.calculate_total_loss_ratio()
    # totalDelay = packet_record.calculate_total_delay()
    # totalRate = packet_record.calculate_total_receiving_rate()


def processR(Rout, Rin, recvf, decFrame, completeFrame, renderFrame, allFrame, estimator, packet_record, cc):
    # global estimator
    processStat = ProcessStat(1)
    lastT = 0
    statDecI = 0
    statBeginI = 1  # avoid renderFrame[-1] = 0
    NextDecStartI = 0
    delayTrack = []
    lossTrack = []
    recvRateTrack = []
    PSNRTrack = []
    FrameDelayTrack = []
    FrameSkipTrack = []
    timeTrack = []
    recv_ratef = open('log/recv_rate.txt', 'w')
    Recv_frame_id = 0
    last_Recv_frame_index = 0
    while True:
        starBeginAll = statBeginI
        lineR = Rout.readline()
        if not lineR:
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
        decFrame, completeFrame, renderFrame = processDecLine(lineR, decFrame, completeFrame, renderFrame, allFrame, Recv_frame_id)
        stats = fetch_stats(lineR, recvf)
        if stats:
            estimator.report_states(stats)
            continue
        request = request_estimated_bandwidth(lineR)

        if request:
            recvf.write(lineR)
            recvf.flush()
            if cc == 'gcc':
                packet_list = sorted(estimator.intervalPackets_list, key=lambda x: x.receive_timestamp)
            if cc == 'hrcc':
                packet_list = sorted(estimator.gcc_estimator.intervalPackets_list, key=lambda x: x.receive_timestamp)
            firstPkt = True  # the first pkt in this step

            ## packet info interval summary
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
                packet_info.bandwidth_prediction = 0  # unused in here
                packet_record.on_receive(packet_info, firstPkt)
                print(f"one pkt: {pkt.sequence_number} ; {pkt.receive_timestamp} at {round(time.time() * 1000)}")
                firstPkt = False
            print("RQT: for pkt: ", round(time.time() * 1000) - lastT)
            bweRequestTime = round(time.time() * 1000)
            timeTrack.append(bweRequestTime)
            receiving_rate = packet_record.calculate_receiving_rate(interval=200)
            recvRateTrack.append(receiving_rate)
            recv_ratef.write(f"{receiving_rate} ; {round(time.time() * 1000000)}\n")

            print("receiving_rate: ", receiving_rate)  # bps
            delay = packet_record.calculate_average_delay(interval=200)
            delayTrack.append(delay)
            print("delay: ", delay)
            loss_ratio, burstLoss_ratio = packet_record.calculate_loss_ratio(interval=200)
            lossTrack.append(loss_ratio)
            print("loss_ratio: ", loss_ratio)
            print("RQT: append: ", round(time.time() * 1000) - lastT)
            bandwidth = estimator.get_estimated_bandwidth()
            print("RQT: get_estimated_bandwidth: ", round(time.time() * 1000) - lastT)

            stat = []  # save the information of the frames received in the last 200ms
            # calculate the real encoded rate
            encodedSize = 0
            Encoded_count = 0
            while (statBeginI <= renderFrame[-1]):
                if statBeginI in renderFrame:
                    stat.append(allFrame[statBeginI * timelistL: statBeginI * timelistL + timelistL - 1])
                    encodedSize += allFrame[statBeginI * timelistL + sizeI]
                    Encoded_count += 1
                statBeginI += 1
            rate = encodedSize / (Encoded_count + 33) * 8 * 1000


            ## calculate frame loss rate
            total_frame_numbers_interval = renderFrame[-1] - renderFrame[last_Recv_frame_index] + 1
            frame_loss_rate_interval = 1 - float((len(renderFrame[last_Recv_frame_index:-1])+1)/total_frame_numbers_interval)
            last_Recv_frame_index = len(renderFrame)-1
            # recvf.write("frame_loss_rate_interval:"+str(frame_loss_rate_interval))
            print("frame_loss_rate_interval:",frame_loss_rate_interval, " total_frame_numbers_interval:",total_frame_numbers_interval)
            Rin.write("{}\n".format(int(bandwidth)).encode("utf-8"))
            Rin.flush()



        recvf.write(lineR)
        recvf.flush()
    return True, recvRateTrack, delayTrack, lossTrack, PSNRTrack, FrameDelayTrack, FrameSkipTrack, timeTrack


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
    sendf = open("log/send.txt", 'w')
    print("./peerconnection_serverless.origin " + argv)
    appSend = subprocess.Popen(
        argv,
        # "./peerconnection_serverless.origin " + argv,
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
        if not lineS:
            break
        if isinstance(lineS, bytes):
            lineS = lineS.decode("utf-8")
        frameCnt = processEncLine(lineS, tmpAll, encI, frameCnt, allFrame)

        sendf.write(lineS)
        sendf.flush()


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

    if "YINWENPEI after enc atTime" in sendLine:
        print(int((getTime(sendLine, timeLog) / 1000)) % 1000000)

    if "YINWENPEI: send encoded_image:" in sendLine:
        # print(sendLine)
        frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
        final[frameCnt * timelistL + NumI] = frameCnt
        final[frameCnt * timelistL + sizeI] = int(sendLine[sendLine.index("size") + 5:sendLine.index("at") - 2])
        final[frameCnt * timelistL + sendTI] = int((getTime(sendLine, timeLog) / 1000)) % 1000000

    if "KOYONYONG" in sendLine:
        print(sendLine)

    return frameCnt

def run(argv, cc):
    print(argv)

    sudoPW = "1"
    # initiate allFrame with -777
    frame_numbers = 30 * 60 * 2
    allFrame = Array('i', range(timelistL * 30 * 60 * 2))
    # allFrame = Array(FrameInfo,frame_numbers)
    # allFrame = mp.Manager().list()
    for i in range(frame_numbers):
        allFrame[i] = -777

    (gymPipe, rtcPipe) = Pipe()
    (recv_send_pipe, send_recv_pipe) = Pipe()
    p1 = mp.Process(target=appRecvProxy, args=(argv[1], allFrame, recv_send_pipe, cc))
    p2 = mp.Process(target=appSendProxy, args=(argv[0], allFrame, send_recv_pipe))

    p1.start()
    if send_recv_pipe.recv() == 1:
        print("appRecv started")
        time.sleep(5)
        p2.start()

    p1.join()
    p2.join()
    # for i in allFrame:
    #     print(i)
    print("finish")


def main():
    os.system("rm -rf /home/yinwenpei/rtc_signal/baseline_frame_id.txt")
    portNum = 8000
    traceRandom = random.randint(0, 999)
    if traceRandom < 500:
        traceType = 'random'
    else:
        traceType = 'periodic'
    # traceNum = traceRandom % 500
    traceNum = 38
    # queLength = random.randint(6, 349)
    queLength = 168
    # lossRate = float(random.randint(0, 500)) / 100
    lossRate = 3
    # video = random.randint(0, 4)
    video = 2
    videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
    traceType = 'random'
    # traceType = 'random'
    # traceNum = 438
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


def drawPlt(xlabel, ylabel, pltName, x, y):
    plt.cla()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(pltName)


def testConnection(appRecv, appRecvPID, appSendPID):
    recvf = open("log/recv.txt", 'r')
    count = len(recvf.readlines())
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
