import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import time
import math
import info
import numpy as np
import subprocess

def addT(T, type, time):
    if type != "is_KeyFrame":
        time = int(time/1000)
        time = int(time % 1000000)
    if T == []:
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if type == "gotT":
        T[0] = time
    elif type == "beforeEncT":
        T[1] = time
    elif type == "is_KeyFrame":
        T[2] = time
    elif type == "afterEncT":
        T[3] = time
    elif type == "sendT":
        T[4] = time
    elif type == "recvT1":
        T[5] = time
    elif type == "recvT2":
        T[6] = time
    elif type == "beforeDecT":
        T[7] = time
    elif type == "afterDecT":
        T[8] = time
    elif type == "beforeRenderT":
        T[9] = time
    elif type == "RenQueueRecved":
        T[10] = time
    elif type == "afterRenderT":
        T[11] = time
    return T

def getTime(line, log):
    return int(line[line.index(log) + len(log): ])

def getAllFrame():
    # get Lost frame
    # 0: enc drop
    # -1: path lost
    # -2: path left
    # -3: dec drop
    recvf = open("./log/recv.txt")
    recvLine = recvf.readline()
    decFrame = []
    completeFrame = []
    decLog = "KOYONYONG: decoded size: "
    timeLog = " atTime: "
    # decFrame = [frameSize, [gotT, beforeEncT, afterEncT, sendT,
    #                recvT1, recvT2, beforeDecT, afterDecT,
    #               beforeRenderT, RenQueueRecved, afterRenderT], ifDropped]
    inI = 0
    decI = 0
    renI = 0
    addI = 0
    writI = 0
    writDrop = 0
    while recvLine:
        if "KOYONYONG: first packet in:" in recvLine:
            completeFrame.append([0, 0, int(getTime(recvLine, timeLog)/1000)% 1000000, 0])

        if "KOYONYONG: last packet in:" in recvLine:
            completeFrame[inI][info.cIn2I] = int(getTime(recvLine, timeLog)/1000)% 1000000

        if "KOYONYONG: one complete frame" in recvLine:
            completeFrame[inI][info.cSizeI] = int(recvLine[recvLine.index("KOYONYONG: one complete frame ") + len("KOYONYONG: one complete frame ") : recvLine.index(", frame->Timestamp(): ")])
            completeFrame[inI][info.cRtpI] = int(recvLine[recvLine.index(", frame->Timestamp(): ") + len(", frame->Timestamp(): ") :])% 10000000
            inI += 1

        if "KOYONYONG: before decode:" in recvLine:
            decFrame.append([0, 0, addT([], "beforeDecT", getTime(recvLine, timeLog)), 0])

        if decLog in recvLine:
            decFrame[decI][info.dSizeI] = int(recvLine[recvLine.index(decLog) + len(decLog):recvLine.index(", timeStamp: ")])
            decFrame[decI][info.dRtpI] = int(recvLine[recvLine.index(", timeStamp: ") + len(", timeStamp: "):])% 10000000

        if "KOYONYONG: after decode:" in recvLine:
            decFrame[decI][info.dRtpI + 1] = addT(decFrame[decI][info.dRtpI + 1], "afterDecT", getTime(recvLine, timeLog))
            i = len(completeFrame) - 1
            while i >= 0:
                if completeFrame[i][info.cRtpI] == decFrame[decI][info.cRtpI]:
                    decFrame[decI][info.dRtpI + 1][5:7] = completeFrame[i][info.cIn1I:]
                    completeFrame.pop(i)
                    inI -= 1
                    break
                i -= 1
            decI += 1

        if "KOYONYONG: IncomingVideoStream::OnFrame atTime:" in recvLine:
            decFrame[renI][info.dRtpI + 1] = addT(decFrame[renI][info.dRtpI + 1], "beforeRenderT", getTime(recvLine, timeLog))
            renI += 1

        if "KOYONYONG: added frame: " in recvLine:
            decFrame[addI][info.dRtpI + 1] = addT(decFrame[addI][info.dRtpI + 1], "RenQueueRecved", getTime(recvLine, timeLog))
            addI += 1

        if "KOYONYONG: Frame scheduled out of order," in recvLine \
                or "KOYONYONG: Too old frame, " in recvLine\
                or "KOYONYONG: Frame too long into the future," in recvLine:
            decFrame[addI - 1][info.dDroppedI] = -3

        if "KOYONYONG: ++frames_dropped_:" in recvLine:
            writDrop += 1

        if "KOYONYONG: written to frame:" in recvLine:
            while (decFrame[writI][info.dDroppedI] == -3):
                writI += 1
            while writDrop > 0:
                decFrame[writI][info.dDroppedI] = -3
                writDrop -= 1
                writI += 1
            decFrame[writI][info.dRtpI + 1] = addT(decFrame[writI][info.dRtpI + 1], "afterRenderT", getTime(recvLine, timeLog))
            decFrame[writI][info.dDroppedI] = 1
            writI += 1

        recvLine = recvf.readline()
        '''
    print("decFrame:")
    for i in decFrame:
        print(i)
        '''
    recvf.close()

    if decFrame == []:
        return []

    while decFrame[-1][info.dDroppedI] == 0:
        decFrame.pop()
    ##==================================
    # get Lost frame
    # 0: enc drop
    # -1: path lost
    # -2: path left
    # -3: dec drop
    sendf = open("./log/send.txt")
    sendLine = sendf.readline()
    encLog = "KOYONYONG: encoded_image.size(): "

    allFrame = []
    # allFrame = [frameSize, [gotT, beforeEncT, afterEncT, sendT,
    #                recvT1, recvT2, beforeDecT, afterDecT,
    #               beforeRenderT, RenQueueRecved, afterRenderT], ifDropped]
    encI = 0
    frameCnt = 0
    senI = 0
    while sendLine:
        if "KOYONYONG: got frame" in sendLine:
            allFrame.append([frameCnt, 1, 1, 1, 1, addT([], "gotT", getTime(sendLine, timeLog)), 2])
            frameCnt += 1
        if "Drop frame in order to respect" in sendLine:
            allFrame[frameCnt - 1][info.tmpDroppedI] = 0


        #drop before enc
        if "KOYONYONGDROP" in sendLine or "Same/old NTP timestamp" in sendLine:
            while allFrame[encI][info.tmpDroppedI] == 0:
                encI += 1
            for i in range(info.SizeI, info.RtpI + 1):
                allFrame[encI][i] = 0
            allFrame[encI][info.tmpDroppedI] = 0
            encI += 1

        if "KOYONYONG: Before enc" in sendLine:
            while allFrame[encI][info.tmpDroppedI] == 0:
                encI += 1
            allFrame[encI][info.RtpI + 1] = addT(allFrame[encI][info.RtpI + 1], "beforeEncT", getTime(sendLine, timeLog))
            allFrame[encI][info.widthI] = int(sendLine[sendLine.index("KOYONYONG: Before enc: ") + len("KOYONYONG: Before enc: ") : sendLine.index(timeLog)])

        if "KOYONYONG: this frame is KEYFRAME" in sendLine:
            allFrame[encI][info.RtpI + 1] = addT(allFrame[encI][info.RtpI + 1], "is_KeyFrame", True)
        elif "KOYONYONG: this frame is not KEYFRAME" in sendLine:
            allFrame[encI][info.RtpI + 1] = addT(allFrame[encI][info.RtpI + 1], "is_KeyFrame", False)


        if "KOYONYONG: PSNR:" in sendLine:
            allFrame[encI][info.PSNRI] = int(float(sendLine[sendLine.index("AVERAGE: ") + len("AVERAGE: ") : ])* 10000)

        if encLog in sendLine:
            allFrame[encI][info.SizeI] = int(sendLine[sendLine.index(encLog) + len(encLog) : sendLine.index(timeLog)])


        if "KOYONYONG: encoded_image sent:" in sendLine:
            allFrame[encI][info.RtpI] = int(sendLine[sendLine.index(", rtpTimeStamp: ") + len(", rtpTimeStamp: ") : sendLine.index(timeLog)])%10000000
            allFrame[encI][info.RtpI + 1] = addT(allFrame[encI][info.RtpI + 1], "sendT", getTime(sendLine, timeLog))
            allFrame[encI][info.tmpDroppedI] = 1

        #dropped in enc
        if "NOTHING111" in sendLine:
            for i in range(info.SizeI, info.RtpI + 1):
                allFrame[encI][i] = 0
            allFrame[encI][info.tmpDroppedI] = 0

        if "KOYONYONG: After enc" in sendLine:
            allFrame[encI][info.RtpI + 1] = addT(allFrame[encI][info.RtpI + 1], "afterEncT", getTime(sendLine, timeLog))
            encI += 1


        sendLine = sendf.readline()



    sendf.close()

    while allFrame[-1][info.tmpDroppedI] == 2:
        allFrame.pop()
    '''
    print("allFrame:")
    for i in allFrame:
        print(i)
    '''
    #================================
    # get Lost frame
    # 0: enc drop
    # -1: path lost
    # -2: path left
    # -3: dec drop
    encI = 0
    for dec in decFrame:
        while allFrame[encI][info.tmpDroppedI] == 0:
            encI += 1
        while dec[info.dRtpI] != allFrame[encI][info.RtpI]:
            allFrame[encI][info.tmpDroppedI] = -1
            encI += 1
            while allFrame[encI][info.tmpDroppedI] == 0:
                encI += 1
        if dec[info.dRtpI] == allFrame[encI][info.RtpI]:
            allFrame[encI][info.RtpI + 1][5:12] = dec[info.dRtpI + 1][5:]
        if dec[info.dDroppedI] == -3:
            allFrame[encI][info.tmpDroppedI] = -3
        encI += 1

    while encI < len(allFrame):
        allFrame[encI][info.tmpDroppedI] = -2
        encI += 1
    '''
    print("allFrame:")
    for i in allFrame:
        print(i)
    '''
    return allFrame
