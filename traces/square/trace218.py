#t:2155-2459 ; rate:1320-1561 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace218.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace218.txt", 'a+')
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1511kbit")
	time.sleep(2.399)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(2.251)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(2.182)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(2.268)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(2.23)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(2.187)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(2.209)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(2.193)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(2.447)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(2.231)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(2.433)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(2.157)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(2.362)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(2.453)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(2.415)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(2.298)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(2.311)
	tracef.write(f"1481 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1481kbit")
	time.sleep(2.161)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(2.368)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(2.284)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(2.375)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(2.389)
	tracef.write(f"1483 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1483kbit")
	time.sleep(2.418)
	tracef.write(f"1536 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1536kbit")
	time.sleep(2.316)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(2.209)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(2.425)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(2.317)
	tracef.write(f"1375 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1375kbit")
	time.sleep(2.45)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(2.32)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(2.429)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(2.426)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(2.375)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(2.427)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(2.197)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(2.321)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(2.263)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(2.37)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(2.189)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(2.267)
	tracef.write(f"1386 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1386kbit")
	time.sleep(2.29)
	tracef.write(f"1346 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1346kbit")
	time.sleep(2.395)
	tracef.write(f"1346 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1346kbit")
	time.sleep(2.395)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()