import sys
import os
import subprocess
import pickle
import time

#user: koyong
#gid: 1000
cudaList = [0, 1, 2, 3]
dockList = [0, 1, 2]
# cudaList = [1]
# dockList = [1]
dockerPath = "/home/yinwenpei/DockerRTC/"             # "/home/koyong/DockerRTC/"
localIP = "172.16.7.251" # "172.16.6.123"
localPath = "/home/yinwenpei/RTCPython/localFiles"              # "/home/koyong/RTC/AlphaRTCNoDocker/localFiles"
localUsr = "yinwenpei" #"koyong"
localpsword = "jj"      #"1"
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
    # stop all dockers
    os.system(f"docker stop $(docker ps -q)")

    dockers = []
    for cuda in cudaList:
        for dock in dockList:
            # dockerCmd = f"echo '1' | sudo -S docker run --rm -u koyong:1000 -v {dockerPath}cuda{cuda}/docker{dock}/:/RTC -w '/RTC' -e LD_LIBRARY_PATH=/RTC/lib --gpus all --privileged=true cuda_mahi sh trainRemote.sh"
            # dockerCmd = f"docker run --rm -u koyong:1000 -v {dockerPath}cuda{cuda}/docker{dock}/:/RTC -w '/RTC' -e LD_LIBRARY_PATH=/RTC/lib --gpus all --privileged=true cuda_mahi sh trainRemote.sh"
            dockerCmd = f"docker run --rm -u yinwenpei:1000 -v {dockerPath}cuda{cuda}/docker{dock}/:/RTC -w '/RTC' -e LD_LIBRARY_PATH=/RTC/lib --gpus all --privileged=true yinwenpei/allenv:Done sh trainRemote.sh"
            app = subprocess.Popen(
                    dockerCmd,
                    shell=True,

                    bufsize=1,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
            dockers.append(app)

    i = 0
    for d in dockers:
        # popen.communicate use ram to storage pipe info, avoid popen.wait deadblock
        # output, error = d.communicate()
        # print("output:", output)
        # print("error:", error)

        # try:
        #     if i==0:
        #         return_code = d.wait(timeout=120)
        #     else:
        #         return_code = d.wait(timeout=20)
        # except subprocess.TimeoutExpired:
        #     d.kill()
        #     os.system(f"docker stop $(docker ps -q)")
        #     print("timeout (docker id): ", i)
        # print("return code: ", return_code)
        d.wait()
        line = d.stdout.readline()
        while line:
            line = line.decode("utf-8")
            print(line)
            line = d.stdout.readline()
        print(f"docker{d} done")
        i += 1
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
