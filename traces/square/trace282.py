#t:1157-2617 ; rate:1101-1540 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace282.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace282.txt", 'a+')
	tracef.write(f"1460 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1460kbit")
	time.sleep(1.979)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(1.266)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(1.588)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(2.208)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(1.591)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(2.309)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(2.501)
	tracef.write(f"1215 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1215kbit")
	time.sleep(1.187)
	tracef.write(f"1178 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1178kbit")
	time.sleep(1.579)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(1.235)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(2.039)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(2.413)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(2.253)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(1.519)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(1.381)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(2.418)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(1.61)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.096)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(2.244)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(1.737)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(1.894)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(1.891)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(2.351)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(2.279)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(1.461)
	tracef.write(f"1181 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1181kbit")
	time.sleep(1.227)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(1.814)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(2.349)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(1.62)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(1.172)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(1.365)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(2.009)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(1.327)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(1.85)
	tracef.write(f"1159 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1159kbit")
	time.sleep(1.414)
	tracef.write(f"1293 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1293kbit")
	time.sleep(2.325)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(2.391)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(1.419)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(1.989)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(2.49)
	tracef.write(f"1215 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1215kbit")
	time.sleep(1.801)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(2.614)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(2.108)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(1.241)
	tracef.write(f"1528 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1528kbit")
	time.sleep(2.212)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(2.476)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(1.567)
	tracef.write(f"1510 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1510kbit")
	time.sleep(2.532)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(1.995)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(2.379)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(1.725)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(1.725)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()