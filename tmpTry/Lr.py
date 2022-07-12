from re import L
import matplotlib.pyplot as plt
import math
import numpy as np

range1 = 50
range2 = 60
range3 = 70
exp1 = 0.35
exp2 = 0.2
exp3 = 0.1
exp4 = 0.01
max_num_episodes = range1 + range2 + range3
lrMax = 3e-3                 # Adam parameters
lrMin = 3e-5
a = lrMax
b = lrMin
e = max_num_episodes
es = []
lrs = []
for episode in range(max_num_episodes):

    lr = (a - b) / 2 * math.cos(1 / e * math.pi  * episode) + (a + b) / 2
    es.append(episode)
    lrs.append(lr)
plt.plot(es, lrs)

es = []
lrs = []
lr = lrMax
for episode in range(max_num_episodes):

    if episode == 50:
        lr = lr * 0.1
    if episode == 110:
        lr = lr * 0.1
    es.append(episode)
    lrs.append(lr)


plt.plot(es, lrs)

es = []
lrs = []
lr = lrMax
d = [30, 30, 30, 30, 40, 50]
episodesList = []
for i in range(len(d)):
    if i == 0:
        episodesList.append(d[i])
    else:
        episodesList.append(d[i] + episodesList[i - 1])

for episode in range(max_num_episodes):

    if episode in episodesList:
        lr = lr /3
    es.append(episode)
    lrs.append(lr)

plt.plot(es, lrs)


plt.grid()
plt.savefig('tmpTry/lr.png')