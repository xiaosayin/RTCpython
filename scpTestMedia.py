# copy the videos to the remote hosts

from ast import parse
import os
import paramiko


def main():
    fileList = []
               
                #, \
                #"testTrain.py",\
                #"test_rtc_env.py"]
                #'''
    folderList = ["testmedia/"]

    localPath = f'/home/koyong/RTC/AlphaRTCNoDocker/'
    remotePath = [#f'/home/tony/KoyongRTC/AlphaRTCNoDocker/', \
                f'/home/koyong/AlphaRTCNoDocker/',\
                 f'/home/racheal/KoyongRTC/AlphaRTCNoDocker/', f'/home/yuanjinghao/KoyongRTC/AlphaRTCNoDocker/']
    remoteip = [#'172.16.6.117',\
                 '172.16.6.104', '172.16.6.164', '172.16.6.165']
    remoteid = [#'tony', \
                'koyong', 'racheal', 'yuanjinghao']
    remotePSword = [#'555888',\
                     '1', '010203', '9375']
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
            print(f"sshpass -p {remotePSword[i]} scp {localPath + filepath + filename} \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + filepath}")
            os.system(f"sshpass -p {remotePSword[i]} scp {localPath + filepath + filename} \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + filepath}")
            i += 1

    for fold in folderList:
        i = 0
        while i < len(remotePath):
            print(f"sshpass -p {remotePSword[i]} \scp -r {localPath + fold}* \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + fold}")
            os.system(f"sshpass -p {remotePSword[i]} \scp -r {localPath + fold}* \
                    {remoteid[i]}@{remoteip[i]}:{remotePath[i] + fold}")
            i += 1

def sync104Dock():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.16.6.104', username='koyong', password='1')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"cd /home/koyong/AlphaRTCNoDocker/ && \
                    python3 dockers/syncTestMedia.py")
    out,err = ssh_stdout.read(), ssh_stderr.read()
    print(out)

if __name__ == '__main__':
    main()