#================================
# get render lost
# 0: enc drop
# -1: path lost
# -2: path left
# -3: dec drop



def cutYUV(allFrame, videoName):
    if allFrame == []:
        return
    totalLostFrame = []
    for i in range(len(allFrame)):
        if allFrame[i][info.tmpDroppedI] != 1:
            totalLostFrame.append(i)
    '''
    print("Lost: ", totalLostFrame)
    '''
    cutCmd = f"echo y | ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i testmedia/{videoName}/{videoName}_1280x720_30_70s.yuv -filter:v select='{makeCutString(totalLostFrame)}' -vsync 0 -r 30 -s 1280x720 -pix_fmt yuv420p result/cut.yuv"
    os.system(cutCmd)

def drawTruePSNR():
    os.system("ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i result/outvideo.y4m -lavfi psnr=\"stats_file=psnr.log\" -f null -")
    
    psnrf = open("psnr.log", 'r')
    psnrLine = psnrf.readline()
    frameNum = os.popen("ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 result/outvideo.y4m").read()
    print("frameNum: ", frameNum)
    if frameNum == "":  #rtc break down!
        return None
    psnr = []
    psnrVal = []
    while psnrLine:
        psnr.append(float(psnrLine[psnrLine.index("psnr_avg:") + len("psnr_avg:"): psnrLine.index(" psnr_y:")]))
        psnrVal.append(math.pow(10, psnr[-1] / 10))
        psnrLine = psnrf.readline()
        if len(psnr) == int(frameNum):
            break

        
    plt.cla()
    x_major_locator=MultipleLocator(300)
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    plt.plot(range(len(psnr)), psnr)
    plt.grid()
    plt.savefig(f"result/delay/TruePSNR.png")

    plt.cla()
    x_major_locator=MultipleLocator(300)
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    plt.plot(range(len(psnrVal)), psnrVal)
    plt.grid()
    plt.savefig(f"result/delay/TruePSNRVal.png")
    return psnr, np.mean(psnr)




