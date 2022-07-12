import os
MAX_LENGTH = 100000
def cutTrace(tracePath, cutPath):
    tracef = open(tracePath, 'r')
    traceLine = tracef.readline()
    base_time = 0
    cnt = 0
    while traceLine:
        file = f"{cutPath}_{cnt}"
        base_time = int(traceLine)
        filef = open(file, 'w')
        while traceLine:
            if int(traceLine) > base_time + MAX_LENGTH:
                filef.close()
                break
            else:
                filef.write(f"{int(traceLine) - base_time}\n")
                traceLine = tracef.readline()
        
        cnt += 1

def writeTrace(traceLine, file, base_time):
    tracef = open(file, 'w')
    while traceLine:
        if int(traceLine) > base_time + MAX_LENGTH:
            tracef.close()
            return traceLine
        else:
            tracef.write(f"{int(traceLine) - base_time}\n")
            traceLine = tracef.readline()
    return traceLine

def main():
    
    #file = 'trace-1553453943-ts-walking'
    path = 'sampledTraces/pens_traces/'
    cutPath = 'sampledTraces/pens_traces90s/'
    ls = os.listdir(path)
    for file in ls:
        if '.log'  not in file and '.png' not in file:
            tracePath = f'{path}{file}'
            newTracePath = f'{cutPath}{file}'
            cutTrace(tracePath, newTracePath)

if __name__ == "__main__":
    main()