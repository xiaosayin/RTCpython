from pdb import Restart
import sys
import os
sys.path.append(os.getcwd())

import random
import peerconnection_serverless2
import tests_trace.bitRateAnalysis2_trace as bitRateAnalysis2_trace
import plotResult
import pickle
import math
import numpy as np
import matplotlib.pyplot as plt
import allDelay
import tests_trace.testTrain_traces as testTrain_traces
import tests.getAvgTraceBW as getAvgTraceBW
import time
randomSeed = 0
random.seed(randomSeed)

def frameFromAllDelay(videoName):
    allFrame = allDelay.getAllFrame()
    framePSNR = allDelay.getPSNR(allFrame)
    frameDelay = allDelay.getFrameDelay(allFrame)
    frameLoss = allDelay.frameSkip(allFrame)
    t1 = round(time.time())
    allDelay.cutYUV(allFrame, videoName)
    print("cutYUV used:", round(time.time()) - t1)
    t1 = round(time.time())
    avgPSNR = allDelay.drawTruePSNR()
    print("drawTruePSNR used:", round(time.time()) - t1)
    t1 = round(time.time())
    vmaf = allDelay.VMAF()
    print("allDelay.VMAF used:", round(time.time()) - t1)
    print(f"this result: PSNR: {avgPSNR}, FrameDleay: {frameDelay}, FrameLoss: {frameLoss}")
    return framePSNR, frameDelay, frameLoss, avgPSNR, vmaf

def getTestTraces(testNum):
    setf = open(f'tests_trace/DividedTestSetPickle','rb')
    traceName, queLength, lossRate, video = pickle.load(setf)
    setf.close()
    return traceName, queLength, lossRate, video

