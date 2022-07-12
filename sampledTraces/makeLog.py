import os
import sys
sys.path.append(os.getcwd())
import drawMahiRate
import matplotlib.pyplot as plt
MIN_INTERVAL = 500
def makeLog(tracePath, logPath):
    logf = open(logPath, 'w')
    logf.write("#t:nan-nan ; rate:nan-nan\n")

    base_time = 0
    tracef = open(tracePath, 'r')
    traceLine = tracef.readline()
    while traceLine:
        pktNum = 0
        while (traceLine and int(traceLine) < base_time + MIN_INTERVAL):
            pktNum += 1
            traceLine = tracef.readline()
        if (traceLine):
            logf.write(f"rate: {int(pktNum * 1500 * 8 / (int(traceLine) - base_time))} 	 duration: {int(traceLine) - base_time } \n")
            base_time = int(traceLine)
        



def main():
    
    #file = 'trace-1553453943-ts-walking'
    path = 'sampledTraces/pens_traces90s/'
    ls = os.listdir(path)
    for file in ls:
        if '.log'  not in file and '.png' not in file:
            tracePath = f'{path}{file}'
            logPath = f'{path}{file}.log'
            makeLog(tracePath, logPath)
            mahiRate, mahiT = drawMahiRate.drawMahiTrace(logPath)
            figPath = f'{path}{file}.png'
            plt.cla()
            plt.figure(figsize=(12,7))
            plt.step(mahiT, mahiRate, alpha = 0.6, label='network bandwidth', color='grey')
            #for i in plotRecv:
                #print("plotRecv: ", plotRecv)
            plt.legend(loc=1)
            plt.xlabel("t (us)")
            plt.ylabel("bitrate (bps)")
            plt.grid()
            plt.savefig(figPath)

if __name__ == "__main__":
    main()