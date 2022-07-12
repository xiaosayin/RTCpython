
import time
def printLog(line, switch, logf):
    if switch:
        if logf == None:
            print(line + f"{round(time.time() * 1000)}")
        else:
            logf.write(line)
            logf.flush()