traceName, queLength, lossRate, video = getTestTraces(200)
def testCC(cc, totalNum, restart, continueID):
    if restart:
        #os.system(f"rm tests/{cc}/*")
        os.system(f"rm tests_trace/{cc}/avgPLT/*")
        os.system(f"rm tests_trace/{cc}/track/*")
        testid = 0
    else:
        testid = continueID
    
    port = 8000

    
    print("TestTracesSet:", traceName, queLength, lossRate, video)
    pkt_recv = []
    pkt_delay = []
    pkt_loss = []
    frame_psnr = []
    frame_delay = []
    frame_loss = []
    QOE_recv = []
    QOE_delay = []
    QOE_loss = []
    QOE_pkt = []
    QOE_frameQuality = []
    QOE_frameDelay = []
    QOE_frameDrop = []
    QOE_frame = []
    vmaf = []

    avg_pkt_recv = 0
    avg_pkt_delay = 0
    avg_pkt_loss = 0
    avg_frame_psnr = 0
    avg_frame_delay = 0
    avg_frame_loss = 0

    NumList = []
    while testid < totalNum:
        testName = traceName[testid]
        testQue = queLength[testid]
        testLoss = lossRate[testid]
        testVideo = video[testid]
        videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
        videos = ["vidyo4"]
        args = [f"mm-link sampledTraces/chosenTraces/{testName} 12mbps.trace --uplink-queue=droptail --uplink-queue-args=\"packets={testQue}\" mm-loss uplink {testLoss/100} " + \
            f"-- sh ./rtcGym/alphartc_gym/shs/sh_{videos[testVideo]}/pcsend{port}.sh", \
                f"./rtcGym/alphartc_gym/jsons/json_{videos[testVideo]}/receiver_pyinfer{port}.json"]
        if cc == 'hrcc' or cc == 'gcc' or cc == 'gcc_copy' or cc == 'hrcc_copy':
            if 'gcc' in cc:
                peerconnection_serverless2.run(args, 'gcc')
            if 'hrcc' in cc:
                peerconnection_serverless2.run(args, 'hrcc')
        else:
            testTrain_traces.testTrain(cc, testName, testQue, testLoss, testVideo, port)

        trackf = open(f'tests_trace/{cc}/track/trackPickle','rb')
        storageTrack = pickle.load(trackf)
        trackf.close()
        if len(storageTrack[0][0]) < 100:
            port += 1
            if (port == 8049):
                port = 8000
            testid += 1
            continue

        if (len(storageTrack[0][0]) == 0 or len(storageTrack[0][1]) == 0 or len(storageTrack[0][2]) == 0):
            print("not enough actions!")
            port += 1
            if (port == 8049):
                port = 8000
            continue
        
        NumList.append(len(storageTrack[0][0]))


        plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, plotTraceT, plotTrace, \
                    plotRecvT, plotRecv, mahiT, mahiRate = bitRateAnalysis2_trace.getPLTlist(testName)
        
        if testQue < 10:
            logQ = f"00{testQue}"
        elif testQue >= 10 and testQue < 100:
            logQ = f"0{testQue}"
        else:
            logQ = f"{testQue}"
        logL = math.floor(testLoss)
        plotResult.plt_track(plotTargetT, plotTarget, plotEncT, plotEnc, \
                    plotSetT, plotSet, plotTraceT, plotTrace, plotRecvT, plotRecv, mahiT, mahiRate,  f'tests_trace/{cc}/track/track{testid}_q:{logQ}_L:{logL}_{testName}.jpg')
        

        
        

        allFramePSNR, allFrameDelay, allFrameLoss, avgPSNR, thisvmaf = frameFromAllDelay(videos[testVideo])
        
        
        if (len(allFramePSNR) < 10 or len(allFrameDelay) < 10 or len(allFrameLoss) < 10):
            print("not enough actions!")
            port += 1
            if (port == 8049):
                port = 8000
            continue
        
        if (not thisvmaf ):
            print("vmaf break down!")
            port += 1
            if (port == 8049):
                port = 8000
            continue

        if (not avgPSNR):
            print("rtc break down!")
            port += 1
            if (port == 8049):
                port = 8000
            continue
        #frame_psnr.append(np.mean(allFramePSNR))

        print(f"pkrVSnp_recv : {storageTrack[1].calculate_total_receiving_rate()} v.s. {np.mean(storageTrack[0][0])}")
        print(f"pkrVSnp_delay: {storageTrack[1].calculate_total_delay()} v.s. {np.mean(storageTrack[0][1])}")
        print(f"pkrVSnp_loss : {storageTrack[1].calculate_total_loss_ratio()} v.s. {np.mean(storageTrack[0][2])}")
        
        delay_max, delay_min, delay_95th = storageTrack[1].calculate_max_min_95_delay()
        bwe_utility = storageTrack[1].calculate_total_receiving_rate() / getAvgTraceBW.getBW_trace(testName) / 1000
        QOE_recv.append(100 * bwe_utility)
        QOE_delay.append(100 * (delay_max - delay_95th) / (delay_max - delay_min))
        QOE_loss.append(100 * (1 - storageTrack[1].calculate_total_loss_ratio()))
        QOE_pkt.append(0.2 * QOE_recv[-1] + 0.2 * QOE_delay[-1] + 0.3 * QOE_loss[-1])

        QOE_frameQuality.append(100 * avgPSNR / 45)
        QOE_frameDelay.append(100 * (max(allFrameDelay) - np.percentile(allFrameDelay, 95)) / (max(allFrameDelay) - min(allFrameDelay)))
        QOE_frameDrop.append(100 * (1 - np.mean(allFrameLoss) ))
        QOE_frame.append(0.2 * QOE_frameQuality[-1] + 0.2 * QOE_frameDelay[-1] + 0.3 * QOE_frameDrop[-1])
 
        pkt_recv.append(storageTrack[1].calculate_total_receiving_rate())
        pkt_delay.append(storageTrack[1].calculate_total_delay())
        pkt_loss.append(storageTrack[1].calculate_total_loss_ratio())
        frame_psnr.append(avgPSNR)
        frame_delay.append(np.mean(allFrameDelay))
        frame_loss.append(np.mean(allFrameLoss))
        vmaf.append(thisvmaf)

        print(f"AllFrameVSnp_recv : {np.mean(allFramePSNR)} v.s. {np.mean(storageTrack[0][3])}")
        print(f"AllFrameVSnp_delay: {np.mean(allFrameDelay)} v.s. {np.mean(storageTrack[0][4])}")
        print(f"AllFrameVSnp_loss : {np.mean(allFrameLoss)} v.s. {np.mean(storageTrack[0][5])}")
        print("this result: ", pkt_recv[-1], pkt_delay[-1], pkt_loss[-1], frame_psnr[-1], frame_delay[-1], frame_loss[-1] )

        f=open(f'tests_trace/{cc}/track/trace{testid}_Pickle','wb')
        pickle.dump({"testid":testid, "plots":[plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, plotTraceT, plotTrace, \
                    plotRecvT, plotRecv, mahiT, mahiRate], "storage":storageTrack, \
                    "QoE_pkt":[QOE_recv[-1], QOE_delay[-1], QOE_loss[-1], QOE_pkt[-1]],\
                    "QoE_frame":[QOE_frameQuality[-1], QOE_frameDelay[-1], QOE_frameDrop[-1], QOE_frame[-1]]    
                        }, f, 0)
        f.close()

        
        port += 1
        if (port == 8049):
            port = 8000
        testid += 1

    print("sampleed nums: ", NumList)
    
    
    #plotAvgTrack(cc, pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss)
    return pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, vmaf, QOE_recv, QOE_delay, QOE_loss, QOE_pkt, QOE_frameQuality, QOE_frameDelay, QOE_frameDrop, QOE_frame




