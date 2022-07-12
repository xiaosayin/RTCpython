import matplotlib.pyplot as plt
import pickle
import os
import numpy as np
import sys
import math
sys.path.append(os.getcwd())

def cal_QoE_pkt_recv(trace, traceBW):
    return 100 * trace / traceBW / 1000000

def cal_QoE_pkt_delay(trace):
    delay_max = max(trace)
    delay_min = min(trace)
    delay_95th = np.percentile(trace, 95)
    return 100 * (delay_max - delay_95th) / (delay_max - delay_min)

def cal_QoE_pkt_loss(trace):
    print(" trace.calculate_total_loss_ratio()", trace.calculate_total_loss_ratio())
    return 100 * (1 - trace.calculate_total_loss_ratio())

def cal_QoE_frame_psnr(trace):
    minPsnr = 36
    maxPsnr = 42

    return 100 * (math.pow(10, np.mean(trace) / 10) - math.pow(10, minPsnr / 10)) / \
            (math.pow(10, maxPsnr / 10) - math.pow(10, minPsnr / 10))

def cal_QoE_frame_delay(trace):
    delay_max = max(trace)
    delay_min = min(trace)
    delay_95th = np.percentile(trace, 95)

    avgDelay = np.mean(trace)
    return 100 - (avgDelay / 3)
    return 100 * (delay_max - delay_95th) / (delay_max - delay_min)

def cal_QoE_frame_drop(trace):
    return 100 * (1 - np.mean(trace))

