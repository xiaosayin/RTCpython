import numpy as np
import cv2
import os
import argparse

parser = argparse.ArgumentParser(description='convert yuv to rgba')

parser.add_argument('--yuv', dest='yuv', type=str, default=None)
parser.add_argument('--avi', dest='avi', type=str, default=None)

args = parser.parse_args()

# yuv_path = "/home/yinwenpei/RTCPython/result/outvideo.yuv"
yuv_path = args.yuv
width = 1280
height = 720
# vid_out_name = "/home/yinwenpei/RTCPython/result/base_outvideo.avi"
vid_out_name = args.avi
fps = 30
frame_size = int(1.5 * width * height)

assert (not args.yuv is None and not args.avi is None)

def yuv420p_to_gbr(Y, U, V):
    ih, iw = Y.shape
    yuvi420 = np.zeros((ih * 3 // 2, iw), np.uint8)
    yuvi420[:ih, :iw] = Y
    yuvi420[ih:ih * 5 // 4, :] = U.reshape(-1, iw)
    yuvi420[ih * 5 // 4:, :] = V.reshape(-1, iw)
    bgr = cv2.cvtColor(yuvi420, cv2.COLOR_YUV2BGR_I420)
    return bgr


def bgr_to_yuv420p(bgr):
    ih, iw, c = bgr.shape
    # yuvi420 = cv2.cvtColor(bgr, cv2.COLOR_RGB2YUV_I420)
    yuvi420 = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV_I420)
    Y = yuvi420[:ih, :iw]
    U = yuvi420[ih:ih * 5 // 4, :].reshape(ih // 2, iw // 2)
    V = yuvi420[ih * 5 // 4:, :].reshape(ih // 2, iw // 2)
    return Y, U, V

def yuv1d2rgb(yuv1d):
    if yuv1d == None:
        return None
    yuv_matrix = np.frombuffer(yuv1d, dtype=np.uint8, count=int(height * width * 1.5), offset=0)
    yuv_matrix = yuv_matrix.reshape(int(height * 3 / 2), width)
    # rgb_frame = cv2.cvtColor(yuv_matrix, cv2.COLOR_YUV2RGB_I420)
    rgb_frame = cv2.cvtColor(yuv_matrix, cv2.COLOR_YUV2BGR_I420)
    return rgb_frame


fourcc = cv2.VideoWriter_fourcc('R','G','B','A')
vid_out = cv2.VideoWriter(vid_out_name, fourcc, fps, (width, height))
yuv_size = os.path.getsize(yuv_path)
total_frame = int(yuv_size/frame_size)
print("total_frame:", total_frame)

Two_yuv_files = "./result/Two_yuv.yuv"
Two_fd = open(Two_yuv_files, "wb")


with open(yuv_path, 'rb') as fp:
    for i in range(total_frame):
        data_bytes = fp.read(int(width * height * 1.5))
        frame = yuv1d2rgb(data_bytes)
        # Y, U, V = bgr_to_yuv420p(frame)
        # Two_fd.write(Y)
        # Two_fd.write(U)
        # Two_fd.write(V)
        # cv2.namedWindow("frame0")
        # cv2.imshow("frame0", frame)
        # cv2.waitKey(0)
        vid_out.write(frame[:, :, ::-1])
        
# with open(yuv_path, 'rb') as fp:
#     for i in range(total_frame):
#         data_bytes = fp.read(int(width*height*1.5))
#         output_bytes = output_fd.read(int(width*height*1.5))
#         # ori = np.frombuffer(data_bytes, dtype=np.uint8, count=int(height * width * 1.5), offset=0)
#         # out = np.frombuffer(output_bytes, dtype=np.uint8, count=int(height * width * 1.5), offset=0)
#         print(len(data_bytes))
#         frame = yuv1d2rgb(data_bytes)
#         # np.save(f"{i}.npy", frame)
#         vid_out.write(frame[:, :, ::-1])
#
# output_fd.close()

    # cv2.imwrite("frame0.bmp",frame)
