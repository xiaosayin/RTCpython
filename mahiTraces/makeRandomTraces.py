import random
import matplotlib.pyplot as plt
# from pydantic import NoneIsAllowedError
import sampleRandom as sR
import os
traceNum = 500
MTU_SIZE = 1500 * 8         # bit

MAX_RATE = 2000     # kbps
MIN_RATE =  250     # kbps

MIN_DURATION = 250      # ms
MAX_DURATION = 1000      # ms

TOTAL_TIME = 100*1000   # ms

def makeIntervalTrace(targetRate, interval):
    time = 0    #current time
    d = None    #each pkt sent time
    mtuNum = 0  #total pkt Num
    currentRate = 1000000000
    intervalList = []
    rates = []
    times = []
    while time < interval:  #while this interval is not ended
        if d == None:
            d = 1
        else:
            d = 0
        if currentRate > targetRate:    #if rate is too large
            while MTU_SIZE * (mtuNum + 1) / (time + d) > targetRate:    #tune the rate smaller
                d += 1
            intervalList.append(time + d)
            mtuNum += 1
            currentRate = MTU_SIZE * mtuNum / (time + d)
            time += d
        elif currentRate <= targetRate:     #if rate is too small
            while MTU_SIZE * (mtuNum + 1) / (time + d) >= targetRate:    #tune the rate larger
                d += 1
            intervalList.append(time + max(d - 1, 0))
            mtuNum += 1
            currentRate = MTU_SIZE * mtuNum / (time + max(d - 1, 0))
            time += d
        rates.append(currentRate)
        times.append(time)

    return intervalList, rates, times




def makeOneTrace(minT, maxT, minRate, maxRate, path, logPath, pngPath):
    fp = open(logPath, "w")
    fp.close()
    fp = open(logPath, "a+")
    fp.write(f"#t:{minT}-{maxT} ; rate:{minRate}-{maxRate}\n")


    tracef = open(path, "w")
    tracef.close()
    tracef = open(path, 'a+')
    now_time = 0
    rate_t = []
    time_t = []
    while(now_time < TOTAL_TIME):
        random_rate = sR.getR(minRate, maxRate, 1000)
        random_duration = sR.getT(minT, maxT)
        intervalList, rates, times = makeIntervalTrace(random_rate, random_duration)
        for i in intervalList:
            tracef.write(str(i + now_time)+'\n')

        fp.write("rate: %d \t duration: %d \n" %(random_rate, intervalList[-1]))



        now_time = now_time + intervalList[-1]
        rate_t.append(random_rate/1000)
        time_t.append(now_time/1000)

    fp.close()
    plt.cla()
    plt.figure(figsize=(12,5))
    plt.step(time_t, rate_t)
    plt.grid()
    plt.ylim(0, MAX_RATE/1000)
    plt.ylabel("rate/kbps", fontsize=16)
    plt.xlabel("time/s", fontsize=16)
    plt.tick_params(labelsize=15)
    plt.savefig(pngPath,dpi=300)



def main():
    d, rates, times = makeIntervalTrace(1689, 400)
    for i in d:
        print("makeIntervalTrace ", i, flush=True)
    for i in rates:
        print("rates ", i, flush=True)
    plt.cla()
    plt.plot(times, rates)
    plt.plot([times[0], times[-1]], [1689, 1689])
    plt.grid()
    #plt.savefig('makeRandomTrace.png')
    
    os.system("rm mahiTraces/random/*")
    for traceN in range(0,traceNum):
        t = [sR.getT(MIN_DURATION, MAX_DURATION), sR.getT(MIN_DURATION, MAX_DURATION)]
        t.sort()
        r = [sR.getR(MIN_RATE, MAX_RATE, 5000), sR.getR(MIN_RATE, MAX_RATE, 5000)]
        r.sort()
        tracePath = f"mahiTraces/random_2M/trace{traceN}.trace"
        logPath = f"mahiTraces/random_2M/trace{traceN}.log"
        pngPath = f"mahiTraces/random_2M/trace{traceN}.png"
        makeOneTrace(t[0], t[1], r[0], r[1], tracePath, logPath, pngPath)
        #makeOneTrace(MIN_DURATION, MAX_DURATION, MIN_RATE, MAX_RATE, tracePath, logPath, pngPath)

if __name__ == "__main__":
    main()