#t:1104-2700 ; rate:825-1546 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace369.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace369.txt", 'a+')
	tracef.write(f"1090 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1090kbit")
	time.sleep(2.19)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(1.761)
	tracef.write(f"908 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 908kbit")
	time.sleep(2.631)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(2.548)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(1.967)
	tracef.write(f"870 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 870kbit")
	time.sleep(2.194)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(1.107)
	tracef.write(f"1292 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1292kbit")
	time.sleep(2.213)
	tracef.write(f"920 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 920kbit")
	time.sleep(1.631)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(2.652)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(1.351)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(1.11)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(2.207)
	tracef.write(f"1340 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1340kbit")
	time.sleep(1.556)
	tracef.write(f"1375 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1375kbit")
	time.sleep(2.476)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(2.694)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(2.08)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(2.387)
	tracef.write(f"831 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 831kbit")
	time.sleep(2.234)
	tracef.write(f"1517 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1517kbit")
	time.sleep(1.595)
	tracef.write(f"1186 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1186kbit")
	time.sleep(2.51)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(2.099)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(1.382)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(1.433)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(1.712)
	tracef.write(f"997 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 997kbit")
	time.sleep(1.701)
	tracef.write(f"864 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 864kbit")
	time.sleep(1.341)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(2.631)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(2.157)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(1.657)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(2.555)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(2.634)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(1.617)
	tracef.write(f"991 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 991kbit")
	time.sleep(2.665)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(1.451)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(1.799)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(2.03)
	tracef.write(f"1387 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1387kbit")
	time.sleep(1.471)
	tracef.write(f"1056 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1056kbit")
	time.sleep(2.136)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(1.585)
	tracef.write(f"957 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 957kbit")
	time.sleep(1.7)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(2.61)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(2.496)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(2.382)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(1.663)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(1.21)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(2.593)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(1.575)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(1.575)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()