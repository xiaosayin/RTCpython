#t:2049-2835 ; rate:1437-1559 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace22.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace22.txt", 'a+')
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1478kbit")
	time.sleep(2.757)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(2.569)
	tracef.write(f"1481 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1481kbit")
	time.sleep(2.187)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(2.511)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(2.349)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(2.647)
	tracef.write(f"1492 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1492kbit")
	time.sleep(2.273)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(2.389)
	tracef.write(f"1487 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1487kbit")
	time.sleep(2.198)
	tracef.write(f"1492 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1492kbit")
	time.sleep(2.229)
	tracef.write(f"1546 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1546kbit")
	time.sleep(2.478)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(2.082)
	tracef.write(f"1545 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1545kbit")
	time.sleep(2.603)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(2.363)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(2.433)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(2.61)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(2.311)
	tracef.write(f"1533 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1533kbit")
	time.sleep(2.083)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(2.254)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(2.194)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(2.597)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(2.152)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(2.178)
	tracef.write(f"1550 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1550kbit")
	time.sleep(2.236)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(2.547)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(2.494)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(2.744)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(2.614)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(2.595)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(2.229)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(2.484)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(2.706)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.469)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(2.665)
	tracef.write(f"1493 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1493kbit")
	time.sleep(2.376)
	tracef.write(f"1547 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1547kbit")
	time.sleep(2.234)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(2.065)
	tracef.write(f"1525 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1525kbit")
	time.sleep(2.806)
	tracef.write(f"1459 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1459kbit")
	time.sleep(2.419)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(2.093)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(2.093)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()