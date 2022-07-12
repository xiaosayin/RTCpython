import matplotlib.pyplot as plt
import pickle
import os
import numpy as np

testsPath = 'tests/'
ls = os.listdir(testsPath)

name = []
pkt_recv = []
pkt_delay = []
pkt_loss = []
frame_psnr = []
frame_delay = []
frame_loss = []
for fold in ls:
    if '.py' not in fold \
        and 'copy' not in fold \
        and ('recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s without detailed' == fold
            
            #or '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s' == fold
            #or '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s' == fold
            or 'gcc without detailed' == fold
            or 'hrcc without detailed' == fold
            ):
        if fold == 'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s without detailed':
            name.append('CLCC')
        elif fold == 'gcc without detailed':
            name.append('GCC')
        elif fold == 'hrcc without detailed':
            name.append('HRCC')
        pkt_recv.append([])
        pkt_delay.append([])
        pkt_loss.append([])
        frame_psnr.append([])
        frame_delay.append([])
        frame_loss.append([])
        for group in range(0, 5):
            avgf = open(testsPath + fold + f'/avgPLT/{group}/avgPickle', 'rb')
            storageAvg = pickle.load(avgf)
            avgf.close()
            
            pkt_recv[-1].append(storageAvg[0] / 1000000)
            pkt_delay[-1].append(storageAvg[1])
            pkt_loss[-1].append(storageAvg[2] * 100)
            frame_psnr[-1].append(storageAvg[3])
            frame_delay[-1].append(storageAvg[4])
            frame_loss[-1].append(storageAvg[5] * 100)
colorMap = {'GCC':'dodgerblue', 'HRCC':'mediumseagreen', 'CLCC':'crimson'}
markerMap = {'GCC':'o', 'HRCC':'D', 'CLCC':'^'}
avgMarkerMap = {'GCC':'o', 'HRCC':'D', 'CLCC':'^'}
markerMap = {'GCC':'.', 'HRCC':'.', 'CLCC':'.'}
avgMarkerMap = {'GCC':'*', 'HRCC':'*', 'CLCC':'*'}
DOT_SIZE = 200
STAR_SIZE = 250
DOT_ALPHA = 0.5
STAR_ALPHA = 1
figPath = f'testResult/'
plt.cla()
plt.figure(figsize=(6,4))
for i in range(0, len(name)):
    c = colorMap[name[i]]   
    plt.scatter(pkt_delay[i], pkt_recv[i], label = name[i], color = c, marker = markerMap[name[i]], s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(pkt_delay[i]), np.mean(pkt_recv[i]) , marker = avgMarkerMap[name[i]], color = c, s = STAR_SIZE, alpha = STAR_ALPHA)
    print(f"{name[i]} recv rate: {np.mean(pkt_recv[i])}")
    print(f"{name[i]} pkt delay: {np.mean(pkt_delay[i])}")
plt.grid()
plt.legend(loc=1)
plt.xlabel("Packet Delay (ms)")
plt.ylabel("Receiving Rate (Mbps)")
plt.gca().invert_xaxis()
plt.savefig(figPath + f"pkt_recv_delay.pdf")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]      
    plt.scatter(pkt_delay[i], pkt_loss[i], label = name[i], color = c, marker = markerMap[name[i]], s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(pkt_delay[i]), np.mean(pkt_loss[i]), marker = avgMarkerMap[name[i]], color = c, s = STAR_SIZE, alpha = STAR_ALPHA)
    print(f"{name[i]} pkt loss: {np.mean(pkt_loss[i])}")
plt.grid()
plt.legend(loc=2)
plt.xlabel("Packet Delay (ms)")
plt.ylabel("Packet Loss Rate (%)")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig(figPath + f"pkt_loss_delay.pdf")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]      
    plt.scatter(frame_delay[i], frame_psnr[i], label = name[i], color = c, marker = markerMap[name[i]], s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(frame_delay[i]), np.mean(frame_psnr[i]), marker = avgMarkerMap[name[i]], color = c, s = STAR_SIZE, alpha = STAR_ALPHA)
    print(f"{name[i]} frame_psnr: {np.mean(frame_psnr[i])}")
plt.grid()
plt.legend(loc=2)
plt.xlabel("Frame Delay (ms)")
plt.ylabel("Frame PSNR (dB)")
plt.gca().invert_xaxis()
plt.savefig(figPath + f"frame_psnr_delay.pdf")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]    
    plt.scatter(frame_delay[i], frame_loss[i], label = name[i], color = c, marker = markerMap[name[i]], s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(frame_delay[i]), np.mean(frame_loss[i]), marker = avgMarkerMap[name[i]], color = c, s = STAR_SIZE, alpha = STAR_ALPHA)
    print(f"{name[i]} frame_delay: {np.mean(frame_delay[i])}")
    print(f"{name[i]} frame_loss: {np.mean(frame_loss[i])}")
plt.grid()
plt.legend(loc=2)
plt.xlabel("Frame Delay (ms)")
plt.ylabel("Frame Drop Rate (%)")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig(figPath + f"frame_loss_delay.pdf")

