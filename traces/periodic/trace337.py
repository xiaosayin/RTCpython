#t:5000-5000 ; rate:980-1078 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/periodic/trace337.txt", 'w')
	tracef.close()
	tracef = open("traces/periodic/trace337.txt", 'a+')
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	tracef.flush()
	time.sleep(5.0)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()