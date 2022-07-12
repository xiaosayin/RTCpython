# usage: this py is used to write gotAllPathDelay.py

##============================================================
## from request to gotBWE in RTC
#plt.cla()
#processR_pc_got_bweT = []
#i = 0
#while i < len(processR_pc_got_bwe) and i < len(gymstat_sent_bwe_to_appRecv):
#    processR_pc_got_bweT.append(processR_pc_got_bwe[i] - gymstat_sent_bwe_to_appRecv[i])
#    i += 1
#plt.plot(range(len(processR_pc_got_bweT)), processR_pc_got_bweT, label='processR_pc_got_bweT', color = 'red')
#plt.grid()
#plt.legend()
#plt.savefig("allPathDelay/processR_pc_got_bweT.jpg")
##============================================================

allPath = ["RTCrequest", "processR_got_request", "processR_allFrame", \
            "processR_sent_asking_for_bwe", "processR_sent_estimator_stat", "gymstat_recved_string", \
            "gymstat_recved_estimator_stat", "rtcenv_sorted_packlist", "rtcenv_processed_packlist", \
            "rtcenv_processed_state02", "rtcenv_processed_state35", "rtcenv_linear_to_log",\
            "train_state_clone_detach", "ppoagent_FloatTensor_reshape", "ppo_agent_policy_old_forwarded", \
            "rtc_env_log_to_linear_action", "gymstat_sent_bwe_to_appRecv", "processR_pc_got_bwe", "RTCgotBWE"]

allPath = ["RTCrequest", "processR_got_request", "processR_allFrame", \
            "processR_sent_asking_for_bwe", "processR_sent_estimator_stat", "gymstat_recved_string", \
            "gymstat_recved_estimator_stat", "rtcenv_sorted_packlist", "rtcenv_processed_packlist", \
            "rtcenv_processed_state02", "rtcenv_processed_state35", "rtcenv_linear_to_log",\
            "train_state_clone_detach", "ppoagent_FloatTensor_reshape", "ppo_agent_policy_old_forwarded", \
            "rtc_env_log_to_linear_action", "gymstat_sent_bwe_to_appRecv", "processR_pc_got_bwe", "RTCgotBWE"]

allPathLine = ["RTCrequest", "got request at ", "processed allFrame at ", \
            "sent 'asking for bwe' at ", "sent [estimator, stat] at ", "recved string at ", \
            "recved [self.estimator, stat] at ", "sorted packlist at ", "processed packlist at ", \
            "processed state0-2 at ", "processed state3-5 at ", "linear_to_log at ",\
            "state_clone_detach at ", "FloatTensor_reshaped at ", "policy_old.forwarded at ", \
            "log_to_linear action at ", "sent bwe to appRecv at ", "pc got bwe at ", "RTCgotBWE"]

tmpAllPath = open("tmpAll.py", "w")
i = len(allPath) - 1
j = 1
while i >= 1:
    tmpAllPath.write("##============================================================\n")
    tmpAllPath.write("plt.cla()\n")
    tmpAllPath.write(f"{allPath[i]}T = []\n")
    tmpAllPath.write("i = 0\n")
    tmpAllPath.write(f"while i < len({allPath[i]}) and i < len({allPath[i - 1]}):\n")
    tmpAllPath.write(f"\t{allPath[i]}T.append({allPath[i]}[i] - {allPath[i - 1]}[i])\n")
    tmpAllPath.write("\ti += 1\n")
    tmpAllPath.write(f"plt.plot(range(len({allPath[i]}T)), {allPath[i]}T, label='{allPath[i]}T', color = 'red')\n")
    tmpAllPath.write("plt.grid()\n")
    tmpAllPath.write("plt.legend()\n")
    tmpAllPath.write(f"plt.savefig('allPathDelay/{j}{allPath[i]}T.jpg')\n")
    tmpAllPath.write("##============================================================\n")
    i -= 1
    j += 1
    



tmpAllPath2 = open("tmpAll2.py", "w")
tmpAllPath2.write("trainf = open('log/train.txt', 'r')\n")
tmpAllPath2.write("trainLine = trainf.readline()\n")
i = len(allPath) - 2
while i >= 1:
    tmpAllPath2.write(f"{allPath[i]} = []\n")
    tmpAllPath2.write(f"{allPath[i]}Line = \"{allPathLine[i]}\"\n")
    i -= 1
tmpAllPath2.write("while trainLine:\n")

i = len(allPath) - 2
while i >= 1:
    tmpAllPath2.write(f"\tif {allPath[i]}Line in trainLine:\n")
    tmpAllPath2.write(f"\t\t{allPath[i]}.append(int(trainLine[trainLine.index({allPath[i]}Line) + len({allPath[i]}Line):]))\n")
    i -= 1
tmpAllPath2.write("\ttrainLine = trainf.readline()\n")   
    