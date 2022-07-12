import sys
import os
import subprocess
import pickle
import time
#user: koyong
#gid: 1000
cudaList = [1, 2, 3]
dockList = [0, 1, 2, 3, 4]
dockerPath = "/home/koyong/DockerRTC/"
localIP = "172.16.6.123"
localPath = "/home/koyong/RTC/AlphaRTCNoDocker/localFiles"
localUsr = "koyong"
localpsword = "1"
#catf = open("log/catInDocker.txt", "a")
def cpPthExp():
    for cuda in cudaList:
        for dock in dockList:
            cpCmd = f"cp remoteFiles/docker_pth {dockerPath}cuda{cuda}/docker{dock}/remoteFiles/"
            os.system(cpCmd)
            cpCmd = f"cp remoteFiles/exp.txt {dockerPath}cuda{cuda}/docker{dock}/remoteFiles/"
            os.system(cpCmd)

def runInDocker():
    print("calling")
    dockers = []
    for cuda in cudaList:
        for dock in dockList:
            dockerCmd = f"echo '1' | sudo -S docker run --rm -u koyong:1000 -v {dockerPath}cuda{cuda}/docker{dock}/:/RTC -w '/RTC' -e LD_LIBRARY_PATH=/RTC/lib --gpus all --privileged=true cuda_mahi sh trainRemote.sh"

            app = subprocess.Popen(
                    dockerCmd,
                    shell=True,

                    bufsize=1,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
            dockers.append(app)

    for d in dockers:
        d.wait()
        line = d.stdout.readline()
        while line:
            line = line.decode("utf-8")
            print(line)
            line = d.stdout.readline()
        print(f"docker{d} done")
    print("All dockers done!")

def catDockerStorage():
    lastT = round(time.time() * 1000)
    storageList = []
    for cuda in cudaList:
        for dock in dockList:
            #f1 = open(f'{dockerPath}cuda{cuda}/docker{dock}/remoteFiles/storagePickle', 'rb')
            os.system(f"sshpass -p {localpsword} scp '{dockerPath}cuda{cuda}/docker{dock}/remoteFiles/storagePickle' {localUsr}@{localIP}:{localPath}/storage{cuda}{dock}")
    #catf.write(f"cat used {round(time.time() * 1000) - lastT}ms\n")

def main():
    cpPthExp()
    runInDocker()
    catDockerStorage()

if __name__ == "__main__":
    main()
