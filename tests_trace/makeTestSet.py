import random
import os
import pickle

randomSeed = 0
SetNum = 110
random.seed(randomSeed)
chosenTracesPath = "sampledTraces/chosenTraces/"
ls = os.listdir(chosenTracesPath)

traceName = []
for t in ls:
    if '.log' not in t and '.png' not in t:
        traceName.append(t)

queLength = []
lossRate = []
video = []
for i in range(0, len(traceName)):
    queLength.append(random.randint(6, 349))
    lossRate.append(float(random.randint(0, 500)) / 100)
    video.append(random.randint(0, 0))
'''
traceName.pop(0)
queLength.pop(0)
lossRate.pop(0)
video.pop(0)
'''
path = f'tests_trace'
f=open(path + '/DividedTestSetPickle','wb')
pickle.dump([traceName, queLength, lossRate, video], f, 0)
f.close()