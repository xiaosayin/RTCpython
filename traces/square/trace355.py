#t:2516-2798 ; rate:914-1541 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace355.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace355.txt", 'a+')
	tracef.write(f"1011 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1011kbit")
	time.sleep(2.614)
	tracef.write(f"1379 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1379kbit")
	time.sleep(2.64)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(2.746)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(2.532)
	tracef.write(f"1075 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1075kbit")
	time.sleep(2.676)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(2.76)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(2.692)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(2.77)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.751)
	tracef.write(f"1405 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1405kbit")
	time.sleep(2.611)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(2.628)
	tracef.write(f"919 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 919kbit")
	time.sleep(2.659)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(2.588)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(2.679)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(2.789)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(2.607)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(2.605)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(2.651)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(2.683)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.568)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(2.548)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(2.797)
	tracef.write(f"1381 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1381kbit")
	time.sleep(2.606)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(2.522)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(2.607)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(2.598)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(2.532)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(2.75)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(2.517)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(2.628)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(2.713)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(2.772)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(2.583)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.724)
	tracef.write(f"1081 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1081kbit")
	time.sleep(2.798)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(2.669)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(2.669)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()