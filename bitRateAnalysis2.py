import os
import matplotlib.pyplot as plt
import drawMahiRate

def getTime(line, log):
    return int(line[line.index(log) + len(log): ])

def makeCutString(lostFrame):
    string = ""
    for i in lostFrame:
        if string == "":
            string += f"eq(n\, {i-1})"
        else:
            string += f" + eq(n\, {i-1})"
    string = "not(" + string + ")"
    return string

def drawMAHItrace():
    mahif = open('6mbps.trace', 'r')
    mahiLine = mahif.readline()
    totalTime = 50 * 1000

    # readin mahi trace
    trace = []
    while mahiLine:
        trace.append(int(mahiLine))
        mahiLine = mahif.readline()

    # pad to full time
    tmpTrace = trace
    while tmpTrace[-1] < totalTime:
        end = tmpTrace[-1]
        padTrace = []
        for i in trace:
            padTrace.append(i + end)
        tmpTrace = tmpTrace + padTrace

    #get the trace
    trace = tmpTrace
    mahiRate = []
    mahiT = []
    lastT = None
    i = 0
    while i < len(trace):
        pktNum = 0
        thisT = trace[i]
        if lastT != None:
            i += 1
            while i < len(trace) and trace[i] == thisT:
                pktNum += 1
                i += 1

            thisT = trace[i-1]
            mahiRate.append((pktNum + 1) * 1500 * 8 * 1000 / (thisT - lastT))
            mahiT.append(thisT * 1000)

        else:
            mahiRate.append((pktNum + 1) * 1500 * 8 * 1000 / thisT)
            mahiT.append(thisT * 1000)
            i += 1
        lastT = thisT

    i = 0
    while i < len(mahiRate):
        #print(mahiRate[i], mahiT[i])
        i += 1

    return mahiRate, mahiT

