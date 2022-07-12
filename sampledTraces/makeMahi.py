import os
def drawTrace(csvPath):
    tracePath = f"{csvPath[:csvPath.index('.')]}/"
    os.system(f"mkdir {tracePath}")
    tracef = open(csvPath, 'r')
    traceLine = tracef.readline()
    baseT = 0
    while (traceLine):
        t = 0
        while (getBW(traceLine) == 0):
            traceLine = tracef.readline()
            baseT += 1
        
        traceLine = tracef.readline()


def pickTrace(traceLine, baseT):
    traces = []
    for i in range(0, 100):
        if getBW(traceLine) != 0:
            traces.append(getBW(traceLine))

def getBW(traceLine):
    if ('0,bits/sec' in traceLine):
        return 0
    else:
        index = traceLine.index(',')
        if traceLine[index + 1] == 'M':
            return int(traceLine[:index]) * 1000
        if traceLine[index + 1] == 'K':
            return int(traceLine[:index])
        else:
            return 0

def main():
    csvPath = 'sampledTraces/Dataset/7Train/7BtrainNew.csv'
    drawTrace(csvPath)

if __name__ == "__main__":
    main()