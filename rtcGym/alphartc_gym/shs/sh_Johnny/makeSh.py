portNum = 8001
path = "./rtcGym/alphartc_gym/shs/sh_Johnny"
while portNum < 8000 + 121:
    newrecvf = open(f"{path}/pcsend{portNum}.sh", 'w')
    newrecvf.close()
    newrecvf = open(f"{path}/pcsend{portNum}.sh", 'a+')
    recvf8000 = open(f"{path}/pcsend8000.sh")
    recv8000Line = recvf8000.readline()
    while recv8000Line:
        if "./peerconnection_serverless.origin " not in recv8000Line:
            newrecvf.write(recv8000Line)
        else:
            newrecvf.write(f"./peerconnection_serverless.origin ./rtcGym/alphartc_gym/jsons/json_Johnny/sender_pyinfer{portNum}.json\n")
        recv8000Line = recvf8000.readline()
    newrecvf.close()
    recvf8000.close()
    portNum += 1