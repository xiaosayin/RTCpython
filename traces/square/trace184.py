#t:2309-2765 ; rate:966-1072 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace184.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace184.txt", 'a+')
	tracef.write(f"1053 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1053kbit")
	time.sleep(2.672)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(2.638)
	tracef.write(f"1029 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1029kbit")
	time.sleep(2.316)
	tracef.write(f"1063 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1063kbit")
	time.sleep(2.613)
	tracef.write(f"1013 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1013kbit")
	time.sleep(2.444)
	tracef.write(f"1052 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1052kbit")
	time.sleep(2.476)
	tracef.write(f"972 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 972kbit")
	time.sleep(2.404)
	tracef.write(f"998 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 998kbit")
	time.sleep(2.619)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(2.467)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(2.726)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(2.662)
	tracef.write(f"1012 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1012kbit")
	time.sleep(2.701)
	tracef.write(f"980 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 980kbit")
	time.sleep(2.455)
	tracef.write(f"1044 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1044kbit")
	time.sleep(2.611)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.511)
	tracef.write(f"1047 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1047kbit")
	time.sleep(2.567)
	tracef.write(f"997 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 997kbit")
	time.sleep(2.542)
	tracef.write(f"982 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 982kbit")
	time.sleep(2.579)
	tracef.write(f"971 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 971kbit")
	time.sleep(2.672)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(2.39)
	tracef.write(f"985 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 985kbit")
	time.sleep(2.731)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(2.644)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(2.332)
	tracef.write(f"998 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 998kbit")
	time.sleep(2.602)
	tracef.write(f"1012 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1012kbit")
	time.sleep(2.634)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(2.659)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(2.425)
	tracef.write(f"1046 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1046kbit")
	time.sleep(2.351)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(2.355)
	tracef.write(f"997 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 997kbit")
	time.sleep(2.484)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.394)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(2.529)
	tracef.write(f"1022 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1022kbit")
	time.sleep(2.75)
	tracef.write(f"977 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 977kbit")
	time.sleep(2.403)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(2.587)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(2.352)
	tracef.write(f"975 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 975kbit")
	time.sleep(2.332)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(2.681)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(2.681)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()