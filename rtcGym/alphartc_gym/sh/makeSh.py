portNum = 8001
while portNum < 8000 + 121:
    newrecvf = open(f"./rtcGym/alphartc_gym/sh/pcsend{portNum}.sh", 'w')
    newrecvf.close()
    newrecvf = open(f"./rtcGym/alphartc_gym/sh/pcsend{portNum}.sh", 'a+')
    recvf8000 = open("./rtcGym/alphartc_gym/sh/pcsend8000.sh")
    recv8000Line = recvf8000.readline()
    while recv8000Line:
        if "./peerconnection_serverless.origin ./rtcGym/alphartc_gym/json/sender_pyinfer" not in recv8000Line:
            newrecvf.write(recv8000Line)
        else:
            newrecvf.write(f"./peerconnection_serverless.origin ./rtcGym/alphartc_gym/json/sender_pyinfer{portNum}.json\n")
        recv8000Line = recvf8000.readline()
    newrecvf.close()
    recvf8000.close()
    portNum += 1