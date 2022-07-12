# For finding all the delay components in the bwe time. 
# usage: When a bwe time is too much larger than 200ms, this py can be used to find out the reason 

import matplotlib.pyplot as plt
import delayTools.gotBWETime as gotBWETime

def getHiddenDelay(string1, string2):
    trainf = open('log/trainRemote.txt', 'r')

    t1 = []
    t2 = []

    trainLine = trainf.readline()
    while trainLine:
        if string1 in trainLine:
            t1.append(int(trainLine[len(string1):]))
        if string2 in trainLine:
            t2.append(int(trainLine[len(string2):]))
        trainLine = trainf.readline()
    print(t1)
    deltaT = []
    i = 0
    while i < len(t1) and i < len(t2):
        deltaT.append(t2[i] - t1[i])
        i += 1
    return deltaT

def gotRequestDelay():
    recvf = open('log/recv.txt', 'r')
    t1 = []
    recvLine = recvf.readline()
    while recvLine:
        if "KOYONYONG: RequestForBandwidth atTime: " in recvLine:
            t1.append(int(recvLine[len("KOYONYONG: RequestForBandwidth atTime: "):] )/ 1000)
        recvLine = recvf.readline()

    trainf = open('log/trainRemote.txt', 'r')
    t2 = []
    trainLine = trainf.readline()
    while trainLine:
        if "got request at " in trainLine:
            t2.append(int(trainLine[len("got request at "):]))
        trainLine = trainf.readline()

    deltaT = []
    i = 0
    while i < len(t1) and i < len(t2):
        deltaT.append(t2[i] - t1[i])
        i += 1
    return deltaT

def gotBWEDelay():
    recvf = open('log/recv.txt', 'r')
    t2 = []
    recvLine = recvf.readline()
    while recvLine:
        if "KOYONYONG: got BWE atTime: " in recvLine:
            t2.append(int(recvLine[len("KOYONYONG: got BWE atTime: "):] )/ 1000)
        recvLine = recvf.readline()

    trainf = open('log/trainRemote.txt', 'r')
    t1 = []
    trainLine = trainf.readline()
    while trainLine:
        if "sent bwe to appRecv at " in trainLine:
            t1.append(int(trainLine[len("sent bwe to appRecv at "):]))
        trainLine = trainf.readline()

    deltaT = []
    i = 0
    while i < len(t1) and i < len(t2):
        deltaT.append(t2[i] - t1[i])
        i += 1
    return deltaT

totalDelta = []
deltaT = getHiddenDelay("FloatTensor_reshaped at ", "policy_old.forwarded at ")
plt.plot(range(len(deltaT)), deltaT, label='policy_old.forwarded at ', alpha = 0.4, color = 'red')
totalDelta.append(deltaT)

deltaT = getHiddenDelay("sorted packlist at ", "processed packlist at ")
plt.plot(range(len(deltaT)), deltaT, label='processed packlist at ', alpha = 0.4, color = 'orange')
totalDelta.append(deltaT)

deltaT = getHiddenDelay("processed delay_gradient at ", "processed loss_ratio at ")
plt.plot(range(len(deltaT)), deltaT, label='processed loss_ratio at ', alpha = 0.4, color = 'green')
totalDelta.append(deltaT)

deltaT = getHiddenDelay("send [estimator, stat] at ", "sent [estimator, stat] at ")
plt.plot(range(len(deltaT)), deltaT, label='sent [estimator, stat] at ', alpha = 0.4, color = 'purple')
totalDelta.append(deltaT)

deltaT = gotRequestDelay()
plt.plot(range(len(deltaT)), deltaT, label='gotRequest', alpha = 0.7, color = 'cyan')
totalDelta.append(deltaT)

deltaT = gotBWEDelay()
plt.plot(range(len(deltaT)), deltaT, label='gotBWE', alpha = 0.7, color = 'pink')
totalDelta.append(deltaT)

deltaT = getHiddenDelay("send 'asking for bwe' at ", "sent 'asking for bwe' at ")
plt.plot(range(len(deltaT)), deltaT, label="sent 'asking for bwe' at ", alpha = 1, color = 'yellow')
totalDelta.append(deltaT)

gotTime, bigDelay = gotBWETime.gotBWETime()
plt.plot(range(len(gotTime)), gotTime, label='Total Time', alpha = 0.3, color = 'blue')

restTime = gotTime[:]
for singleDelta in totalDelta:
    i = 0
    while i < len(restTime) and i < len(singleDelta):
        restTime[i] -= singleDelta[i]
        i += 1
plt.plot(range(len(restTime)), restTime, label='Rest Time', alpha = 1, color = 'black')

plt.legend()
plt.grid()
plt.savefig('tmp/hiddenDelay.png')