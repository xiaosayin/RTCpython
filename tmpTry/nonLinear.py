import matplotlib.pyplot as plt
import math
import numpy as np
MIN_FACTOR = 0.7
MAX_FACTOR = 1/MIN_FACTOR
a_factor = MAX_FACTOR - MIN_FACTOR
b_factor = math.log(a_factor/(1-MIN_FACTOR),2)
x= []
xt = []
nonLy =[]
nonLyt = []
Ly = []
BiLy = []
k = 8
for i in range(0, 100):
    value = i / 100
    x.append(value)

    nonLy.append((-1/2 +  1 / (1 + math.exp(-k * value + 1/2 * k ))) * (MAX_FACTOR - MIN_FACTOR) + (MAX_FACTOR + MIN_FACTOR) / 2)
    Ly.append((MAX_FACTOR - MIN_FACTOR) * (value) + MIN_FACTOR)
    if value >= 0.5:
        BiLy.append((MAX_FACTOR - 1) * 2 * (value - 0.5) + 1)
    else:
        BiLy.append((1 - MIN_FACTOR) * 2 * value + MIN_FACTOR)

for j in range(1, 100):

    value = (MAX_FACTOR - MIN_FACTOR) * j / 100 + MIN_FACTOR
    xt.append(value)
    nonLyt.append(-math.log(1 / ((value - (MAX_FACTOR + MIN_FACTOR) / 2) / (MAX_FACTOR - MIN_FACTOR) + 1 / 2) - 1) / k  + 1 / 2)

high_low_linearx = []
high_low_lineary = []
HL_MAX_FACTOR = 1.5
HL_MIN_FACTOR = 0.5
for j in range(1, 100):
    value = j / 100
    high_low_linearx.append(value)
    high_low_lineary.append((HL_MAX_FACTOR - HL_MIN_FACTOR) * (value) + HL_MIN_FACTOR)


x0711 = []
y0711 = []
MAX_FACTOR_0711 = 1.1
MIN_FACTOR_0711 = 0.7
for j in range(1, 100):
    value = j / 100
    x0711.append(value)
    if value >= 0.4:
        y0711.append((MAX_FACTOR_0711 - 1) / 0.6 * (value - 0.4) + 1)
    else:
        y0711.append((1 - MIN_FACTOR_0711) / 0.4 * value + MIN_FACTOR_0711)


#==================
#InfSigmoid
MAX_INFSIG = 1.15
MIN_INFSIG = 0.6
MIDX = 0.4
MIDY = 1
infSigx = []
infSigy = []
for j in range(-100, 200):
    value = j / 100
    infSigx.append(value)
    if value >= MIDX:
        infSigy.append( (1/(1 + math.exp(- (3) * (value - 0.4))) - 1/2 ) * 2 * (MAX_INFSIG - MIDY) + 1)
    else:
        infSigy.append( (1/(1 + math.exp(- (5) * (value - 0.4))) - 1/2 ) * 2 * (MIDY - MIN_INFSIG) + 1)

#=========



plt.xlim((-1, 2))
plt.ylim((-1, 2))
my_x_ticks = np.arange(-10, 10, 0.2)#原始数据有13个点，故此处为设置从0开始，间隔为1
#plt.xticks(my_x_ticks)
my_y_ticks = np.arange(-10, 10, 0.2)#原始数据有13个点，故此处为设置从0开始，间隔为1
#plt.yticks(my_y_ticks)
plt.plot(x, nonLy)
plt.plot(x, Ly)
plt.plot(xt, nonLyt)
plt.plot(x, BiLy)
plt.plot(high_low_linearx, high_low_lineary)
plt.plot(x0711, y0711)
plt.plot(infSigx, infSigy)
plt.grid()
plt.savefig('tmpTry/nonLinear.png')
