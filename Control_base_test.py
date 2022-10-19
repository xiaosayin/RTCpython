import subprocess
import time
import random
import os
import numpy as np

videos = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]

record_file = "/run/media/yinwenpei/data_of_RTC/base_test_files/Env_record.txt"
Eval_file = "Base_Average_record.txt"
Packet_file = "In_this_RTC.txt"
all_avg_file = "/run/media/yinwenpei/data_of_RTC/base_test_files/all_avg.txt"


def one_test(portNum,traceNum, traceType, video_id, queLength, lossRate):
    RTC_process = subprocess.Popen(f"python3 peerconnection_serverless_args.py --portNum={portNum} --traceNum={traceNum} --traceType={traceType} \
    --video_id={video_id} --queLength={queLength} --lossRate={lossRate}", shell=True)
    RTC_process.wait()
    print("RTC_process done!")

    time.sleep(2)

    Base_Evaluation_process = subprocess.Popen(f"python3 baseline_Evaluation_args.py --portNum=8000 --traceNum={traceNum} --traceType={traceType} \
    --video_id={video_id} --queLength={queLength} --lossRate={lossRate}", shell=True)
    Base_Evaluation_process.wait()
    print("Base_Evaluation_process done!")

# env = [traceType, traceNum, queLength, lossRate, video_id]

def calculate_avg():
    record_traceType = []
    record_traceNum = []
    record_queLength = []
    record_lossRate = []
    record_video_id = []
    fd = open(record_file, "r")
    envs = fd.readlines()
    fd.close()
    for env in envs:
        env = env.strip()  # 去除换行符
        env = env.strip("[]")  # 去除列表的[]符号
        env = env.split(",")  # 已经成为列表，不过列表中的所有元素均为 str
        record_traceType.append(eval(env.pop(0)))
        record_traceNum.append(int(env.pop(0)))
        record_queLength.append(int(env.pop(0)))
        record_lossRate.append(float(env.pop(0)))
        record_video_id.append(int(env.pop(0)))
    record_vmaf = []
    record_psnr = []
    record_ssim = []
    record_frame_delay = []
    record_frame_loss = []

    record_recv_rate = []
    record_packet_delay = []
    record_packet_loss = []
    for i in range(len(record_traceNum)):
        readPath = f"/run/media/yinwenpei/data_of_RTC/base_test_files/{record_traceType[i]}_{record_traceNum[i]}_video_id{record_video_id[i]}_queLength{record_queLength[i]}_lossRate{record_lossRate[i]}/"
        if os.path.exists(readPath+Eval_file):
            Eval_fd = open(readPath+Eval_file, "r")
            Eval_lines = Eval_fd.readlines()
            Eval_fd.close()
        else:
            print(readPath+Eval_file + " not exist! Continue next")
            continue

        for line in Eval_lines:
            if "Vmaf:" in line:
                vmaf = float(line[line.index("Vmaf:") + len("Vmaf:") : ])
                record_vmaf.append(vmaf)

            if "Parsed_psnr" in line:
                psnr = float(line[line.index("average:") + len("average:") : line.index("min")])
                record_psnr.append(psnr)

            if "SSIM" in line:
                ssim = float(line[line.index("All:") + len("All:") : line.index("All:") + len("All:") + 8])
                record_ssim.append(ssim)

            if "new frame_loss_rate" in line:
                frame_loss_rate = float(line[line.index("frame_loss_rate:") + len("frame_loss_rate:") : ])
                record_frame_loss.append(frame_loss_rate)

            if "frame_delay" in line:
                frame_delay = float(line[line.index("frame_delay:") + len("frame_delay:") : ])
                record_frame_delay.append(frame_delay)

            print(line)

        # count packet data
        if os.path.exists(readPath+Packet_file):
            packet_fd = open(readPath + Packet_file, "r")
            packet_line = packet_fd.readline()
            packet_fd.close()
        else:
            print(readPath + Packet_file + " not exist! Continue next!")
            continue

        recv_rate = float(packet_line[packet_line.index("recv_rate =") + len("recv_rate =") : packet_line.index(", delay")])
        packet_delay = float(packet_line[packet_line.index("delay =") + len("delay =") : packet_line.index(", loss")])
        packet_loss = float(packet_line[packet_line.index("loss =") + len("delay ="): ])

        record_recv_rate.append(recv_rate)
        record_packet_delay.append(packet_delay)
        record_packet_loss.append(packet_loss)

        print(packet_line)
    avg_vmaf = np.mean(record_vmaf)
    avg_psnr = np.mean(record_psnr)
    avg_ssim = np.mean(record_ssim)
    avg_frame_delay = np.mean(record_frame_delay)
    avg_frame_loss = np.mean(record_frame_loss)

    avg_recv_rate = np.mean(record_recv_rate)
    avg_packet_delay = np.mean(record_packet_delay)
    avg_packet_loss = np.mean(record_packet_loss)

    with open(all_avg_file, "w") as avg_fd:
        avg_fd.write("test traces numbers: " + str(len(record_vmaf)) + "\n")

        avg_fd.write("avg_vmaf: " + str(avg_vmaf) + "\n")
        avg_fd.write("avg_psnr: " + str(avg_psnr) + "\n")
        avg_fd.write("avg_ssim: " + str(avg_ssim) + "\n")
        avg_fd.write("avg_frame_delay: " + str(avg_frame_delay) + "\n")
        avg_fd.write("avg_frame_loss: " + str(avg_frame_loss) + "\n")

        avg_fd.write("avg_recv_rate: " + str(avg_recv_rate) + "\n")
        avg_fd.write("avg_packet_delay: " + str(avg_packet_delay) + "\n")
        avg_fd.write("avg_packet_loss: " + str(avg_packet_loss) + "\n")







def main():
    record_Env = []
    once_Env = []  #[]
    total_trace_count = 50
    portNum = 8001
    os.system("rm -rf /home/yinwenpei/rtc_signal/baseline_frame_id.txt")

    for i in range(total_trace_count):
        once_Env = []
        traceRandom = random.randint(0, 499)
        if traceRandom < 500:
            traceType = 'random_2M'
        else:
            traceType = 'periodic'
        traceNum = traceRandom % 500
        queLength = random.randint(6, 349)
        lossRate = float(random.randint(0, 500)) / 100
        video_id = random.randint(0, 4)  # [Johnny, KristenAndSara, vidyo1, vidyo3, FourPeople]
        one_test(portNum, traceNum, traceType, video_id, queLength, lossRate)
        once_Env = [traceType, traceNum, queLength, lossRate, video_id]
        record_Env.append(once_Env)
        portNum += 1
        if portNum == 8049:
            portNum = 8000

    with open(record_file, "w") as f:
        for env in record_Env:
            f.writelines(str(env) + "\n")

    # caluculate all average data
    calculate_avg()

if __name__ == "__main__":
    main()