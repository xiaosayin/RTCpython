import os
import time

def updown():
    tracef = open("trace.txt", 'w')
    tracef.close()
    tracef = open("trace.txt", 'a+')
    lastT = 0
    kbit = 600
    addCmd = f"echo 1 | sudo -S tc qdisc add dev lo root netem rate {kbit}kbit"
    os.system(addCmd)
    time.sleep(4)
    thisT = round(time.time() * 1000)
    tracef.write(f"{kbit} ; {thisT}\n")
    for i in range(0, 8):
        kbit = 800
        changeCmd = f"echo 1 | sudo -S tc qdisc change dev lo root netem rate {kbit}kbit"
        #print(delCmd)
        thisT = round(time.time() * 1000)
        tracef.write(f"{kbit} ; {thisT}\n")
        os.system(changeCmd)
        time.sleep(4)

        kbit = 600
        changeCmd = f"echo 1 | sudo -S tc qdisc change dev lo root netem rate {kbit}kbit"
        thisT = round(time.time() * 1000)
        tracef.write(f"{kbit} ; {thisT}\n")
        os.system(changeCmd)
        time.sleep(4)
    delCmd = "echo 1 | sudo -S tc qdisc del dev lo root"
    os.system(delCmd)
    tracef.close()


def main():
    updown()

if __name__ == "__main__":
    main()
