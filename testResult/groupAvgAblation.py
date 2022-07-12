import matplotlib.pyplot as plt
import pickle
import os
import numpy as np

testsPath = 'tests/'
ls = os.listdir(testsPath)

colorMap = {'gcc':'dodgerblue', 'hrcc':'mediumseagreen', 'E3C':'crimson', 'pkt+frame':'darkorange', 'pkt_only':'gold'}
labelMap = {'gcc':'gcc', 'hrcc':'hrcc', \
            'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s':'E3C',\
            '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s':'pkt+frame',\
            '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s':'pkt_only'
            }

DOT_SIZE = 70
STAR_SIZE = 100
DOT_ALPHA = 0.5
STAR_ALPHA = 1
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
        and ('recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s' == fold
            
            or '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s' == fold
            or '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s' == fold
            or 'gcc' == fold
            #or 'hrcc' == fold
            ):
        name.append(labelMap[fold])
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
            
            pkt_recv[-1].append(storageAvg[0])
            pkt_delay[-1].append(storageAvg[1])
            pkt_loss[-1].append(storageAvg[2] * 100)
            frame_psnr[-1].append(storageAvg[3])
            frame_delay[-1].append(storageAvg[4])
            frame_loss[-1].append(storageAvg[5] * 100)
        

figPath = f'testResult/ablation/'
plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]   
    plt.scatter(pkt_delay[i], pkt_recv[i], label = name[i], color = c, s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(pkt_delay[i]), np.mean(pkt_recv[i]), marker = '*', color = c, s = STAR_SIZE)
plt.grid()
plt.legend(loc=2)
plt.xlabel("Packet Delay (ms)")
plt.ylabel("Receiving Rate (bps)")
plt.gca().invert_xaxis()
plt.savefig(figPath + f"pkt_recv_delay")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]      
    plt.scatter(pkt_delay[i], pkt_loss[i], label = name[i], color = c, s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(pkt_delay[i]), np.mean(pkt_loss[i]), marker = '*', color = c, s = STAR_SIZE)
plt.grid()
plt.legend(loc=2)
plt.xlabel("Packet Delay (ms)")
plt.ylabel("Packet Loss Rate (%)")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig(figPath + f"pkt_loss_delay")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]      
    plt.scatter(frame_delay[i], frame_psnr[i], label = name[i], color = c, s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(frame_delay[i]), np.mean(frame_psnr[i]), marker = '*', color = c, s = STAR_SIZE)
plt.grid()
plt.legend(loc=3)
plt.xlabel("Frame Delay (ms)")
plt.ylabel("PSNR")
plt.gca().invert_xaxis()
plt.savefig(figPath + f"frame_psnr_delay")

plt.cla()
for i in range(0, len(name)):
    c = colorMap[name[i]]    
    plt.scatter(frame_delay[i], frame_loss[i], label = name[i], color = c, s = DOT_SIZE, alpha = DOT_ALPHA)
    plt.scatter(np.mean(frame_delay[i]), np.mean(frame_loss[i]), marker = '*', color = c, s = STAR_SIZE)
plt.grid()
plt.legend(loc=2)
plt.xlabel("Frame Delay (ms)")
plt.ylabel("Frame Drop Rate (%)")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig(figPath + f"frame_loss_delay")

