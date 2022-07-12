import matplotlib.pyplot as plt
from testResult.drawCompeteTrace import LINEWIDTH

def drawMahiTrace(logFile):
    ratef = open(logFile, 'r')
    rateLine = ratef.readline()
    rate = [0]
    time = [0]
    curTime = 0
    while rateLine:
        if "rate: " in rateLine:
            rate.append(int(rateLine[len("rate: ") : rateLine.index(" 	 duration: ")]) * 1000)
            time.append(curTime + int(rateLine[rateLine.index(" 	 duration: ") + len(" 	 duration: ") : ]) * 1000)
            curTime += int(rateLine[rateLine.index(" 	 duration: ") + len(" 	 duration: ") : ]) * 1000
        rateLine = ratef.readline()
    return rate, time

def main():
    file = "mahiTraces/random/trace0.log"
    rate, time = drawMahiTrace(file)
    i = 0
    while i < len(rate):
        print(rate[i], time[i], flush=True)
        i += 1
    plt.figure(figsize=(12,5))

    plt.step(time, rate, alpha = 1, label='network bandwidth', color='blue')
    plt.grid()
    #plt.ylim(0, 4000000)
    #plt.tick_params(labelsize=15)
    plt.legend(loc=1)
    plt.xlabel("t (us)")
    plt.ylabel("bitrate (bps)")
    plt.grid()


    plt.savefig('tmp/drawMahiRate.png')

if __name__ == "__main__":
    main()
