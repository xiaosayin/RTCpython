#t:1376-2921 ; rate:1392-1478 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace272.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace272.txt", 'a+')
	tracef.write(f"1449 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1449kbit")
	time.sleep(1.393)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(2.785)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(2.626)
	tracef.write(f"1406 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1406kbit")
	time.sleep(2.039)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(2.116)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(1.426)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(1.586)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(1.636)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(1.961)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(1.725)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(1.402)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(2.623)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(1.857)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(1.396)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(1.871)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(2.43)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(2.414)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(1.597)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(2.777)
	tracef.write(f"1446 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1446kbit")
	time.sleep(2.521)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(1.767)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.651)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(2.214)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(2.439)
	tracef.write(f"1420 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1420kbit")
	time.sleep(2.097)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(1.656)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(1.926)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(1.531)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(1.629)
	tracef.write(f"1406 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1406kbit")
	time.sleep(2.078)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(1.823)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(2.335)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.732)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(2.058)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(2.061)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(1.575)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(1.871)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(2.263)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(2.297)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.404)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(2.46)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(1.499)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(2.633)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(1.91)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(2.652)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(2.432)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(2.432)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()