rm result/*

export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH

python ./peerconnection_serverless.py ./receiver.json