def getPLTlist(traceType, traceNum):
    sendf = open("./log/send.txt")
    sendLine = sendf.readline()
    vp8SetLog = "YINWENPEI: vp8 setRate kbps: "
    gotFrameLog = "YINWENPEI: got frame ID:"
    # dropOnFrameLog = "KOYONYONG: Drop frame in order to respect frame rate constraint"
    dropOnFrameLog = "YINWENPEI: Drop frame in order to respect frame rate constraint"
    # onFrameLog = "KOYONYONG: OnFRAME"
    encodeSizeLog = "YINWENPEI: send encoded_image"
    #nothingLog = "KOYONYONG: NOTHING1111 "
    nothingLog = "YINWENPEI: NOTHING1111"
    encoderDropLog = "YINWENPEIDROP"
    NTPDropLog = "Same/old NTP timestamp"

    timeLog = " atTime: "

    ## ========================================
    # Read in vp8Rates and encodeRates
    encodeRates = []
    encodeBytes = []
    gotFrameT = []
    gotFrameIndex = 0
    vp8Rates = []

    while sendLine:
        if vp8SetLog in sendLine:
            targetRate = int(sendLine[len(vp8SetLog) : sendLine.index(timeLog)]) * 1000
            targetTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            # targetTime = int(int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])) / 1000 % 1000000 
            vp8Rates.append([targetRate, targetTime])
        sendLine = sendf.readline()

    # debug info vp8Rates present normal
    print("vp8Rates",vp8Rates)

    sendf.seek(0)
    sendLine = sendf.readline()
    while sendLine:
        if gotFrameLog in sendLine:
            # gotT = int((getTime(sendLine, timeLog) / 1000)) % 1000000
            gotT = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            gotFrameT.append(gotT)

        if dropOnFrameLog in sendLine:
            encodeTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            encodeBytes.append(["DROP", gotFrameT[gotFrameIndex]])
            gotFrameIndex += 1

        if encodeSizeLog in sendLine:
            encodeByte = int(sendLine[sendLine.index("size") + 5:sendLine.index("at") - 2])
            encodeTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            encodeBytes.append([encodeByte, gotFrameT[gotFrameIndex]])
            gotFrameIndex += 1

        if nothingLog in sendLine:
            encodeTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            encodeBytes.append(["DROP", gotFrameT[gotFrameIndex]])
            gotFrameIndex += 1

        if encoderDropLog in sendLine or NTPDropLog in sendLine:
            # encodeTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            encodeBytes.append(["DROP", gotFrameT[gotFrameIndex]])
            gotFrameIndex += 1

        sendLine = sendf.readline()
    
    print("=================================\n")
    print("encodeBytes:", encodeBytes)


    setLog = "YINWENPEI: setTargetRate:"

    sendf.seek(0)
    sendLine = sendf.readline()
    setRates = []
    while sendLine:
        if setLog in sendLine:
            setRate = int(sendLine[sendLine.index(setLog) + len(setLog): sendLine.index(timeLog)])
            setTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            # setTime = int((getTime(sendLine, timeLog) / 1000)) % 1000000
            setRates.append([setRate, setTime])
        sendLine = sendf.readline()
    
    print("=================================\n")
    print("setRates:", setRates)


    sendf.seek(0)
    sendLine = sendf.readline()
    setCnt = 0
    while sendLine:
        if setLog in sendLine:
            setTime = int(sendLine[(sendLine.index(timeLog) + len(timeLog)): ])
            setCnt += 1
            if setCnt == 1:
                break
        sendLine = sendf.readline()

    # deltaT = 0
    # tracef = open("traces/periodic/trace1.txt", 'r')
    # traceLine = tracef.readline()
    # trace = []
    # lastTrace = 0
    # lastTime = 0
    # #print("setTime:", setTime)
    # while traceLine:
    #     thisTrace = float(traceLine[0:traceLine.index(" ; ")])
    #     thisTime = float(traceLine[traceLine.index(" ; ") + len(" ; ") : ]) * 1000
    #     if deltaT == 0:
    #         deltaT = 0
    #     if lastTime != 0:
    #         trace.append([lastTrace, thisTime + deltaT])
    #     trace.append([thisTrace, thisTime + deltaT])

    #     lastTrace = thisTrace
    #     lastTime = thisTime + deltaT
    #     traceLine = tracef.readline()
    
    sendLine = sendf.readline()

    ## ========================================
    # Sort by Time
    vp8Rates.sort(key=lambda x:x[1])
    encodeBytes.sort(key=lambda x:x[1])

    targetIndex = 0
    encodeIndex = 0
    allStartT = min(encodeBytes[0][1], vp8Rates[0][1], setRates[0][1])
    #print("1", encodeBytes)
    #print("2", vp8Rates)
    #print("3", setRates)
    #print("4", trace)
    # if trace == []:
    #     allStartT = min(encodeBytes[0][1], vp8Rates[0][1], setRates[0][1])
    # else:
    #     allStartT = min(encodeBytes[0][1], vp8Rates[0][1], setRates[0][1])
    ## ========================================
    # Calculate encodeRate
    bytes = 0
    startT = encodeBytes[encodeIndex][1]
    #print(startT)
    #print(vp8Rates[targetIndex][1])

    # find the first used vp8 set rate!!
    while startT > setRates[targetIndex][1]:
        targetIndex += 1
    while targetIndex < len(setRates):
        print("===================================")
        print(f"target: {targetIndex - 1} ; {setRates[targetIndex - 1][1] % 10000000}")
        print("encodeIndex:",encodeIndex)
        print("setRates[targetIndex][1]:", setRates[targetIndex][1])
        print("encodeBytes[encodeIndex][1]: ",encodeBytes[encodeIndex][1])
        while encodeIndex < len(encodeBytes) and encodeBytes[encodeIndex][1] < setRates[targetIndex][1]:
            print(f"{encodeBytes[encodeIndex][0]} ; {encodeBytes[encodeIndex][1]% 10000000} ")
            if encodeBytes[encodeIndex][0] != "DROP":
                bytes += encodeBytes[encodeIndex][0]
            encodeIndex += 1
        if encodeIndex < len(encodeBytes):
            endT = encodeBytes[encodeIndex - 1][1] + 33333
            if bytes != 0:
                encodeRates.append([float(bytes * 8 * 1000000) / (float(endT - startT)), setRates[targetIndex - 1][1]])
            else:
                encodeRates.append([0, setRates[targetIndex - 1][1]])
            startT = encodeBytes[encodeIndex][1]
            bytes = 0
            targetIndex += 1
            print("targetIndex:",targetIndex)
        else:
            break
    # encodeRates.pop(0)
    print("encodeRates:")
    for i in encodeRates:
        print(f"rate: {i[0]} ; {i[1] % 10000000}")

    # ==================================
    ## calculate recv_rate
    recv_ratef = open('log/recv_rate.txt', 'r')
    recvLine = recv_ratef.readline()
    recv_rates = []
    recvT = []
    while recvLine:
        recv_rates.append(float(recvLine[:recvLine.index(" ; ")]))
        # recvT.append(int(float(recvLine[recvLine.index(" ; ") + len(" ; ") : recvLine.index("\n")]) /1000) %1000000 \
        #     - allStartT)
        recvT.append(float(recvLine[recvLine.index(" ; ") + len(" ; ") : recvLine.index("\n")]) - allStartT)
        #print("recvPLT: ", [recv_rates[-1], recvT[-1]])
        recvLine = recv_ratef.readline()

    print("======================]\n")
    print("recv_rates:", recv_rates)
    print("======================]\n")
    print("recvT:",recvT)
    
    # =================================
    ## draw mahimahi
    mahif = open('12mbps.trace', 'r')
    mahiLine = mahif.readline()
    mahiRate = []
    mahiT = []
    lastT = None
    while mahiLine:
        pktNum = 1
        if lastT != None:
            while mahiLine and int(mahiLine) == lastT:

                mahiLine = mahif.readline()
        else:
            mahiRate.append(pktNum * 1500 * 8 * 1000 / int(mahiLine))
        mahiLine = mahif.readline()
        mahiLine = mahif.readline()

    mahiRate, mahiT = drawMAHItrace()
    mahiRate, mahiT = drawMahiRate.drawMahiTrace(f"mahiTraces/{traceType}/trace{traceNum}.log")
    
    # mahiT = [int(i /1000) for i in mahiTus]
    print("======================\n")
    print("mahiT:", mahiT)
    # ==================================
    ## get the whole pack
    
    print("allstartT:", allStartT)
    
    plotTarget = []
    plotEnc = []
    plotSet = []
    plotTrace = []
    plotTargetT = []
    plotEncT = []
    plotSetT = []
    plotTraceT = []
    for i in vp8Rates:
        plotTarget.append(i[0])
    for i in encodeRates:
        plotEnc.append(i[0])
    for i in setRates:
        plotSet.append(i[0])
    # for i in trace:
    #     plotTrace.append(i[0] * 1000)
    for i in vp8Rates:
        plotTargetT.append(i[1] - allStartT)
    for i in encodeRates:
        plotEncT.append(i[1] - allStartT)
    for i in setRates:
        plotSetT.append(i[1] - allStartT)
    # for i in trace:
    #     plotTraceT.append(i[1] - allStartT)
        #print(plotTraceT[-1])

    # plotTrace, plotTraceT是之前用tc仿真网络时使用的，现在使用mahi，所以不再使用plotTrace
    # return plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, plotTraceT, plotTrace, recvT, recv_rates, mahiT, mahiRate
    return plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, recvT, recv_rates, mahiT, mahiRate
    

def main():
    traceType = 'random'
    traceNum = 38
    plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, \
                    plotRecvT, plotRecv, mahiT, mahiRate= getPLTlist(traceType, traceNum)
    plt.figure(figsize=(12,7))
    plt.plot(plotTargetT, plotTarget, alpha = 0.4, label='vp8 rate', color = 'blue')
    plt.plot(plotEncT, plotEnc, alpha = 0.6, label='actual rate', color = 'red')
    plt.plot(plotSetT, plotSet, alpha = 0.9, label='gcc rate', color='brown')
    #plt.plot(plotTraceT, plotTrace, alpha = 0.5, label='network bandwidth', color='grey')
    plt.plot(plotRecvT, plotRecv, alpha = 0.7, label='recv rate', color='orange')
    plt.step(mahiT, mahiRate, alpha = 0.5, label='network bandwidth', color='grey')
    plt.legend(loc=1)
    plt.xlabel("t (us)")
    plt.ylabel("bitrate (bps)")
    plt.grid()
    plt.savefig("tmp/bitrate.png")

if __name__ == '__main__':
    main()