#t:1544-2416 ; rate:950-1491 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace137.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace137.txt", 'a+')
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1023kbit")
	time.sleep(2.024)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(2.331)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(2.36)
	tracef.write(f"1384 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1384kbit")
	time.sleep(1.585)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(1.828)
	tracef.write(f"1123 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1123kbit")
	time.sleep(2.238)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(1.86)
	tracef.write(f"957 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 957kbit")
	time.sleep(1.693)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(1.85)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.669)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(2.275)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(1.554)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(1.917)
	tracef.write(f"1205 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1205kbit")
	time.sleep(1.872)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(2.006)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(2.097)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(1.563)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(2.263)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(1.842)
	tracef.write(f"1437 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1437kbit")
	time.sleep(1.799)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(1.881)
	tracef.write(f"1157 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1157kbit")
	time.sleep(2.148)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(1.643)
	tracef.write(f"1028 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1028kbit")
	time.sleep(2.303)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(1.918)
	tracef.write(f"1029 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1029kbit")
	time.sleep(2.4)
	tracef.write(f"1423 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1423kbit")
	time.sleep(1.705)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(1.629)
	tracef.write(f"966 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 966kbit")
	time.sleep(2.074)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(2.347)
	tracef.write(f"964 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 964kbit")
	time.sleep(2.18)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(2.252)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(1.74)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(1.939)
	tracef.write(f"1245 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1245kbit")
	time.sleep(1.813)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(2.257)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(2.316)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(1.727)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.014)
	tracef.write(f"1036 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1036kbit")
	time.sleep(2.048)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(2.114)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(2.065)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(1.945)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(2.379)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(2.188)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(1.909)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(2.321)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(2.065)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(2.065)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()