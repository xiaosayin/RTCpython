import sys
import os
import subprocess
import paramiko
import time
import pickle
import torch

def runInRemote(localPath, remotePath, remoteip, remoteid, remotePSword, this_exploration_param):
    remoteI = 0
    sshList = []
    sshInList = []
    sshOutList = []
    sshErrList = []
    while remoteI < len(remotePath):
        expf = open(f"{localPath}exp.txt", "w")
        expf.write(f"{this_exploration_param}")
        expf.close()
        print('sshpass -p %s scp %sdocker_pth %s@%s:%sremoteFiles' %(remotePSword[remoteI], localPath, remoteid[remoteI], remoteip[remoteI], remotePath[remoteI]))   #local to remote

        os.system('sshpass -p %s scp %sdocker_pth %s@%s:%sremoteFiles' %(remotePSword[remoteI], localPath, remoteid[remoteI], remoteip[remoteI], remotePath[remoteI]))   #local to remote
        os.system('sshpass -p %s scp %sexp.txt %s@%s:%sremoteFiles' %(remotePSword[remoteI], localPath, remoteid[remoteI], remoteip[remoteI], remotePath[remoteI]))   #local to remote
        print("calling")
        sshList.append(paramiko.SSHClient())
        #ssh = paramiko.SSHClient()
        sshList[remoteI].set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshList[remoteI].connect(hostname=remoteip[remoteI], username=remoteid[remoteI], password=remotePSword[remoteI])
        if remoteip[remoteI] == "172.16.6.104":
            print("bianma server")
            ssh_stdin, ssh_stdout, ssh_stderr = sshList[remoteI].exec_command(f"cd {remotePath[remoteI]} && \
                            export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && \
                            python3 runInDocker.py > log/runInDocker.txt")

        else:
            ssh_stdin, ssh_stdout, ssh_stderr = sshList[remoteI].exec_command(f"cd {remotePath[remoteI]} && \
                            export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && \
                            python3 trainRemote.py > log/trainRemote.txt")

        #ssh_stdin, ssh_stdout, ssh_stderr = sshList[remoteI].exec_command("ping -c 100 www.baidu.com")
        sshInList.append(ssh_stdin)
        sshOutList.append(ssh_stdout)
        sshErrList.append(ssh_stderr)
        print(f"start to ping {round(time.time()* 1000000)}\n")
        remoteI += 1

    startTime = round(time.time())
    remoteI = 0
    while remoteI < len(remotePath):
        print(f"trying remote{remoteI}")
        out,err = sshOutList[remoteI].read(), sshErrList[remoteI].read()
        print(out)
        print("docker done")
        print(f"ping ended {round(time.time()* 1000000)}\n")
        os.system('sshpass -p %s scp %s@%s:%sremoteFiles/storagePickle  %sstorage%s ' %(remotePSword[remoteI], remoteid[remoteI], remoteip[remoteI], remotePath[remoteI], localPath, remoteI))   #local to remote
        sshList[remoteI].close()
        remoteI += 1

    print("waited: ", round(time.time()) - startTime)

def catStorage(localPath, storage):
    lastT = round(time.time() * 1000)
    ls = os.listdir(localPath)
    for f in ls:
        if 'storage' in f:
            f1 = open(localPath + f, 'rb')
            print(f"catting {f}")
            try:
                storage1 = pickle.load(f1)
            except EOFError:
                print("EOFError: Ran out of input!")
            f1.close()
            # print("length: ", len(storage1.rewards))
            # print("rewards: ", storage1.rewards)
            # if len(storage1.rewards) > 420:
                # print(storage1.is_terminals[-1])
                # continue
            storage.cat_Storage(storage1)
            torch.stack(storage.actions)

    print(f"cat used {round(time.time() * 1000) - lastT}ms")
    return storage


def main():
    # localPath = f'/home/koyong/RTC/AlphaRTCNoDocker/localFiles/'
    localPath = f'/home/yinwenpei/RTCPython/localFiles/'
    # remotePath = [f'/home/tony/KoyongRTC/AlphaRTCNoDocker/']#, f'/home/koyong/AlphaRTCNoDocker/']
    remotePath = [f'/home/yinwenpei/RTCPython/']
    # remoteip = ['172.16.6.117']#, '172.16.6.198']
    remoteip = ['172.16.6.104']
    remoteid = ['yinwenpei']#, 'koyong']
    # remotePSword = ['555888']#, '1']
    remotePSword = ['medialab2022']
    runInRemote(localPath, remotePath, remoteip, remoteid, remotePSword, 0.6)

if __name__ == "__main__":
    main()
