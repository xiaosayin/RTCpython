#similar tool to findHiddenDelay.py

import matplotlib.pyplot as plt
'''
allPath = [RTCrequest, processR_got_request, processR_allFrame, \
            processR_sent_asking_for_bwe, processR_sent_estimator_stat, gymstat_recved_string, \
            gymstat_recved_estimator_stat, rtcenv_sorted_packlist, rtcenv_processed_packlist, \
            rtcenv_processed_state02, rtcenv_processed_state35, rtcenv_linear_to_log,\
            train_state_clone_detach, ppoagent_FloatTensor_reshape, ppo_agent_policy_old_forwarded, \
            rtc_env_log_to_linear_action, gymstat_sent_bwe_to_appRecv, processR_pc_got_bwe, RTCgotBWE]'''

recvf = open("log/recv.txt", 'r')
recvLine = recvf.readline()
RTCrequest = []
RTCgotBWE = []
RTCrequestLine = "KOYONYONG: RequestForBandwidth atTime: "
RTCgotBWELine = "KOYONYONG: got BWE atTime: "
while recvLine:
    if RTCrequestLine in recvLine:
        RTCrequest.append(int(recvLine[recvLine.index(RTCrequestLine) + len(RTCrequestLine):])//1000)
    if RTCgotBWELine in recvLine:
        RTCgotBWE.append(int(recvLine[recvLine.index(RTCgotBWELine) + len(RTCgotBWELine):])//1000)
    recvLine = recvf.readline()

trainf = open('log/train.txt', 'r')
trainLine = trainf.readline()
processR_pc_got_bwe = []
processR_pc_got_bweLine = "pc got bwe at "
gymstat_sent_bwe_to_appRecv = []
gymstat_sent_bwe_to_appRecvLine = "sent bwe to appRecv at "
rtc_env_log_to_linear_action = []
rtc_env_log_to_linear_actionLine = "log_to_linear action at "
ppo_agent_policy_old_forwarded = []
ppo_agent_policy_old_forwardedLine = "policy_old.forwarded at "
ppoagent_FloatTensor_reshape = []
ppoagent_FloatTensor_reshapeLine = "FloatTensor_reshaped at "
train_state_clone_detach = []
train_state_clone_detachLine = "state_clone_detach at "
rtcenv_linear_to_log = []
rtcenv_linear_to_logLine = "linear_to_log at "
rtcenv_processed_state35 = []
rtcenv_processed_state35Line = "processed state3-5 at "
rtcenv_processed_state02 = []
rtcenv_processed_state02Line = "processed state0-2 at "
rtcenv_processed_packlist = []
rtcenv_processed_packlistLine = "processed packlist at "
rtcenv_sorted_packlist = []
rtcenv_sorted_packlistLine = "sorted packlist at "
gymstat_recved_estimator_stat = []
gymstat_recved_estimator_statLine = "recved [self.estimator, stat] at "
gymstat_recved_string = []
gymstat_recved_stringLine = "recved string at "
processR_sent_estimator_stat = []
processR_sent_estimator_statLine = "sent [estimator, stat] at "
processR_sent_asking_for_bwe = []
processR_sent_asking_for_bweLine = "sent 'asking for bwe' at "
processR_allFrame = []
processR_allFrameLine = "processed allFrame at "
processR_got_request = []
processR_got_requestLine = "got request at "
while trainLine:
	if processR_pc_got_bweLine in trainLine:
		processR_pc_got_bwe.append(int(trainLine[trainLine.index(processR_pc_got_bweLine) + len(processR_pc_got_bweLine):]))
	if gymstat_sent_bwe_to_appRecvLine in trainLine:
		gymstat_sent_bwe_to_appRecv.append(int(trainLine[trainLine.index(gymstat_sent_bwe_to_appRecvLine) + len(gymstat_sent_bwe_to_appRecvLine):]))
	if rtc_env_log_to_linear_actionLine in trainLine:
		rtc_env_log_to_linear_action.append(int(trainLine[trainLine.index(rtc_env_log_to_linear_actionLine) + len(rtc_env_log_to_linear_actionLine):]))
	if ppo_agent_policy_old_forwardedLine in trainLine:
		ppo_agent_policy_old_forwarded.append(int(trainLine[trainLine.index(ppo_agent_policy_old_forwardedLine) + len(ppo_agent_policy_old_forwardedLine):]))
	if ppoagent_FloatTensor_reshapeLine in trainLine:
		ppoagent_FloatTensor_reshape.append(int(trainLine[trainLine.index(ppoagent_FloatTensor_reshapeLine) + len(ppoagent_FloatTensor_reshapeLine):]))
	if train_state_clone_detachLine in trainLine:
		train_state_clone_detach.append(int(trainLine[trainLine.index(train_state_clone_detachLine) + len(train_state_clone_detachLine):]))
	if rtcenv_linear_to_logLine in trainLine:
		rtcenv_linear_to_log.append(int(trainLine[trainLine.index(rtcenv_linear_to_logLine) + len(rtcenv_linear_to_logLine):]))
	if rtcenv_processed_state35Line in trainLine:
		rtcenv_processed_state35.append(int(trainLine[trainLine.index(rtcenv_processed_state35Line) + len(rtcenv_processed_state35Line):]))
	if rtcenv_processed_state02Line in trainLine:
		rtcenv_processed_state02.append(int(trainLine[trainLine.index(rtcenv_processed_state02Line) + len(rtcenv_processed_state02Line):]))
	if rtcenv_processed_packlistLine in trainLine:
		rtcenv_processed_packlist.append(int(trainLine[trainLine.index(rtcenv_processed_packlistLine) + len(rtcenv_processed_packlistLine):]))
	if rtcenv_sorted_packlistLine in trainLine:
		rtcenv_sorted_packlist.append(int(trainLine[trainLine.index(rtcenv_sorted_packlistLine) + len(rtcenv_sorted_packlistLine):]))
	if gymstat_recved_estimator_statLine in trainLine:
		gymstat_recved_estimator_stat.append(int(trainLine[trainLine.index(gymstat_recved_estimator_statLine) + len(gymstat_recved_estimator_statLine):]))
	if gymstat_recved_stringLine in trainLine:
		gymstat_recved_string.append(int(trainLine[trainLine.index(gymstat_recved_stringLine) + len(gymstat_recved_stringLine):]))
	if processR_sent_estimator_statLine in trainLine:
		processR_sent_estimator_stat.append(int(trainLine[trainLine.index(processR_sent_estimator_statLine) + len(processR_sent_estimator_statLine):]))
	if processR_sent_asking_for_bweLine in trainLine:
		processR_sent_asking_for_bwe.append(int(trainLine[trainLine.index(processR_sent_asking_for_bweLine) + len(processR_sent_asking_for_bweLine):]))
	if processR_allFrameLine in trainLine:
		processR_allFrame.append(int(trainLine[trainLine.index(processR_allFrameLine) + len(processR_allFrameLine):]))
	if processR_got_requestLine in trainLine:
		processR_got_request.append(int(trainLine[trainLine.index(processR_got_requestLine) + len(processR_got_requestLine):]))
	trainLine = trainf.readline()


allPathT = []
i = 0
while i < len(RTCgotBWE) and i < len(RTCrequest):
	allPathT.append(RTCgotBWE[i] - RTCrequest[i])
	i += 1
plt.plot(range(len(allPathT)), allPathT, label='RTCgotBWET', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/00allPathT.jpg')
##============================================================
plt.cla()
RTCgotBWET = []
i = 0
while i < len(RTCgotBWE) and i < len(processR_pc_got_bwe):
	RTCgotBWET.append(RTCgotBWE[i] - processR_pc_got_bwe[i])
	print([RTCgotBWE[i] ,  processR_pc_got_bwe[i]])
	i += 1
plt.plot(range(len(RTCgotBWET)), RTCgotBWET, label='RTCgotBWET', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/1RTCgotBWET.jpg')

for i in RTCgotBWET:
    print(i)
##============================================================
##============================================================
plt.cla()
processR_pc_got_bweT = []
i = 0
while i < len(processR_pc_got_bwe) and i < len(gymstat_sent_bwe_to_appRecv):
	processR_pc_got_bweT.append(processR_pc_got_bwe[i] - gymstat_sent_bwe_to_appRecv[i])
	i += 1
plt.plot(range(len(processR_pc_got_bweT)), processR_pc_got_bweT, label='processR_pc_got_bweT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/2processR_pc_got_bweT.jpg')
##============================================================
##============================================================
plt.cla()
gymstat_sent_bwe_to_appRecvT = []
i = 0
while i < len(gymstat_sent_bwe_to_appRecv) and i < len(rtc_env_log_to_linear_action):
	gymstat_sent_bwe_to_appRecvT.append(gymstat_sent_bwe_to_appRecv[i] - rtc_env_log_to_linear_action[i])
	i += 1
plt.plot(range(len(gymstat_sent_bwe_to_appRecvT)), gymstat_sent_bwe_to_appRecvT, label='gymstat_sent_bwe_to_appRecvT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/3gymstat_sent_bwe_to_appRecvT.jpg')
##============================================================
##============================================================
plt.cla()
rtc_env_log_to_linear_actionT = []
i = 0
while i < len(rtc_env_log_to_linear_action) and i < len(ppo_agent_policy_old_forwarded):
	rtc_env_log_to_linear_actionT.append(rtc_env_log_to_linear_action[i] - ppo_agent_policy_old_forwarded[i])
	i += 1
plt.plot(range(len(rtc_env_log_to_linear_actionT)), rtc_env_log_to_linear_actionT, label='rtc_env_log_to_linear_actionT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/4rtc_env_log_to_linear_actionT.jpg')
##============================================================
##============================================================
plt.cla()
ppo_agent_policy_old_forwardedT = []
i = 0
while i < len(ppo_agent_policy_old_forwarded) and i < len(ppoagent_FloatTensor_reshape):
	ppo_agent_policy_old_forwardedT.append(ppo_agent_policy_old_forwarded[i] - ppoagent_FloatTensor_reshape[i])
	i += 1
plt.plot(range(len(ppo_agent_policy_old_forwardedT)), ppo_agent_policy_old_forwardedT, label='ppo_agent_policy_old_forwardedT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/5ppo_agent_policy_old_forwardedT.jpg')
##============================================================
##============================================================
plt.cla()
ppoagent_FloatTensor_reshapeT = []
i = 0
while i < len(ppoagent_FloatTensor_reshape) and i < len(train_state_clone_detach):
	ppoagent_FloatTensor_reshapeT.append(ppoagent_FloatTensor_reshape[i] - train_state_clone_detach[i])
	i += 1
plt.plot(range(len(ppoagent_FloatTensor_reshapeT)), ppoagent_FloatTensor_reshapeT, label='ppoagent_FloatTensor_reshapeT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/6ppoagent_FloatTensor_reshapeT.jpg')
##============================================================
##============================================================
plt.cla()
train_state_clone_detachT = []
i = 0
while i < len(train_state_clone_detach) and i < len(rtcenv_linear_to_log):
	train_state_clone_detachT.append(train_state_clone_detach[i] - rtcenv_linear_to_log[i])
	i += 1
plt.plot(range(len(train_state_clone_detachT)), train_state_clone_detachT, label='train_state_clone_detachT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/7train_state_clone_detachT.jpg')
##============================================================
##============================================================
plt.cla()
rtcenv_linear_to_logT = []
i = 0
while i < len(rtcenv_linear_to_log) and i < len(rtcenv_processed_state35):
	rtcenv_linear_to_logT.append(rtcenv_linear_to_log[i] - rtcenv_processed_state35[i])
	i += 1
plt.plot(range(len(rtcenv_linear_to_logT)), rtcenv_linear_to_logT, label='rtcenv_linear_to_logT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/8rtcenv_linear_to_logT.jpg')
##============================================================
##============================================================
plt.cla()
rtcenv_processed_state35T = []
i = 0
while i < len(rtcenv_processed_state35) and i < len(rtcenv_processed_state02):
	rtcenv_processed_state35T.append(rtcenv_processed_state35[i] - rtcenv_processed_state02[i])
	i += 1
plt.plot(range(len(rtcenv_processed_state35T)), rtcenv_processed_state35T, label='rtcenv_processed_state35T', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/9rtcenv_processed_state35T.jpg')
##============================================================
##============================================================
plt.cla()
rtcenv_processed_state02T = []
i = 0
while i < len(rtcenv_processed_state02) and i < len(rtcenv_processed_packlist):
	rtcenv_processed_state02T.append(rtcenv_processed_state02[i] - rtcenv_processed_packlist[i])
	i += 1
plt.plot(range(len(rtcenv_processed_state02T)), rtcenv_processed_state02T, label='rtcenv_processed_state02T', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/10rtcenv_processed_state02T.jpg')
##============================================================
##============================================================
plt.cla()
rtcenv_processed_packlistT = []
i = 0
while i < len(rtcenv_processed_packlist) and i < len(rtcenv_sorted_packlist):
	rtcenv_processed_packlistT.append(rtcenv_processed_packlist[i] - rtcenv_sorted_packlist[i])
	i += 1
plt.plot(range(len(rtcenv_processed_packlistT)), rtcenv_processed_packlistT, label='rtcenv_processed_packlistT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/11rtcenv_processed_packlistT.jpg')
##============================================================
##============================================================
plt.cla()
rtcenv_sorted_packlistT = []
gymstat_recved_estimator_stat.pop(0)
i = 0
while i < len(rtcenv_sorted_packlist) and i < len(gymstat_recved_estimator_stat):
	rtcenv_sorted_packlistT.append(rtcenv_sorted_packlist[i] - gymstat_recved_estimator_stat[i])
	i += 1
plt.plot(range(len(rtcenv_sorted_packlistT)), rtcenv_sorted_packlistT, label='rtcenv_sorted_packlistT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/12rtcenv_sorted_packlistT.jpg')
##============================================================
##============================================================
plt.cla()
gymstat_recved_estimator_statT = []
i = 0
while i < len(gymstat_recved_estimator_stat) and i < len(gymstat_recved_string):
	gymstat_recved_estimator_statT.append(gymstat_recved_estimator_stat[i] - gymstat_recved_string[i])
	i += 1
plt.plot(range(len(gymstat_recved_estimator_statT)), gymstat_recved_estimator_statT, label='gymstat_recved_estimator_statT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/13gymstat_recved_estimator_statT.jpg')
##============================================================
##============================================================
plt.cla()
gymstat_recved_stringT = []
i = 0
while i < len(gymstat_recved_string) and i < len(processR_sent_estimator_stat):
	gymstat_recved_stringT.append(gymstat_recved_string[i] - processR_sent_estimator_stat[i])
	i += 1
plt.plot(range(len(gymstat_recved_stringT)), gymstat_recved_stringT, label='gymstat_recved_stringT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/14gymstat_recved_stringT.jpg')
##============================================================
##============================================================
plt.cla()
processR_sent_estimator_statT = []
i = 0
while i < len(processR_sent_estimator_stat) and i < len(processR_sent_asking_for_bwe):
	processR_sent_estimator_statT.append(processR_sent_estimator_stat[i] - processR_sent_asking_for_bwe[i])
	i += 1
plt.plot(range(len(processR_sent_estimator_statT)), processR_sent_estimator_statT, label='processR_sent_estimator_statT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/15processR_sent_estimator_statT.jpg')
##============================================================
##============================================================
plt.cla()
processR_sent_asking_for_bweT = []
i = 0
while i < len(processR_sent_asking_for_bwe) and i < len(processR_allFrame):
	processR_sent_asking_for_bweT.append(processR_sent_asking_for_bwe[i] - processR_allFrame[i])
	i += 1
plt.plot(range(len(processR_sent_asking_for_bweT)), processR_sent_asking_for_bweT, label='processR_sent_asking_for_bweT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/16processR_sent_asking_for_bweT.jpg')
##============================================================
##============================================================
plt.cla()
processR_allFrameT = []
i = 0
while i < len(processR_allFrame) and i < len(processR_got_request):
	processR_allFrameT.append(processR_allFrame[i] - processR_got_request[i])
	i += 1
plt.plot(range(len(processR_allFrameT)), processR_allFrameT, label='processR_allFrameT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/17processR_allFrameT.jpg')
##============================================================
##============================================================
plt.cla()
processR_got_requestT = []
i = 0
while i < len(processR_got_request) and i < len(RTCrequest):
	processR_got_requestT.append(processR_got_request[i] - RTCrequest[i])
	i += 1
plt.plot(range(len(processR_got_requestT)), processR_got_requestT, label='processR_got_requestT', color = 'red')
plt.grid()
plt.legend()
plt.savefig('allPathDelay/18processR_got_requestT.jpg')
##============================================================
