ARG IMAGE_NAME=nvidia/cuda
FROM ${IMAGE_NAME}:11.4.2-runtime-ubuntu20.04 as base

FROM base as base-amd64

ENV NV_CUDNN_VERSION 8.2.4.15

ENV NV_CUDNN_PACKAGE "libcudnn8=$NV_CUDNN_VERSION-1+cuda11.4"
ENV NV_CUDNN_PACKAGE_NAME "libcudnn8"

FROM base-amd64

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"
LABEL com.nvidia.cudnn.version="${NV_CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    ${NV_CUDNN_PACKAGE} \
    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y sudo

RUN apt-get update && apt-get install -y iproute2

RUN apt-get update && apt-get install -y iputils-ping

RUN sudo apt-get update -y && sudo apt-get install software-properties-common -y

RUN sudo add-apt-repository ppa:deadsnakes/ppa -y

RUN sudo apt-get install python3 -y

RUN sudo apt-get install python3-pip -y

RUN pip install torch -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

RUN pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

RUN pip install matplotlib

RUN pip install gym

RUN pip install psutil

RUN sudo apt-get update -y && sudo apt-get install ffmpeg -y

RUN sudo add-apt-repository ppa:keithw/mahimahi

RUN sudo apt-get update

RUN sudo apt-get install mahimahi

RUN groupadd --gid 5000 newuser \
    && useradd --home-dir /home/newuser --create-home --uid 5000 \
        --gid 5000 --shell /bin/sh --skel /dev/null newuser