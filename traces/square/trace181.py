#t:1481-1627 ; rate:1202-1547 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace181.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace181.txt", 'a+')
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1235kbit")
	time.sleep(1.506)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(1.526)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(1.569)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(1.528)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(1.618)
	tracef.write(f"1352 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1352kbit")
	time.sleep(1.622)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(1.58)
	tracef.write(f"1498 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1498kbit")
	time.sleep(1.481)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(1.549)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(1.539)
	tracef.write(f"1460 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1460kbit")
	time.sleep(1.599)
	tracef.write(f"1334 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1334kbit")
	time.sleep(1.53)
	tracef.write(f"1517 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1517kbit")
	time.sleep(1.511)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(1.507)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(1.498)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.572)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(1.555)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(1.543)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(1.522)
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1511kbit")
	time.sleep(1.576)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(1.542)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(1.56)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(1.582)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(1.591)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(1.571)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(1.557)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(1.571)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(1.558)
	tracef.write(f"1228 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1228kbit")
	time.sleep(1.547)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(1.491)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(1.521)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(1.606)
	tracef.write(f"1354 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1354kbit")
	time.sleep(1.508)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(1.515)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(1.561)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(1.497)
	tracef.write(f"1318 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1318kbit")
	time.sleep(1.599)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(1.554)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(1.589)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(1.601)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(1.626)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(1.553)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(1.535)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(1.616)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(1.619)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(1.505)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(1.609)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(1.551)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(1.621)
	tracef.write(f"1523 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1523kbit")
	time.sleep(1.591)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(1.566)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.494)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(1.549)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(1.496)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(1.567)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(1.553)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(1.508)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(1.594)
	tracef.write(f"1422 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1422kbit")
	time.sleep(1.499)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(1.605)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(1.49)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(1.577)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(1.577)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()