import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import time
import math
import info
import numpy as np
from multiprocessing import Array
from CLCC.frame_info import *

traceType = 'random'
traceNum = 38
queLength = 168
lossRate = 3
videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
video_id = 2
houzhui = f'{traceType}_{traceNum}_{queLength}_{lossRate}_{videos[video_id]}'

Average_recode_file = "./result/base_delay/Base_Average_record" + houzhui + ".txt"

def getTime(line, log):
    return int(line[line.index(log) + len(log):])


def addT(T, type, time):
    if type != "is_KeyFrame":
        time = int(time / 1000)
        time = int(time % 1000000)
    if T == []:
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if type == "gotT":
        T[0] = time
    elif type == "beforeEncT":
        T[1] = time
    elif type == "sendT":
        T[2] = time
    elif type == "complete_frameT":
        T[3] = time
    elif type == "beforeDecT":
        T[4] = time
    elif type == "afterDecT":
        T[5] = time
    elif type == "beforeRenderT":
        T[6] = time
    elif type == "RenQueueRecved":
        T[7] = time
    elif type == "afterRenderT":
        T[8] = time
    return T

def makeCutString(lostFrame):
    string = ""
    for i in lostFrame:
        if string == "":
            string += f"eq(n\, {i})"
        else:
            string += f" + eq(n\, {i})"
    string = "not(" + string + ")"
    return string

def cutYUV(drop_frame_id, videoName):
    if drop_frame_id == []:
        return
    
    cutCmd = f"echo y | /usr/bin/ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i testmedia/{videoName}/repeat12_{videoName}.yuv -filter:v select='{makeCutString(drop_frame_id)}' -fps_mode passthrough -r 30 -s 1280x720 -pix_fmt yuv420p result/cut.yuv"
    print(cutCmd)
    os.system(cutCmd)

def VQA():
    method = "libvmaf"
    #method = "psnr"
    frameNum = os.popen(f"/usr/bin/ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 {output_path}").read()
    Vmaf = os.popen(f"/usr/bin/ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i {output_path} -vframes {int(frameNum)} -filter_complex {method} -f null -").read()
    PSNR = os.popen(f"/usr/bin/ffmpeg -r 30 -s 1280x720 -pix_fmt yuv420p -i result/cut.yuv -r 30 -i {output_path} -vframes {int(frameNum)} -filter_complex {'psnr'} -f null -").read()
    print(f"vmaf: {Vmaf}")
    print(f"psnr: {PSNR}")
    return Vmaf,PSNR

def RGBVQA():
    method = "libvmaf"
    os.system("python3 convert_yuv2rgba.py --yuv=./result/cut.yuv --avi=./result/base_cut.avi")
    os.system("echo y | /usr/bin/ffmpeg -i ./result/outvideo.y4m ./result/outvideo.yuv")
    os.system("python3 convert_yuv2rgba.py --yuv=./result/outvideo.yuv --avi=./result/base_outvideo.avi")
    frameNum = os.popen(f"/usr/bin/ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 ./result/base_outvideo.avi").read()
    RGB_Vmaf = os.popen(f"/usr/bin/ffmpeg -r 30 -i result/base_cut.avi -r 30 -i ./result/base_outvideo.avi -vframes {int(frameNum)} -filter_complex {method} -f null -").read()
    RGB_PSNR = os.popen(f"/usr/bin/ffmpeg -r 30 -i result/base_cut.avi -r 30 -i ./result/base_outvideo.avi -vframes {int(frameNum)} -filter_complex {'psnr'} -f null -").read()
    print(f"RGBvmaf: {RGB_Vmaf}")
    print(f"RGBpsnr: {RGB_PSNR}")
    return RGB_Vmaf, RGB_PSNR
    