def getAllQoE(pktRecv, pktDelay, pktLoss, framePSNR, frameDelay, frameDrop, pktRecord, traceBWE, GROUP, HEAD_TAIL):
    QoE_pkt = []
    QoE_pkt_recv = []
    QoE_pkt_delay = []
    QoE_pkt_loss = []
    QoE_frame = []
    QoE_frame_psnr = []
    QoE_frame_delay = []
    QoE_frame_drop = []

    ccCnt = 0
    groupCnt = 0
    traceCnt = 0
    for cc in pktRecv:
        groupCnt = 0
        QoE_pkt_recv.append([])
        for group in cc:
            QoE_pkt_recv[-1].append([])
            traceCnt = 0
            for trace in group:
                QoE_pkt_recv[-1][-1].append(cal_QoE_pkt_recv(trace, traceBWE[ccCnt][groupCnt][traceCnt]))
                traceCnt += 1
            groupCnt += 1
        ccCnt += 1

    for cc in pktDelay:
        QoE_pkt_delay.append([])
        for group in cc:
            QoE_pkt_delay[-1].append([])
            for trace in group:
                QoE_pkt_delay[-1][-1].append(cal_QoE_pkt_delay(trace))

    for cc in pktRecord:
        QoE_pkt_loss.append([])
        for group in cc:
            QoE_pkt_loss[-1].append([])
            for trace in group:
                QoE_pkt_loss[-1][-1].append(cal_QoE_pkt_loss(trace))

    for cc in framePSNR:
        QoE_frame_psnr.append([])
        for group in cc:
            QoE_frame_psnr[-1].append([])
            for trace in group:
                QoE_frame_psnr[-1][-1].append(cal_QoE_frame_psnr(trace))
            
    for cc in frameDelay:
        QoE_frame_delay.append([])
        for group in cc:
            QoE_frame_delay[-1].append([])
            for trace in group:
                QoE_frame_delay[-1][-1].append(cal_QoE_frame_delay(trace))   

    for cc in frameDrop:
        QoE_frame_drop.append([])
        for group in cc:
            QoE_frame_drop[-1].append([])
            for trace in group:
                QoE_frame_drop[-1][-1].append(cal_QoE_frame_drop(trace))      

   
    QoE_pkt_recv_score = []
    QoE_pkt_delay_score = []
    QoE_pkt_loss_score = []
    QoE_frame_psnr_score = []
    QoE_frame_delay_score = []
    QoE_frame_drop_score = []

    ccNum = len(QoE_pkt_recv)
    for cc in range(ccNum):
        QoE_pkt_recv_score.append([])
        QoE_pkt_delay_score.append([])
        QoE_pkt_loss_score.append([])
        QoE_frame_psnr_score.append([])
        QoE_frame_delay_score.append([])
        QoE_frame_drop_score.append([])
        for group in range(GROUP):
            QoE_pkt_recv_score[-1].append(np.mean(sorted(QoE_pkt_recv[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))
            QoE_pkt_delay_score[-1].append(np.mean(sorted(QoE_pkt_delay[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))
            QoE_pkt_loss_score[-1].append(np.mean(sorted(QoE_pkt_loss[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))
            QoE_frame_psnr_score[-1].append(np.mean(sorted(QoE_frame_psnr[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))
            QoE_frame_delay_score[-1].append(np.mean(sorted(QoE_frame_delay[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))
            QoE_frame_drop_score[-1].append(np.mean(sorted(QoE_frame_drop[cc][group])[HEAD_TAIL:0-HEAD_TAIL]))

        
    for cc in range(ccNum):
        QoE_pkt.append([])
        QoE_frame.append([])
        for group in range(GROUP):
            QoE_pkt[cc].append([])
            QoE_frame[cc].append([])
            traceNum = len(QoE_pkt_delay[cc][group])
            for trace in range(traceNum):
                QoE_pkt[cc][group].append(0.2 * QoE_pkt_recv[cc][group][trace] + \
                                            0.2 * QoE_pkt_delay[cc][group][trace] + \
                                                0.3 * QoE_pkt_loss[cc][group][trace])
                QoE_frame[cc][group].append(0.2 * QoE_frame_psnr[cc][group][trace] + \
                                            0.2 * QoE_frame_delay[cc][group][trace] + \
                                                0.3 * QoE_frame_drop[cc][group][trace])


    for cc in range(ccNum):
        for group in range(GROUP):
            QoE_pkt[cc][group] = sorted(QoE_pkt[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_frame[cc][group] = sorted(QoE_frame[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_pkt_recv[cc][group] = sorted(QoE_pkt_recv[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_pkt_delay[cc][group] = sorted(QoE_pkt_delay[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_pkt_loss[cc][group] = sorted(QoE_pkt_loss[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_frame_psnr[cc][group] = sorted(QoE_frame_psnr[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_frame_delay[cc][group] = sorted(QoE_frame_delay[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
            QoE_frame_drop[cc][group] = sorted(QoE_frame_drop[cc][group])[HEAD_TAIL:0-HEAD_TAIL]
    print("QoE_pkt", QoE_pkt)
    print("QoE_frame", QoE_frame)
    print("QoE_pkt_recv", QoE_pkt_recv)
    


    return QoE_pkt, QoE_pkt_recv, QoE_pkt_delay, QoE_pkt_loss, \
        QoE_frame, QoE_frame_psnr, QoE_frame_delay, QoE_frame_drop

#from HRCC.packet_record import PacketRecord
testsPath = 'tests_trace/'
ls = os.listdir(testsPath)

FOLDLIST = [
        'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s',
        #'16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s',
        #'16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s',
        'gcc', 
        'hrcc'
        ]

nameMap = {'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s':'CLCC',
        'gcc':'GCC',
        'hrcc':'HRCC'
        
        }
colorMap = {'GCC':'dodgerblue', 'HRCC':'mediumseagreen', 'CLCC':'crimson'}
DOT_SIZE = 70
STAR_SIZE = 100
DOT_ALPHA = 0.5
STAR_ALPHA = 1
HEAD_TAIL = 10
GROUP = 1

name = []
vmaf = []
frame_psnr = []
QOE_pkt = []
QOE_frame = []

for fold in ls:
    if '.py' not in fold \
        and 'copy' not in fold \
        and (fold in FOLDLIST):
        name.append(nameMap[fold])
        vmaf.append([])
        frame_psnr.append([])
        QOE_pkt.append([])
        QOE_frame.append([])
        for group in range(0, GROUP):
            avgf = open(testsPath + fold + f'/avgPLT/{group}/everyTestPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            vmaf[-1].append(storageAvg[6])

            avgf = open(testsPath + fold + f'/avgPLT/{group}/avgPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            frame_psnr[-1].append(storageAvg[3])

name = []
pktRecv = []    #[gcc:[group:[tyrace: [], []], [], []]]
pktDelay = []
pktLoss = []
framePSNR = []
frameDelay = []
frameDrop = []
pktRecord = []
traceBWE = []

for fold in ls:
    if '.py' not in fold \
        and 'copy' not in fold \
        and (fold in FOLDLIST):
        name.append(nameMap[fold])
        pktRecv.append([])  #add cc
        pktDelay.append([])
        pktLoss.append([])
        framePSNR.append([])
        frameDelay.append([])
        frameDrop.append([])
        pktRecord.append([])
        traceBWE.append([])

        for group in range(0, GROUP):
            pktRecv[-1].append([])  #add group
            pktDelay[-1].append([])
            pktLoss[-1].append([])
            framePSNR[-1].append([])
            frameDelay[-1].append([])
            frameDrop[-1].append([])
            pktRecord[-1].append([])
            traceBWE[-1].append([])
            EveryTracef = open(testsPath + fold + f'/avgPLT/{group}/detailedEveryTrace', 'rb')
            detailedEveryTrace = pickle.load(EveryTracef)
            EveryTracef.close()
            for trace in detailedEveryTrace:
                pktRecv[-1][-1].append(trace[0])
                pktDelay[-1][-1].append(trace[1])
                pktLoss[-1][-1].append(trace[2])
                pktRecord[-1][-1].append(trace[3])
                framePSNR[-1][-1].append(trace[4])
                frameDelay[-1][-1].append(trace[5])
                frameDrop[-1][-1].append(trace[6])
                traceBWE[-1][-1].append(trace[7])
  



QoE_pkt, QoE_pkt_recv, QoE_pkt_delay, QoE_pkt_loss, QoE_frame, QoE_frame_psnr, QoE_frame_delay, QoE_frame_drop\
    = getAllQoE(pktRecv, pktDelay, pktLoss, framePSNR, frameDelay, frameDrop, pktRecord, traceBWE, GROUP, HEAD_TAIL)



#[pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, vmaf, QOE_recv, QOE_delay, QOE_loss, QOE_pkt, QOE_frameQuality, QOE_frameDelay, QOE_frameDrop, QOE_frame]
figPath = f'testResult_trace/'
'''
print("QoE_pkt_recv, ", QoE_pkt_recv)
print("QoE_pkt_delay, ", QoE_pkt_delay)
print("QoE_pkt_loss, ", QoE_pkt_loss)
print("QoE_frame_psnr, ", QoE_frame_psnr)
print("QoE_frame_delay, ", QoE_frame_delay)
print("QoE_frame_drop, ", QoE_frame_drop)
'''


print("name: ", name)
plt.cla()
plt.figure(figsize=(6,3))
plt.bar([0, 1], [0, 1], tick_label=['QoE_pkt', 'QoE_frame'], width=0)
xbase = 0
x = np.arange(xbase,2)
bar_width = 1 / 2 / len(name)
for i in range(0, len(name)):
    plt.bar(x, [np.mean(QoE_pkt[i][0]), np.mean(QoE_frame[i][0])], width=bar_width, yerr=[np.std(QoE_pkt[i][0],ddof=1), np.std(QoE_frame[i][0],ddof=1)], error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,2)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoE.pdf")

plt.cla()
plt.bar(range(0, 3), range(0, 3), tick_label=['QoE_pkt_recv', 'QoE_pkt_delay', 'QoE_pkt_loss'], width=0)
xbase = 0
x = np.arange(xbase,3)
bar_width = 1 / 2 / len(name)
for i in range(0, len(name)):
    plt.bar(x, [np.mean(QoE_pkt_recv[i][0]), np.mean(QoE_pkt_delay[i][0]), np.mean(QoE_pkt_loss[i][0])], \
            width=bar_width, yerr=[np.std(QoE_pkt_recv[i][0],ddof=1), np.std(QoE_pkt_delay[i][0],ddof=1), np.std(QoE_pkt_loss[i][0],ddof=1)], \
            error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,3)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoEs_packet.pdf")

plt.cla()
plt.bar(range(0, 3), range(0, 3), tick_label=['QoE_frame_quality', 'QoE_frame_delay', 'QoE_frame_drop'], width=0)
xbase = 0
x = np.arange(xbase,3)
bar_width = 1 / 2 / len(name)


for i in range(0, len(name)):
    
    print(f"{name[i]}_psnr: ", np.mean(QoE_frame_psnr[i][0]))
    print(f"{name[i]}_drop: ", np.mean(QoE_frame_drop[i][0]))
    plt.bar(x, [np.mean(QoE_frame_psnr[i][0]), np.mean(QoE_frame_delay[i][0]), np.mean(QoE_frame_drop[i][0])], \
            width=bar_width, yerr=[np.std(QoE_frame_psnr[i][0],ddof=1), np.std(QoE_frame_delay[i][0],ddof=1), np.std(QoE_frame_drop[i][0],ddof=1)], \
            error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,3)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoEs_frame.pdf")

'''
plt.cla()
for i in range(0, len(name)):
    plt.scatter(vmaf[i], frame_psnr[i], label = name[i], c = colorMap[name[i]], s = DOT_SIZE)
    plt.scatter(np.mean(vmaf[i]), np.mean(frame_psnr[i]), marker = '*', color = colorMap[name[i]], s = STAR_SIZE)

plt.grid()
plt.legend(loc=3)
plt.xlabel("vmaf")
plt.ylabel("psnr")
plt.savefig(figPath + f"vmaf_psnr.png")
'''