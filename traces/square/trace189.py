#t:1640-2864 ; rate:1112-1512 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace189.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace189.txt", 'a+')
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1206kbit")
	time.sleep(2.45)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(2.273)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(2.706)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(2.212)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(2.651)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(2.696)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(2.55)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(2.02)
	tracef.write(f"1112 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1112kbit")
	time.sleep(1.981)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(2.746)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(2.757)
	tracef.write(f"1145 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1145kbit")
	time.sleep(1.825)
	tracef.write(f"1481 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1481kbit")
	time.sleep(2.398)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(2.571)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(1.958)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(2.404)
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1164kbit")
	time.sleep(2.791)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(2.498)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(1.992)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(2.809)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(2.342)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(2.387)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(2.41)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(2.069)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(2.112)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(2.422)
	tracef.write(f"1447 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1447kbit")
	time.sleep(2.485)
	tracef.write(f"1423 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1423kbit")
	time.sleep(2.651)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(2.696)
	tracef.write(f"1340 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1340kbit")
	time.sleep(2.497)
	tracef.write(f"1350 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1350kbit")
	time.sleep(2.34)
	tracef.write(f"1352 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1352kbit")
	time.sleep(2.388)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(2.463)
	tracef.write(f"1179 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1179kbit")
	time.sleep(2.391)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(1.696)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(2.176)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(1.842)
	tracef.write(f"1275 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1275kbit")
	time.sleep(2.713)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.819)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(1.733)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(2.404)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(2.404)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()