def getAllFrame(allFrame):
    sendf = open("./log/send.txt")
    sendLine = sendf.readline()
    timeLog = " atTime: "
    while sendLine:
        if "YINWENPEI: got frame ID" in sendLine:
            frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
            allFrame[frameCnt * timelistL + NumI] = frameCnt
            allFrame[frameCnt * timelistL + sizeI] = 1
            allFrame[frameCnt * timelistL + psnrI] = 1
            allFrame[frameCnt * timelistL + widthI] = 1
            allFrame[frameCnt * timelistL + heightI] = 1
            allFrame[frameCnt * timelistL + gotTI: frameCnt * timelistL + afterRenderTI + 1] = addT([], "gotT",
                                                                                                getTime(sendLine, timeLog))
            # print(sendLine)

        if "YINWENPEI: Before enc" in sendLine:
            # print(sendLine)
            frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
            allFrame[frameCnt * timelistL + NumI] = frameCnt
            allFrame[frameCnt * timelistL + widthI] = int(sendLine[sendLine.index("width") + 6:sendLine.index("height") - 2])
            allFrame[frameCnt * timelistL + heightI] = int(sendLine[sendLine.index("height") + 7:sendLine.index("at") - 2])
            allFrame[frameCnt * timelistL + beforeEncTI] = int((getTime(sendLine, timeLog) / 1000)) % 1000000

        if "YINWENPEI: PSNR" in sendLine:
            allFrame[frameCnt * timelistL + psnrI] = int(float(sendLine[sendLine.index("AVERAGE: ") + len("AVERAGE: ") : ])* 10000)
            print("PSNR frameCnt:", frameCnt)
            # allFrame[encI * info.frameL + info.PSNRI] = tmpAll[encI][info.PSNRI]

        # if "YINWENPEI after enc atTime" in sendLine:
        #     print("YINWENPEI after enc atTime", int((getTime(sendLine, timeLog) / 1000)) % 1000000)

        if "YINWENPEI: send encoded_image:" in sendLine:
            # print(sendLine)
            frameCnt = int(sendLine[sendLine.index("ID") + 3:sendLine.index(",")])
            allFrame[frameCnt * timelistL + NumI] = frameCnt
            allFrame[frameCnt * timelistL + sizeI] = int(sendLine[sendLine.index("size") + 5:sendLine.index("at") - 2])
            allFrame[frameCnt * timelistL + sendTI] = int((getTime(sendLine, timeLog) / 1000)) % 1000000
        
        sendLine = sendf.readline()
    sendf.close()
    
    recvf = open("./log/recv.txt")
    lineR = recvf.readline()
    decFrame = []
    completeFrame = []
    renderFrame = []
    # decLog = "KOYONYONG: decoded size: "
    while lineR:
        if "YINWENPEI: one complete frame" in lineR:
            Recv_frame_id = int(lineR[lineR.index("ID") + 3:lineR.index(",")])
            allFrame[Recv_frame_id * timelistL + complete_frameI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
            completeFrame.append(Recv_frame_id)
            # print(lineR)
        if "YINWENPEI before decode frame" in lineR:
            # print(lineR)
            try:
                Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
                allFrame[Recv_frame_id * timelistL + beforeDecTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
            except:
                print(lineR)

        if "YINWENPEI: after decode frame" in lineR:
            # print(lineR)
            try:
                Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
                allFrame[Recv_frame_id * timelistL + afterDecTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
                decFrame.append(Recv_frame_id)
            except:
                print(lineR)

        if "YINWENPEI: IncomingVideoStream::OnFrame ID" in lineR:
            # print(lineR)
            Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime")-2])
            allFrame[Recv_frame_id * timelistL + beforeRenderTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000

        if "YINWENPEI: RenderQueue frame ID" in lineR:
            # print(lineR)
            Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime") - 2])
            allFrame[Recv_frame_id * timelistL + RenQueueReceivedI] = int((getTime(lineR, timeLog) / 1000)) % 1000000

        if "YINWENPEI: written to frame" in lineR:
            # print(lineR)
            Recv_frame_id = int(lineR[lineR.index("ID") + 4:lineR.index("atTime") - 2])
            allFrame[Recv_frame_id * timelistL + afterRenderTI] = int((getTime(lineR, timeLog) / 1000)) % 1000000
            renderFrame.append(Recv_frame_id)
        lineR = recvf.readline()
    
    recvf.close()
    return allFrame,completeFrame,renderFrame

def getFrameDelay(allFrame,completeFrame):
    frame_delay = []
    for id in completeFrame:
        # print("beforeDecT:", allFrame[id * timelistL + beforeDecTI])
        # print("sendT:",allFrame[id * timelistL + sendTI])
        one_delay = allFrame[id * timelistL + beforeDecTI] - allFrame[id * timelistL + sendTI]
        if one_delay < 0:
            frame_delay.append((one_delay + 1000000))
            print("negative one_delay:", one_delay)
        else:#"afterEnc_beforeDec"
            frame_delay.append(one_delay)
    plt.figure(1)
    plt.grid()
    plt.plot(range(1, len(frame_delay) + 1), frame_delay)
    plt.xlabel("Frame Index")
    plt.ylabel("Delay Time (ms)")
    plt.savefig(f"./result/base_delay/frame_delay"+ houzhui + ".png")
    return frame_delay

def getPSNR(allFrame,renderFrame):
    PSNR = []
    for id in renderFrame:
        PSNR.append(float(allFrame[id * timelistL + psnrI]* allFrame[id * timelistL + widthI]/1280/10000))
    plt.figure(11)
    plt.plot(range(1, len(PSNR) + 1), PSNR)
    plt.grid()
    plt.savefig(f"result/base_delay/Enc_PSNR_" + houzhui + ".png")
    return PSNR

output_path = "./result/outvideo.y4m"
os.system("mv /home/yinwenpei/rtc_signal/baseline_frame_id.txt ./result/")

baseline_frame_id_txt = "./result/baseline_frame_id.txt"
frame_fd = open(baseline_frame_id_txt,"r")
lines = frame_fd.readlines()
recv_video_frame_id = [int(i) for i in lines]
print("recv_frame_numbers:", len(recv_video_frame_id))

whole_list = list(range(1,recv_video_frame_id[-1] + 1))

drop_frame_id = [i-1 for i in whole_list if i not in recv_video_frame_id]
print("drop_frame_id numbers:", len(drop_frame_id))

cutYUV(drop_frame_id, videos[video_id])
Vmaf, PSNR = VQA()
# RGB_Vmaf, RGB_PSNR = RGBVQA()

# get the allFrame timestamp info
## initial allFrame every element with -777
frame_numbers = 30 * 60 * 2
allFrame = Array('i', range(timelistL * 30 * 60 * 2))
for i in range(frame_numbers):
    allFrame[i] = -777

allFrame, completeFrame, renderFrame = getAllFrame(allFrame)

print("received_frame_id length: ", len(recv_video_frame_id))
print("renderFrame length: ",len(renderFrame))
frame_delay = getFrameDelay(allFrame,renderFrame)
print("average_frame_delay: ", sum(frame_delay)/len(frame_delay))
print("frame_loss_rate:", len(drop_frame_id)/len(whole_list))

Enc_PSNR = getPSNR(allFrame, renderFrame)
print("average Enc_PSNR:", sum(Enc_PSNR)/len(Enc_PSNR))
# print(recv_video_frame_id)
# print(len(recv_video_frame_id))

with open(Average_recode_file,"w") as f:
    f.write("YUV_Vmaf and YUV_PSNR:" + str(Vmaf) + ", " + str(PSNR) + "\n")
    # f.write("RGB_Vmaf and RGB_PSNR:" + str(RGB_Vmaf) + ", " + str(RGB_PSNR) + "\n")
    f.write("average_frame_delay: " + str(sum(frame_delay)/len(frame_delay)) + "\n")
    f.write("frame_loss_rate: " + str(len(drop_frame_id)/len(whole_list)) + "\n")
    f.write("average Enc_PSNR: "+ str(sum(Enc_PSNR)/len(Enc_PSNR)) + "\n")

# calculate the loss frame in transport


print("hello world!")

