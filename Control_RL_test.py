import subprocess
import time
import os
import random
import numpy as np

record_file = "/run/media/yinwenpei/data_of_RTC/base_test_files/Env_record.txt"
Eval_file = "RL_Average_record.txt"
Packet_file = "In_this_RTC.txt"
all_avg_file = "/run/media/yinwenpei/data_of_RTC/RL_test_files/all_avg.txt"

def one_test(portNum, traceNum, traceType, video_id, queLength, lossRate):
    # start interpolate frame process
    interpolate_process = subprocess.Popen(
        f"python3 Fast_fifo_recv.py --multi=2 --output=out_RGBA.avi --fps=30", shell=True,
        cwd="/home/yinwenpei/python_workspace/Practical-RIFE/")

    time.sleep(3)

    RTC_process = subprocess.Popen(
        f"python3 test2Remote_args.py --portNum={portNum} --traceNum={traceNum} --traceType={traceType} \
    --video_id={video_id} --queLength={queLength} --lossRate={lossRate}", shell=True)
    RTC_process.wait()
    interpolate_process.wait()
    print("RTC_process done!")

    time.sleep(2)

    Evaluation_process = subprocess.Popen(
        f"python3 Evaluation_args.py --portNum={portNum} --traceNum={traceNum} --traceType={traceType} \
    --video_id={video_id} --queLength={queLength} --lossRate={lossRate}", shell=True)
    Evaluation_process.wait()
    print("Evaluation_process done!")


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
        readPath = f"/run/media/yinwenpei/data_of_RTC/RL_test_files/{record_traceType[i]}_{record_traceNum[i]}_video_id{record_video_id[i]}_queLength{record_queLength[i]}_lossRate{record_lossRate[i]}/"
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

            if "frame_loss_rate" in line:
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

def get_envs(args_record_file):
    record_traceType = []
    record_traceNum = []
    record_queLength = []
    record_lossRate = []
    record_video_id = []
    fd = open(args_record_file, "r")
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
    return record_traceType, record_traceNum, record_queLength, record_lossRate, record_video_id

def main():
    # record_traceType = []
    # record_traceNum = []
    # record_queLength = []
    # record_lossRate = []
    # record_video_id = []
    # fd = open(record_file, "r")
    # envs = fd.readlines()
    # fd.close()
    # for env in envs:
    #     env = env.strip()  # 去除换行符
    #     env = env.strip("[]")  # 去除列表的[]符号
    #     env = env.split(",")  # 已经成为列表，不过列表中的所有元素均为 str
    #     record_traceType.append(eval(env.pop(0)))
    #     record_traceNum.append(int(env.pop(0)))
    #     record_queLength.append(int(env.pop(0)))
    #     record_lossRate.append(float(env.pop(0)))
    #     record_video_id.append(int(env.pop(0)))
    #
    # record_traceType, record_traceNum, record_queLength, record_lossRate, record_video_id = get_envs(record_file)
    # portNum = 8000
    # for i in range(len(record_traceNum)):
    #     traceNum = record_traceNum[i]
    #     traceType = record_traceType[i]
    #     video_id = record_video_id[i]
    #     queLength = record_queLength[i]
    #     lossRate = record_lossRate[i]
    #     portNum += 1
    #     one_test(portNum, traceNum, traceType, video_id, queLength, lossRate)
    one_test(portNum=8000, traceNum=34, traceType='random', video_id=1, queLength=168, lossRate=3)

    # calculate_avg()


if __name__ == "__main__":
    main()
