rm result/*
rm result/tmp/*
rm result/delay/*
export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH

python ./peerconnection_serverless.py ./receiver_pyinfer.json
