## CLCC

### train2Remote.py

 训练主函数

调用关系：`train2Remote.py` -> `rtc_env.py` -> `gymStat.py`

#### rtc_env.py

`rtc_env.py` 中间层文件，从`gymStat`获取RTC跑出来的状态信息给`train2Remote.py`reward，state和action。

状态主要由两个部分，包级来自于`CLCC/packet_record.py`，帧级来自于`rtcGym/alphartc_gym/utils/ProcessStat.py`。

包级的获取很简单不多讲

主要讲讲帧级的

######  ProcessStat.py

通过processStat函数，接收stat（gymStat.py内会讲），处理帧信息，再通过gotState函数生成state。

#### gymStat.py

管理RTC进程，负责跟RTC进程交互，从RTC获取状态，并把新的bitrate发送给RTC。获取和发送通过pipe实现。

gymStat通过调用`peerconnection.py`的appRecvProxy和appSendProxy来创建RTC进程。

###### peerconnection.py

以appRecvProxy函数为例，通过subprocess创建进程，使用`processR`函数接收RTC的stdout并处理。appSendProxy同理。

#### runInRemote.py

通过这个函数在hosts开启RTC进程并进行训练采样。

### peerconnection_serverless2.py

跑单次RTC用的代码，只可用于运行GCC和HRCC

内部函数与`peerconnection.py`内部基本相同，`peerconnection.py`内部的函数就是从`peerconnection_serverless2.py`里面来的，两者函数上有略微的区别。

其实可以弄成一个文件，但是之后再说吧。

### bitRateAnalysis2.py

根据trace和当前的send.txt和recv.txt画出这次的trace线。

### tests/testGccHrcc.py & tests_trace/testGccHrcc.py

测试文件，前者用于测试random trace，后者用于测试LTEtrace。

通过`testCC`函数来完成一个拥塞控制cc的整轮测试。`testCC`函数内部会根据cc类型选择调用`peerconnection_serverless2.run`函数还是` testTrain_traces.testTrain`函数，前者用于测试GCC和HRCC，后者用于测试CLCC和其他强化学习算法。

在测试结束后，使用TestReult中的plotQoEVmaf.py画QoE，用groupAvg.py画average performance图，用drawCompeteTrace.py把每个trace线画出来。所有带Ablation的都是用于测试CLCC的消融实验的。

其实我还是建议测试脚本最好自己写，不容易出问题，也知道每个东西都是啥。



## 工具类

### mahiTraces/makexxxxxxTraces.py

用于生成mahiTraces，具体参数在py文件开头设置。

### delayTools/

画RTC中的一些延迟，主要用来测试代码有没有一些写的不好的地方导致出现很大的延迟。

用的最多的就是delayTools/gotBWETime.py，直接画出来每次获取bwe用的时间。

### scpToRemote.py

把一些文件复制给远处的distributed hosts

### scpTestMedia.py

把testMedia里面的视频复制给distributed hosts

### dockers/xxx.py

用于在distributed hosts上，对每个docker环境同步



## AlphaRTC

就一个文件要讲，用来改完代码后编译并把新的peerconnection_serverless.origin复制到AlphaRTCNoDocker里面。

### compile.sh

编译RTC，并复制到指定路径下。
