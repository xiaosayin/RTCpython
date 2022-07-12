# plot the time used of getting the bwe on the receiver side
# eg: AlphaRTC starts requesting for bwe -> AlphaRTC gets the bwe

import matplotlib.pyplot as plt

def gotBWETime():
    recvf = open("log/recv.txt", 'r')
    recvLine = recvf.readline()
    gotTime = []
    bigDelayCnt = 0
    while recvLine:
        if "KOYONYONG: got BWE used: " in recvLine:
            gotTime.append(int(recvLine[len("KOYONYONG: got BWE used: "):])/1000)
            if int(recvLine[len("KOYONYONG: got BWE used: "):])/1000 > 7:
                bigDelayCnt += 1
        recvLine = recvf.readline()

    trainf = open("log/send.txt", 'r')
    trainLine = trainf.readline()
    bweSentT = []
    while trainLine:
        if "Bwe Sent: " in trainLine:
            t1 = int(trainLine[len("Bwe Sent:  "):])
            bweSentT.append(t1)
        trainLine = trainf.readline()
    return gotTime, bigDelayCnt

def main():
    gotTime, bigDelayCnt = gotBWETime()
    #plt.plot(range(len(bweSentT)), bweSentT, label='RL Time', alpha = 0.5, color = 'red')
    plt.plot(range(len(gotTime)), gotTime, label='Total Time', alpha = 0.5, color = 'blue')

    plt.xlabel('RL')
    plt.ylabel('used ms')
    plt.grid()
    plt.savefig('tmp/recv_2021_12_13_19_222222.jpg')
    print("bigDelayCnt: ", bigDelayCnt)

if __name__ == "__main__":
    main()
