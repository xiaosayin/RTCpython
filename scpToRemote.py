# copy the files and folders to the remote hosts

from ast import parse
import os
import paramiko


def main():
    fileList = ["rtc_env.py", "trainRemote.py", \
                "rtcGym/alphartc_gym/peerconnection.py", \
                "CLCC/ProcessStat.py",\
                "rtcGym/alphartc_gym/gymStat.py" ,\
                "CLCC/RL/ppo_agent.py" ,\
                "CLCC/RL/actor_critic.py",\
                "bitRateAnalysis2.py",\
                "CLCC/packet_record.py",\
                "6mbps.trace",\
                "scpToRemote.py",\
                "dockers/syncDockers.py",\
                "dockers/syncTestMedia.py",\
                "dockers/resetDockers.py",\
                "runInDocker.py",\
                "CLCC/RL/storage.py",\
                "peerconnection_serverless2.py",\
                "peerconnection_serverless.origin", \
                "allDelay.py",\
                "info.py",\
                "drawMahiRate.py",\
                "plotResult.py",\
                "tests/getAvgTraceBW.py",\
                "CLCC/RL/ppo_agent.py"]
               
                #, \
                #"testTrain.py",\
                #"test_rtc_env.py"]
                #'''
    # folderList = ["rtcGym/alphartc_gym/shs_45s/"]
    folderList = []
    
    '''
    folderList = ["mahiTraces/",\
                "rtcGym/alphartc_gym/"
                    ]
    '''

    # localPath = f'/home/koyong/RTC/AlphaRTCNoDocker/'
    localPath = f'/home/yinwenpei/RTCPython/'
    # remotePath = [#f'/home/tony/KoyongRTC/AlphaRTCNoDocker/', \
    #             f'/home/koyong/AlphaRTCNoDocker/']#,\
    remotePath = [f'/home/yinwenpei/RTCPython/']
    remoteip = [#'172.16.6.117',\
                 '172.16.6.104']#, '172.16.6.164', '172.16.6.165']
    remoteid = ['yinwenpei']
               # 'koyong']#, 'racheal', 'yuanjinghao']
    # remotePSword = [#'555888',\
    #                  '1']#, '010203', '9375']
    remotePSword = ['medialab2022']
    scpToRemote(fileList, folderList, localPath, remotePath, remoteip, remoteid, remotePSword)
    sync104Dock()


def scpToRemote(fileList, folderList, localPath, remotePath, remoteip, remoteid, remotePSword):
    for file in fileList:
        i = 0
        pathParse = None
        while i < len(file):
            if file[i] == '/':
                pathParse = i
            i += 1
        if pathParse != None:
            filepath = file[:pathParse+1]
            filename = file[pathParse+1:]
        else:
            filepath = ''
            filename = file

        print("filepath, filename:", filepath, filename)

        i = 0
        while i < len(remotePath):
            mkdirCmd = f"echo {remotePSword[i]} | ssh {remoteid[i]}@{remoteip[i]} 'mkdir {remotePath[i] + filepath}'"
            print(mkdirCmd)
            os.system(mkdirCmd)
            scpFileCmd = f"sshpass -p {remotePSword[i]} scp {localPath + filepath + filename} \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + filepath}"
            print(scpFileCmd)
            os.system(scpFileCmd)
            i += 1

    for fold in folderList:
        i = 0
        while i < len(remotePath):
            scpFoldCmd = f"sshpass -p {remotePSword[i]} scp -r {localPath + fold}* \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + fold}"
            print(scpFoldCmd)
            os.system(scpFoldCmd)
            i += 1

def sync104Dock():  #used to sync the files in the dockers on the A6000 server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.16.6.104', username='yinwenpei', password='medialab2022')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"cd /home/yinwenpei/RTCPython/ && \
                    python3 dockers/syncDockers.py")
    out,err = ssh_stdout.read(), ssh_stderr.read()
    print(out)

if __name__ == '__main__':
    main()