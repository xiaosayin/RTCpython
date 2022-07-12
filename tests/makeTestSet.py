import random

import pickle

randomSeed = 0
SetNum = 110
random.seed(randomSeed)

traceType = []
traceNum = []
queLength = []
lossRate = []
video = []
for i in range(0, SetNum):
    traceRandom = random.randint(0, 199)
    if traceRandom < 100:
        traceType.append('random')
    else:
        traceType.append('periodic')
    traceNum.append(traceRandom % 100)
    queLength.append(random.randint(6, 349))
    lossRate.append(float(random.randint(0, 500)) / 100)
    video.append(random.randint(0, 0))
path = f'tests'
f=open(path + '/DividedTestSetPickle','wb')
pickle.dump([traceType, traceNum, queLength, lossRate, video], f, 0)
f.close()