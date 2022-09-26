import numpy as np
import cv2
import os

height = 720
width = 1280
frame_size = int(1.5 * width * height)

video_files = ["Johnny", "KristenAndSara", "vidyo1", "vidyo3", "FourPeople"]
video_id = 4
yuv_path = f"/home/yinwenpei/RTCPython/testmedia/{video_files[video_id]}/{video_files[video_id]}_1280x720_30.yuv"

repeat_yuv_file = f"/home/yinwenpei/RTCPython/testmedia/{video_files[video_id]}/repeat12_{video_files[video_id]}.yuv"
repeat_fd = open(repeat_yuv_file,'wb')

repeat_times = 12

yuv_fd = open(yuv_path, "rb")
yuv_size = os.path.getsize(yuv_path)
total_frames = int(yuv_size / frame_size)
all_frame_data_bytes = yuv_fd.read(yuv_size)

for i in range(repeat_times):
    repeat_fd.write(all_frame_data_bytes)

repeat_fd.close()
yuv_fd.close()

