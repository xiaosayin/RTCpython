export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH

python3 ./peerconnection_serverless2.py ./sender_pyinfer.json ./receiver_pyinfer.json