def plotAvg(cc, avg_pkt_recv, avg_pkt_delay, avg_pkt_loss, avg_frame_psnr, avg_frame_delay, avg_frame_loss, figPath):
    
    plt.cla()
    plt.scatter(avg_pkt_delay, avg_pkt_recv, label = f"{cc}_pkt_recv_delay")
    plt.grid()
    plt.savefig(figPath + f"/{cc}_pkt_recv_delay")
    
    plt.cla()
    plt.scatter(avg_pkt_delay, avg_pkt_loss, label = f"{cc}_pkt_loss_delay")
    plt.grid()
    plt.savefig(figPath + f"/{cc}_pkt_loss_delay")
    
    plt.cla()
    plt.scatter(avg_frame_delay, avg_frame_psnr, label = f"{cc}_frame_psnr_delay")
    plt.grid()
    plt.savefig(figPath + f"/{cc}_frame_psnr_delay")
    
    plt.cla()
    plt.scatter(avg_frame_delay, avg_frame_loss, label = f"{cc}_frame_loss_delay")
    plt.grid()
    plt.savefig(figPath + f"/{cc}_frame_loss_delay")


def plotAvgTrack(cc, pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss):
    figPath = f'tests_trace/{cc}/avgPLT/'
    plt.cla()
    plt.plot(range(0, len(pkt_recv)), pkt_recv, label = f"{cc}_pkt_recv")
    plt.grid()
    plt.savefig(figPath + f"{cc}_pkt_recv")
    
    plt.cla()
    plt.plot(range(0, len(pkt_delay)), pkt_delay, label = f"{cc}_pkt_delay")
    plt.grid()
    plt.savefig(figPath + f"{cc}_pkt_delay")

    plt.cla()
    plt.plot(range(0, len(pkt_loss)), pkt_loss, label = f"{cc}_pkt_loss")
    plt.grid()
    plt.savefig(figPath + f"{cc}_pkt_loss")

    plt.cla()
    plt.plot(range(0, len(frame_psnr)), frame_psnr, label = f"{cc}_frame_psnr")
    plt.grid()
    plt.savefig(figPath + f"{cc}_frame_psnr")

    plt.cla()
    plt.plot(range(0, len(frame_delay)), frame_delay, label = f"{cc}_frame_delay")
    plt.grid()
    plt.savefig(figPath + f"{cc}_frame_delay")

    plt.cla()
    plt.plot(range(0, len(frame_loss)), frame_loss, label = f"{cc}_frame_loss")
    plt.grid()
    plt.savefig(figPath + f"{cc}_frame_loss")

def plotEveryTest(pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, path):
    plt.cla()
    plt.plot(range(len(pkt_recv)), pkt_recv, label = f"pkt_recv")
    plt.grid()
    plt.savefig(path + f"/everyTest_pkt_recv")
    
    plt.cla()
    plt.plot(range(len(pkt_delay)), pkt_delay, label = f"pkt_delay")
    plt.grid()
    plt.savefig(path + f"/everyTest_pkt_delay")

    plt.cla()
    plt.plot(range(len(pkt_loss)), pkt_loss, label = f"pkt_loss")
    plt.grid()
    plt.savefig(path + f"/everyTest_pkt_loss")

    plt.cla()
    plt.plot(range(len(frame_psnr)), frame_psnr, label = f"frame_psnr")
    plt.grid()
    plt.savefig(path + f"/everyTest_frame_psnr")

    plt.cla()
    plt.plot(range(len(frame_delay)), frame_delay, label = f"frame_delay")
    plt.grid()
    plt.savefig(path + f"/everyTest_frame_delay")

    plt.cla()
    plt.plot(range(len(frame_loss)), frame_loss, label = f"frame_loss")
    plt.grid()
    plt.savefig(path + f"/everyTest_frame_loss")


def main():
    restart = True
    continueID = 48
    cc = '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s'
    totalNum = len(traceName)
    groups = 1
    for group in range(0, groups):
        pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, vmaf, \
            QOE_recv, QOE_delay, QOE_loss, QOE_pkt, QOE_frameQuality, QOE_frameDelay, QOE_frameDrop, QOE_frame\
                 = testCC(cc, totalNum, restart, continueID)
        avg_pkt_recv = np.mean(pkt_recv)
        avg_pkt_delay = np.mean(pkt_delay)
        avg_pkt_loss = np.mean(pkt_loss)
        avg_frame_psnr = np.mean(frame_psnr)
        avg_frame_delay = np.mean(frame_delay)
        avg_frame_loss = np.mean(frame_loss)
        avg_vmaf = np.mean(vmaf)
        path = f'tests_trace/{cc}/avgPLT/{group}'
        os.system(f"mkdir {path}")

        f=open(path + '/avgPickle','wb')
        pickle.dump([avg_pkt_recv, avg_pkt_delay, avg_pkt_loss, avg_frame_psnr, avg_frame_delay, avg_frame_loss], f, 0)
        f.close()
        plotAvg(cc, avg_pkt_recv, avg_pkt_delay, avg_pkt_loss, avg_frame_psnr, avg_frame_delay, avg_frame_loss, path)
   
        f=open(path + '/everyTestPickle','wb')
        pickle.dump([pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, vmaf, QOE_recv, QOE_delay, QOE_loss, QOE_pkt, QOE_frameQuality, QOE_frameDelay, QOE_frameDrop, QOE_frame], f, 0)
        f.close()
        plotEveryTest(pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, path)


if __name__ == "__main__":
    main()