def makeCutString(lostFrame):
    string = ""
    for i in lostFrame:
        if string == "":
            string += f"eq(n\, {i})"
        else:
            string += f" + eq(n\, {i})"
    string = "not(" + string + ")"
    return string

def VQA():
    method = "libvmaf"
    #method = "psnr"
    frameNum = os.popen("ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 result/outvideo.y4m").read()
    score1 = os.popen(f"/usr/bin/ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i result/outvideo.y4m -vframes {int(frameNum)} -filter_complex {method} -f null -").read()
    score2 = os.popen(f"/usr/bin/ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i result/outvideo.y4m -vframes {int(frameNum)} -filter_complex {'psnr'} -f null -").read()
    print(f"vmaf: {score1}")
    print(f"psnr: {score2}")

def VMAF():
    method = "libvmaf"
    #method = "psnr"
    frameNum = os.popen("ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 result/outvideo.y4m").read()
    out = subprocess.Popen(f"ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i result/outvideo.y4m -vframes {int(frameNum)} -filter_complex {method} -f null -", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell = True)
    stdout, stderr = out.communicate()
    stdout = stdout.decode("utf-8")
    return (float(stdout[stdout.index("VMAF score: ") + len("VMAF score: "):-2]))

# decFrame = [frameSize, [gotT 0, beforeEncT 1, afterEncT 2, sendT 3,
#                recvT1 4, recvT2 5, beforeDecT 6, afterDecT 7,
#               beforeRenderT 8 , RenQueueRecved 9, afterRenderT 10], ifDropped]
def getFrameDelay(allFrame):
    delay = ["got_beforeEnc", "beforeEnc_send", "is_Key", \
            "send_afterEnc", "afterEnc_beforeDec", \
            "beforeDec_beforeRender", "beforeRender_RenQueueRecved", \
            "RenQueueRecved_afterRenderT", "P2P_Delay"]
    frameDelay = []
    for i in delay:
        frameDelay.append([])
    frameDelay.append([])
    deltaT = 0
    for frame in allFrame:
        if frame[info.tmpDroppedI] != 1:
            #delay.append(0)
            continue
        frameT= frame[info.RtpI + 1]
        frameDelay[0].append((frameT[1] - frameT[0]))  #"got_beforeEnc"
        frameDelay[1].append((frameT[3] - frameT[1]))  #"beforeEnc_send"
        frameDelay[2].append((frameT[2] - frameT[3]))  #"send_afterEnc"
        if frameT[7] - frameT[3] < 0:
            frameDelay[3].append((frameT[7] - frameT[3] + 1000000))  #"afterEnc_beforeDec"
        else:
            frameDelay[3].append((frameT[7] - frameT[3]))  #"afterEnc_beforeDec"
        frameDelay[4].append((frameT[8] - frameT[6]))  #"beforeDec_beforeRender"
        frameDelay[5].append((frameT[9] - frameT[8]))  #"beforeRender_RenQueueRecved"
        frameDelay[6].append((frameT[10] - frameT[9]))  #"RenQueueRecved_afterRenderT"
        frameDelay[7].append((frameT[10] - frameT[0]))  #"P2P_Delay"
        frameDelay[8].append(frame[info.SizeI])
    index = 0
    for i in delay:
        #print(i)
        plt.figure(index + 1)
        plt.grid()
        j = 0
        while j < len(frameDelay[index]):
            #print([frameDelay[8][j], frameDelay[index][j]])
            j += 1
        plt.plot(range(1, len(frameDelay[index]) + 1), frameDelay[index])
        plt.xlabel("Frame Index")
        plt.ylabel("Delay Time (ms)")
        plt.savefig(f"result/delay/{index + 1}{i}.png")
        index += 1

    return frameDelay[3]


