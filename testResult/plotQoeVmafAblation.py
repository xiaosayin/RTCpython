import matplotlib.pyplot as plt
import pickle
import os
import numpy as np

testsPath = 'tests/'
ls = os.listdir(testsPath)

name = []
vmaf = []
frame_psnr = []
QOE_pkt = []
QOE_frame = []
FOLDLIST = [
        'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s',
        '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s',
        '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s',
        'gcc']

nameMap = {'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s':'E3C',
        'gcc':'gcc',
        'hrcc':'hrcc',
        '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s':'pkt_frame',
        '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s':'pkt'
        }
colorMap = {'gcc':'dodgerblue', 'hrcc':'mediumseagreen', 'E3C':'crimson', 'pkt_frame':'darkorange', 'pkt':'gold'}

DOT_SIZE = 70
STAR_SIZE = 100
DOT_ALPHA = 0.5
STAR_ALPHA = 1
HEAD_TAIL = 3
GROUP = 5
for fold in ls:
    if '.py' not in fold \
        and 'copy' not in fold \
        and (fold in FOLDLIST):
        name.append(nameMap[fold])
        vmaf.append([])
        frame_psnr.append([])
        QOE_pkt.append([])
        QOE_frame.append([])
        print(fold)
        for group in range(0, GROUP):
            avgf = open(testsPath + fold + f'/avgPLT/{group}/everyTestPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            vmaf[-1].append(np.mean(sorted(storageAvg[6])[HEAD_TAIL:0-HEAD_TAIL]))
            QOE_pkt[-1] += storageAvg[10]
            QOE_frame[-1] += storageAvg[14]

            avgf = open(testsPath + fold + f'/avgPLT/{group}/avgPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            frame_psnr[-1].append(storageAvg[3])

name = []
QOE_pktRecv = []
QOE_pktDelay = []
QOE_pktLoss = []
QOE_framePSNR = []
QOE_frameDelay = []
QOE_frameDrop = []


for fold in ls:
    if '.py' not in fold \
        and 'copy' not in fold \
        and (fold in FOLDLIST):
        name.append(nameMap[fold])
        frame_psnr.append([])
        QOE_pktRecv.append([])
        QOE_pktDelay.append([])
        QOE_pktLoss.append([])
        QOE_framePSNR.append([])
        QOE_frameDelay.append([])
        QOE_frameDrop.append([])

        for group in range(0, GROUP):
            avgf = open(testsPath + fold + f'/avgPLT/{group}/everyTestPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            QOE_pktRecv[-1] += storageAvg[7]
            QOE_pktDelay[-1] += storageAvg[8]
            QOE_pktLoss[-1] += storageAvg[9]
            QOE_framePSNR[-1] += storageAvg[11]
            QOE_frameDelay[-1] += storageAvg[12]
            QOE_frameDrop[-1] += storageAvg[13]

            


#[pkt_recv, pkt_delay, pkt_loss, frame_psnr, frame_delay, frame_loss, vmaf, QOE_recv, QOE_delay, QOE_loss, QOE_pkt, QOE_frameQuality, QOE_frameDelay, QOE_frameDrop, QOE_frame]
figPath = f'testResult/ablation/'
print(name)


plt.cla()
plt.bar([0, 1], [0, 1], tick_label=['QoE_pkt', 'QoE_frame'], width=0)
xbase = 0
x = np.arange(xbase,2)
bar_width = 1 / 2 / len(name)
for i in range(0, len(name)):
    plt.bar(x, [np.mean(sorted(QOE_pkt[i])[HEAD_TAIL:0-HEAD_TAIL]), np.mean(sorted(QOE_frame[i])[HEAD_TAIL:0-HEAD_TAIL])], width=bar_width, yerr=[np.std(QOE_pkt[i],ddof=1), np.std(QOE_frame[i],ddof=1)], error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,2)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoE.png")

plt.cla()
plt.bar(range(0, 3), range(0, 3), tick_label=['QoE_pkt_recv', 'QoE_pkt_delay', 'QoE_pkt_loss'], width=0)
xbase = 0
x = np.arange(xbase,3)
bar_width = 1 / 2 / len(name)
for i in range(0, len(name)):
    plt.bar(x, [np.mean(sorted(QOE_pktRecv[i])[HEAD_TAIL:0-HEAD_TAIL]), np.mean(sorted(QOE_pktDelay[i])[HEAD_TAIL:0-HEAD_TAIL]), np.mean(sorted(QOE_pktLoss[i])[HEAD_TAIL:0-HEAD_TAIL])], \
            width=bar_width, yerr=[np.std(sorted(QOE_pktRecv[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1), np.std(sorted(QOE_pktDelay[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1), np.std(sorted(QOE_pktLoss[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1)], \
            error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,3)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoEs_packet.png")

plt.cla()
plt.bar(range(0, 3), range(0, 3), tick_label=['QoE_frame_quality', 'QoE_frame_delay', 'QoE_frame_drop'], width=0)
xbase = 0
x = np.arange(xbase,3)
bar_width = 1 / 2 / len(name)
for i in range(0, len(name)):
    plt.bar(x, [np.mean(sorted(QOE_framePSNR[i])[HEAD_TAIL:0-HEAD_TAIL]), np.mean(sorted(QOE_frameDelay[i])[HEAD_TAIL:0-HEAD_TAIL]), np.mean(sorted(QOE_frameDrop[i])[HEAD_TAIL:0-HEAD_TAIL])], \
            width=bar_width, yerr=[np.std(sorted(QOE_framePSNR[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1), np.std(sorted(QOE_frameDelay[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1), np.std(sorted(QOE_frameDrop[i])[HEAD_TAIL:0-HEAD_TAIL],ddof=1)], \
            error_kw = {'ecolor' : '0.2', 'capsize' :2 }, label=name[i][0:5], color=colorMap[name[i]])
    xbase += bar_width
    x = np.arange(xbase ,3)
plt.legend(loc=4)
plt.grid()
plt.savefig(figPath + f"QoEs_frame.png")


plt.cla()
for i in range(0, len(name)):
    plt.scatter(vmaf[i], frame_psnr[i], label = name[i], c = colorMap[name[i]], s = DOT_SIZE)
    plt.scatter(np.mean(vmaf[i]), np.mean(frame_psnr[i]), marker = '*', color = colorMap[name[i]], s = STAR_SIZE)

plt.grid()
plt.legend(loc=3)
plt.xlabel("vmaf")
plt.ylabel("psnr")
plt.savefig(figPath + f"vmaf_psnr.png")

