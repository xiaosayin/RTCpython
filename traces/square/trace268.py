#t:1246-2168 ; rate:1384-1532 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace268.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace268.txt", 'a+')
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1388kbit")
	time.sleep(1.676)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(1.656)
	tracef.write(f"1454 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1454kbit")
	time.sleep(1.653)
	tracef.write(f"1437 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1437kbit")
	time.sleep(1.695)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(1.993)
	tracef.write(f"1447 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1447kbit")
	time.sleep(1.483)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(1.262)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(2.114)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(1.888)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(1.876)
	tracef.write(f"1530 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1530kbit")
	time.sleep(1.323)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(1.989)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(1.444)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(1.987)
	tracef.write(f"1487 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1487kbit")
	time.sleep(1.883)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(2.069)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(1.318)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(1.578)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(1.823)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(1.642)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(1.773)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(1.84)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(2.001)
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1511kbit")
	time.sleep(1.503)
	tracef.write(f"1423 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1423kbit")
	time.sleep(2.033)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(1.85)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(1.552)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(1.894)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(1.626)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(1.526)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(2.058)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(1.81)
	tracef.write(f"1493 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1493kbit")
	time.sleep(1.252)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(2.118)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(1.728)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(1.751)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(1.463)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(2.155)
	tracef.write(f"1529 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1529kbit")
	time.sleep(1.259)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(1.867)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(1.638)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(1.757)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(1.427)
	tracef.write(f"1386 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1386kbit")
	time.sleep(1.894)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(1.531)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(1.54)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(1.251)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(1.429)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(2.057)
	tracef.write(f"1529 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1529kbit")
	time.sleep(1.365)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.088)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(1.337)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(1.467)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(1.881)
	tracef.write(f"1429 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1429kbit")
	time.sleep(1.308)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(2.041)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(2.041)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()