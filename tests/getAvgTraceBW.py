# used to calculte the average bandwidth of a trace

def getBW(testType, testNum):
    tracef = open(f"mahiTraces/{testType}/trace{testNum}.log", 'r')
    traceLine = tracef.readline()
    traceLine = tracef.readline()
    bits = 0
    time = 0
    while traceLine:
        rate = int(traceLine[traceLine.index("rate: ") + len("rate: "):traceLine.index(" 	 duration: ")])
        duration = int(traceLine[traceLine.index(" 	 duration: ") + len(" 	 duration: "):])
        bits += rate * duration / 1000
        time += duration / 1000
        traceLine = tracef.readline()
    return bits/time


def main():
    print(getBW("random", 1))


    

if __name__ == "__main__":
    main()
