import matplotlib.pyplot as plt
import pickle
import os

LINEWIDTH = 2
def getTrace(cc, testid):
    tracef = open(f'tests/{cc}/track/trace{testid}_Pickle','rb')
    storageTrace = pickle.load(tracef)
    tracef.close()

    for i in range(len(storageTrace[5])):
        storageTrace[5][i] /= 1000000
    for i in range(len(storageTrace[11])):
        storageTrace[11][i] /= 1000000
    return storageTrace[0], storageTrace[5], storageTrace[6], storageTrace[11], storageTrace[12]

def idExist(testid):
    return os.path.exists(f'tests/gcc/track/trace{testid}_Pickle') and os.path.exists(f'tests/16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s/track/trace{testid}_Pickle')\
            and os.path.exists(f'tests/recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s/track/trace{testid}_Pickle')\
            and os.path.exists(f'tests/16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s/track/trace{testid}_Pickle')

testsPath = 'tests/'
labelMap = {'gcc':'gcc', 'hrcc':'hrcc', \
            'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s':'E3C',\
            '16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s':'pkt+frame',\
            '16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s':'pkt_only'
            }
testCC = ['gcc', 'hrcc', 'recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s']
colorMap = {'gcc':'dodgerblue', 'hrcc':'mediumseagreen', 'E3C':'crimson', 'pkt+frame':'darkorange', 'pkt_only':'gold'}

plt.figure(figsize=(22,7))
#plt.rcParams['figure.figsize']=(12.8, 7.2)

for testid in range(0, 100):
    if not idExist(testid):
        continue

    testid, plotSetT, plotSet, mahiT, mahiRate = getTrace('gcc', testid)
    plt.step(mahiT, mahiRate, alpha = 0.6, label='Bandwidth', color='grey',linewidth=LINEWIDTH)

    testid, plotSetT, plotSet, mahiT, mahiRate = getTrace('recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s', testid)
    plt.plot(plotSetT[:-2], plotSet[:-2], alpha = 0.9, label=labelMap['recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s'], \
            color=colorMap[labelMap['recv+16newPSNR_16delay_6Loss_10frameDelay_BiLinear0711_150_state_400fdg_statePSNRWidth_4video_90s']], linestyle='-',linewidth=LINEWIDTH)

    testid, plotSetT, plotSet, mahiT, mahiRate = getTrace('16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s', testid)
    plt.plot(plotSetT[:-2], plotSet[:-2], alpha = 0.9, label=labelMap['16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s'], \
            color=colorMap[labelMap['16delay_6Loss_10frameDelay_BiLinear0711_300_state_400fdg_90s']], linestyle='--',linewidth=LINEWIDTH)


    testid, plotSetT, plotSet, mahiT, mahiRate = getTrace('16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s', testid)
    plt.plot(plotSetT[:-2], plotSet[:-2], alpha = 0.9, label=labelMap['16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s'], \
            color=colorMap[labelMap['16delay_6Loss_BiLinear0711_150_gamma_08_newstate_90s']], linestyle='-.',linewidth=LINEWIDTH)


    plt.legend(loc=1)
    plt.xlabel("t (s)")
    plt.ylabel("bitrate (bps)")
    plt.grid()
    plt.savefig(f'testResult/ablation/traces/trace{testid}.png')
    plt.cla()