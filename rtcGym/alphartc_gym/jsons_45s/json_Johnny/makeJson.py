portNum = 8001
while portNum < 8000 + 121:
    newrecvf = open(f"./rtcGym/alphartc_gym/json_Johnny/receiver_pyinfer{portNum}.json", 'w')
    newrecvf.close()
    newrecvf = open(f"./rtcGym/alphartc_gym/json_Johnny/receiver_pyinfer{portNum}.json", 'a+')
    recvf8000 = open("./rtcGym/alphartc_gym/json_Johnny/receiver_pyinfer8000.json")
    recv8000Line = recvf8000.readline()
    while recv8000Line:
        if "\"listening_port\": " not in recv8000Line:
            newrecvf.write(recv8000Line)
        else:
            newrecvf.write(f"\t\t\t\"listening_port\": {portNum}\n")
        recv8000Line = recvf8000.readline()
    newrecvf.close()
    recvf8000.close()

    newsendf = open(f"./rtcGym/alphartc_gym/json_Johnny/sender_pyinfer{portNum}.json", 'w')
    newsendf.close()
    newsendf = open(f"./rtcGym/alphartc_gym/json_Johnny/sender_pyinfer{portNum}.json", 'a+')
    sendf8000 = open("./rtcGym/alphartc_gym/json_Johnny/sender_pyinfer8000.json")
    send8000Line = sendf8000.readline()
    while send8000Line:
        if "\"dest_port\": " not in send8000Line:
            newsendf.write(send8000Line)
        else:
            newsendf.write(f"\t\t\t\"dest_port\": {portNum}\n")
        send8000Line = sendf8000.readline()
    portNum += 1