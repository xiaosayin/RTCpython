#t:2642-2998 ; rate:1000-1430 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace145.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace145.txt", 'a+')
	tracef.write(f"1149 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1149kbit")
	time.sleep(2.763)
	tracef.write(f"1269 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1269kbit")
	time.sleep(2.698)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(2.774)
	tracef.write(f"1177 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1177kbit")
	time.sleep(2.9)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(2.763)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(2.878)
	tracef.write(f"1108 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1108kbit")
	time.sleep(2.696)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(2.667)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(2.643)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(2.79)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(2.993)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(2.832)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(2.925)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(2.781)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(2.78)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(2.719)
	tracef.write(f"1116 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1116kbit")
	time.sleep(2.784)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(2.833)
	tracef.write(f"1234 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1234kbit")
	time.sleep(2.971)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(2.8)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(2.727)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.711)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(2.894)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(2.679)
	tracef.write(f"1234 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1234kbit")
	time.sleep(2.706)
	tracef.write(f"1053 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1053kbit")
	time.sleep(2.67)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(2.705)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(2.841)
	tracef.write(f"1121 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1121kbit")
	time.sleep(2.882)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.79)
	tracef.write(f"1303 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1303kbit")
	time.sleep(2.753)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(2.831)
	tracef.write(f"1158 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1158kbit")
	time.sleep(2.658)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(2.901)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(2.806)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(2.806)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()