import matplotlib.pyplot as plt
import math
import numpy as np

range1 = 50
range2 = 50
range3 = 50
range4 = 30
exp1 = 0.35
exp2 = 0.2
exp3 = 0.1
exp4 = 0.01
exp5 = 0
max_num_episodes = range1 + range2 + range3 + range4

e = []
exp = []
for episode in range(0, max_num_episodes):
    e.append(episode)
    if episode <= range1:
        this_exploration_param = ( exp1 - (exp1 - exp2)/range1 * episode)
    if episode > range1 and episode <= range1 + range2:
        this_exploration_param = ( exp2 - (exp2 - exp3)/range2 * (episode - range1))
    if episode > range1 + range2:
        this_exploration_param = ( exp3 - (exp3 - exp4)/range3 * (episode - range1 - range2))
    if episode > range1 + range2 + range3:
        this_exploration_param = ( exp4 - (exp4 - exp5)/range4 * (episode - range1 - range2 - range3))
    exp.append(this_exploration_param)

plt.plot(e, exp)


range1 = 50
range2 = 60
range3 = 70
exp1 = 0.35
exp2 = 0.2
exp3 = 0.1
exp4 = 0.01
max_num_episodes = range1 + range2 + range3

e = []
exp = []
for episode in range(0, max_num_episodes):
    e.append(episode)
    if episode <= range1:
        this_exploration_param = ( exp1 - (exp1 - exp2)/range1 * episode)
    if episode > range1 and episode <= range1 + range2:
        this_exploration_param = ( exp2 - (exp2 - exp3)/range2 * (episode - range1))
    if episode > range1 + range2:
        this_exploration_param = ( exp3 - (exp3 - exp4)/range3 * (episode - range1 - range2))
    exp.append(this_exploration_param)

plt.plot(e, exp)






plt.grid()
plt.savefig('tmpTry/exp.png')