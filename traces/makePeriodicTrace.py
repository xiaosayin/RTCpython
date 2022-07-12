import random
import time
import os
import matplotlib.pyplot as plt
sudoPW = 1
traceNum = 10
sudoPW = "{sudoPW}"
ifPlot = False
cnt = 0
#interval ms
minT = 5
minT = 5000
maxT = 1000
maxT = 5000
#bw kbit
minRate = 800
maxRate = 1500

#loss % * 1000
minLoss = 0
maxLoss = 20 * 1000
maxLoss = 0

#delay ms
minDelay = 0
maxDelay = 100
maxDelay = 0

#periodic ms
periTime = 10 * 1000

#totalTime ms
totalTime = 100 * 1000

def getT(minT, maxT):
    return random.randint(minT, maxT)
def getR(minRate, maxRate):
    delta = 1000
    cnt = 0
    rate = random.gauss((minRate + maxRate) / 2, delta)
    while rate < minRate or rate > maxRate:
        if cnt < 1000:
            rate = random.gauss((minRate + maxRate) / 2, delta)
        else:
            if rate > maxRate:
                rate = maxRate
            if rate < minRate:
                rate = minRate
        cnt += 1
    return int(rate)
def getL(minLoss, maxLoss):
    cnt = 0
    delta = 60
    loss = random.gauss(minLoss, delta)
    while loss > maxLoss or loss < minLoss:
        if cnt < 1000:
            loss = random.gauss(minLoss, delta)
        else:
            if loss > maxLoss:
                loss = maxLoss
            if loss < minLoss:
                loss = minLoss
        cnt += 1
    return float(int(loss)/ 1000)
def getD(minDelay, maxDelay):
    return random.randint(minDelay, maxDelay)

def addTC(t, rate, loss, delay, cmd, tabs, tracef):
    tabLine = ""
    for i in range(0,tabs):
        tabLine = "\t" + tabLine
    if cmd == "del":
        cmd = f"echo {sudoPW} | sudo -S tc qdisc del dev eno2 root"
        writeLine = tabLine + f"os.system(\"{cmd}\")\n"
        tracef.write(writeLine)
        tracef.write(tabLine + "tracef.close()\n")
        return
    else:
        cmd = f"echo {sudoPW} | sudo -S tc qdisc {cmd} dev eno2 root netem"
        if rate != 0:
            cmd = cmd + f" rate {rate}kbit"
        if loss != 0:
            cmd = cmd + f" loss {loss}% 25%"
        if delay != 0:
            cmd = cmd + f" delay {delay}ms {delay/10}ms distribution normal"
        if t == 0:
            return
        else:
            writeLine = tabLine + f"os.system(f\"{cmd}\")\n"
            tracef.write(writeLine)
            logLine = tabLine + f"tracef.write(f\"{rate} ; " + "{round(time.time() * 1000)}\\n\")\n\ttracef.flush()\n"
            tracef.write(logLine)
            writeLine = tabLine + f"time.sleep({float(t/1000)})\n"
            tracef.write(writeLine)



