#t:1371-2345 ; rate:1374-1480 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace252.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace252.txt", 'a+')
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1473kbit")
	time.sleep(1.416)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(2.344)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(1.546)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(1.731)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(1.464)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.149)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(1.534)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(1.682)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(1.795)
	tracef.write(f"1378 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1378kbit")
	time.sleep(1.506)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(2.261)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(1.775)
	tracef.write(f"1401 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1401kbit")
	time.sleep(1.755)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(1.582)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(1.806)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(2.077)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.162)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(1.994)
	tracef.write(f"1377 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1377kbit")
	time.sleep(1.795)
	tracef.write(f"1420 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1420kbit")
	time.sleep(1.857)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(1.845)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(1.462)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(1.991)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(1.519)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(1.64)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(1.702)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(1.848)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(1.974)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.534)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(2.098)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.633)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(2.258)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(1.388)
	tracef.write(f"1433 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1433kbit")
	time.sleep(1.977)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(1.8)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(1.831)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(2.323)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(1.696)
	tracef.write(f"1433 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1433kbit")
	time.sleep(2.269)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(2.016)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(2.2)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(1.922)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(2.093)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(1.651)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(1.866)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(1.913)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(1.472)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(1.785)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(1.744)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(1.602)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(2.249)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(1.942)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(1.942)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()