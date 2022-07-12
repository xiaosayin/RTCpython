export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH

python3 ./peerconnection_serverless.py ./sender.json
