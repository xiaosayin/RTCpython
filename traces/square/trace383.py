#t:1137-2122 ; rate:1190-1590 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace383.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace383.txt", 'a+')
	tracef.write(f"1406 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1406kbit")
	time.sleep(1.847)
	tracef.write(f"1492 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1492kbit")
	time.sleep(1.724)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(1.778)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(2.022)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(1.16)
	tracef.write(f"1462 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1462kbit")
	time.sleep(1.588)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(1.571)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(1.954)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(1.697)
	tracef.write(f"1245 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1245kbit")
	time.sleep(1.906)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(1.621)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(1.926)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(1.391)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(1.518)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(1.838)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(1.429)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(1.869)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(2.107)
	tracef.write(f"1534 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1534kbit")
	time.sleep(1.989)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(1.735)
	tracef.write(f"1336 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1336kbit")
	time.sleep(1.888)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(1.832)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(2.064)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(1.275)
	tracef.write(f"1552 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1552kbit")
	time.sleep(1.453)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(1.995)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(1.188)
	tracef.write(f"1525 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1525kbit")
	time.sleep(1.504)
	tracef.write(f"1224 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1224kbit")
	time.sleep(1.717)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(1.143)
	tracef.write(f"1382 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1382kbit")
	time.sleep(1.982)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(1.216)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(1.873)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(2.045)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(1.501)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(2.107)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(1.293)
	tracef.write(f"1245 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1245kbit")
	time.sleep(1.458)
	tracef.write(f"1499 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1499kbit")
	time.sleep(1.77)
	tracef.write(f"1406 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1406kbit")
	time.sleep(1.158)
	tracef.write(f"1387 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1387kbit")
	time.sleep(1.579)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(1.919)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(1.935)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(1.166)
	tracef.write(f"1360 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1360kbit")
	time.sleep(1.67)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(1.811)
	tracef.write(f"1459 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1459kbit")
	time.sleep(1.83)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(1.688)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(1.558)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(1.945)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(1.75)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(1.58)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(1.419)
	tracef.write(f"1534 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1534kbit")
	time.sleep(1.189)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(1.221)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(1.838)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(1.191)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(1.954)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(1.954)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()