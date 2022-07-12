import matplotlib.pyplot as plt

width = [320, 480, 640, 960, 1280]
height = [180, 270, 360, 540, 720]

widthState = []
pixelState = []
for i in range(len(width)):
    widthState.append(width[i] / max(width))
    pixelState.append(width[i] * height[i] /1280 / 720)

plt.plot(range(0, 5), widthState)
plt.plot(range(0, 5), pixelState)
plt.savefig('tmpTry/widthState.png')