def getPSNR(allFrame):
    PSNR = []
    for i in allFrame:
        if i[info.tmpDroppedI] != 1:
            continue
        #PSNR.append(pow(10, float(i[PSNRI]/10000/10)))
        PSNR.append(float(i[info.PSNRI]/10000))
    plt.figure(11)
    plt.plot(range(1, len(PSNR) + 1), PSNR)
    plt.grid()
    plt.savefig(f"result/delay/PSNR.png")
    return PSNR

def getWebRTCDelay():
    delay = []
    recvf = open("./log/recv.txt")
    recvLine = recvf.readline()
    while recvLine:
        if "KOYONYONG: delay_ms: " in recvLine:
            delay.append(int(recvLine[len("KOYONYONG: delay_ms: ") : ]))
        recvLine = recvf.readline()

    plt.figure(12)
    plt.plot(range(1, len(delay) + 1), delay)
    plt.xlabel("Frame Index")
    plt.ylabel("Delay Time (ms)")

    plt.grid()
    plt.savefig(f"result/delay/WebRTCDelay.png")
    return delay


def frameSkip(allFrame):
    if allFrame == []:
        return []
    skipped = []
    singleSkip =[]
    encI = 0
    skip = 0

    while encI < len(allFrame):
        skip = 0
        while encI < len(allFrame) and allFrame[encI][info.tmpDroppedI] != 1 :
            skip += 1
            encI += 1
        skipped.append(skip)
        encI += 1

    encI = 0
    while encI < len(allFrame):
        skip = 0
        if allFrame[encI][info.tmpDroppedI] != 1 :
            singleSkip.append(1)
        else:
            singleSkip.append(0)
        encI += 1

    if allFrame[-1][info.tmpDroppedI] != 1:
        skipped.pop()

    plt.figure(13)
    plt.scatter(range(1, len(skipped) + 1), skipped)
    plt.grid()
    plt.savefig(f"result/delay/frameSkip.png")
    return singleSkip

def plotFrameSize(allFrame):
    size = []
    for frame in allFrame:
        if frame[info.tmpDroppedI] == 1:
            size.append(frame[info.SizeI])
    plt.figure(14)
    plt.plot(range(1, len(size) + 1), size)
    plt.grid()
    plt.savefig(f"result/delay/frameSize.png")


def main():
    allFrame = getAllFrame()
    video = 0
    videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
        
    cutYUV(allFrame, videos[video])
    VQA()
    drawTruePSNR()
    print("getFrameDelay: ", round(time.time() * 1000))
    getFrameDelay(allFrame)
    getWebRTCDelay()
    print("frameSkip: ", round(time.time() * 1000))
    frameSkip(allFrame)
    plotFrameSize(allFrame)
    getPSNR(allFrame)
    print("out: ", round(time.time() * 1000))




if __name__ == '__main__':
    main()