def makeOneTrace(minT, maxT, minRate, maxRate, minLoss, maxLoss, minDelay, maxDelay, totalTime, traceN):
    tracePath = f"traces/periodic/trace{traceN}.py"
    tracef = open(tracePath, 'w')
    tracef.close()
    tracef = open(tracePath, 'a+')
    tracef.write(f"#t:{minT}-{maxT} ; rate:{minRate}-{maxRate} ; loss_{minLoss}-{maxLoss} ; delay:{minDelay}-{maxDelay}\n")
    tabs = 0
    tracef.write("import os\n")
    tracef.write("import time\n")

    tracef.write("def link(sudoPW):\n")
    tracef.write(f"\ttracef = open(\"traces/periodic/trace{traceN}.txt\", 'w')\n")
    tracef.write(f"\ttracef.close()\n")
    tracef.write(f"\ttracef = open(\"traces/periodic/trace{traceN}.txt\", 'a+')\n")
    tabs += 1
    curT = 0    #currentTime
    periT = 0   #periodicTime
    t = []
    rate = []
    loss = []
    delay = []
    started = 0     #periodic 0-1  eg: _-_-_-_-_-_
    while curT < totalTime:

        addTCI = 0
        started = 0     #periodic 0-1  eg: _-_-_-_-_-_
        while periT < periTime:
            if started == 0:       #periodic 0-1  eg: _-_-_-_-_-_
                t.append(getT(minT, maxT))
                #rate.append(getR(minRate, maxRate))
                rate.append(800)    #periodic 0-1  eg: _-_-_-_-_-_
                loss.append(getL(minLoss, maxLoss))
                delay.append(getD(minDelay, maxDelay))
                if curT == 0:
                    addTC(t[addTCI], rate[addTCI], loss[addTCI], delay[addTCI], "add", tabs, tracef)
                else:
                    addTC(t[addTCI], rate[addTCI], loss[addTCI], delay[addTCI], "change", tabs, tracef)
                periT += t[addTCI]
                curT += t[addTCI]
                addTCI += 1
                started += 1
            else:
                t.append(getT(minT, maxT))
                #rate.append(getR(minRate, maxRate))
                rate.append(1500)    #periodic 0-1  eg: _-_-_-_-_-_
                loss.append(getL(minLoss, maxLoss))
                delay.append(getD(minDelay, maxDelay))
                if curT == 0:
                    addTC(t[addTCI], rate[addTCI], loss[addTCI], delay[addTCI], "add", tabs, tracef)
                else:
                    addTC(t[addTCI], rate[addTCI], loss[addTCI], delay[addTCI], "change", tabs, tracef)
                periT += t[addTCI]
                curT += t[addTCI]
                addTCI += 1
                started += 1
        periT = 0
    addTC(t[addTCI], rate[addTCI], loss[addTCI], delay[addTCI], "change", tabs, tracef)
    addTC(t[addTCI], rate, loss, delay, "del", tabs, tracef)

    tabs -= 1
    tracef.write("def main():\n")
    tabs += 1
    tracef.write("\tlink()\n")
    tabs -= 1
    tracef.write("if __name__ == \"__main__\":\n")
    tabs += 1
    tracef.write("\tmain()")
    tracef.close()

def main():
    os.system("rm periodic/*.py")
    os.system("rm periodic/*.txt")
    statsT = []
    statsR = []
    statsL = []
    statsD = []
    for traceN in range(0,traceNum):
        t = [getT(minT, maxT), getT(minT, maxT)]
        t.sort()
        r = [getT(minRate, maxRate), getT(minRate, maxRate)]
        r.sort()
        l = [getL(minLoss, maxLoss), getL(minLoss, maxLoss)]
        l.sort()
        d = [getD(minDelay, maxDelay), getD(minDelay, maxDelay)]
        d.sort()


        makeOneTrace(t[0], t[1], r[0], r[1], \
                        l[0], l[1], d[0], d[1], \
                        totalTime, traceN)
        statsT.append(float((t[0] + t[1])/2))
        statsR.append(float((r[0] + r[1])/2))
        statsL.append(float((l[0] + l[1])/2))
        statsD.append(float((d[0] + d[1])/2))


    statsT.sort()
    statsR.sort()
    statsL.sort()
    statsD.sort()
    plt.subplot(2, 2, 1)
    plt.plot(range(0, len(statsT)), statsT)
    plt.grid()
    plt.subplot(2, 2, 2)
    plt.plot(range(0, len(statsR)), statsR)
    plt.grid()
    plt.subplot(2, 2, 3)
    plt.plot(range(0, len(statsL)), statsL)
    plt.grid()
    plt.subplot(2, 2, 4)
    plt.plot(range(0, len(statsD)), statsD)
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()






