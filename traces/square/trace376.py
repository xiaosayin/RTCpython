#t:1401-1721 ; rate:924-1551 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace376.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace376.txt", 'a+')
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1164kbit")
	time.sleep(1.684)
	tracef.write(f"1411 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1411kbit")
	time.sleep(1.517)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(1.687)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(1.522)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(1.644)
	tracef.write(f"1359 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1359kbit")
	time.sleep(1.579)
	tracef.write(f"984 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 984kbit")
	time.sleep(1.504)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(1.516)
	tracef.write(f"1085 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1085kbit")
	time.sleep(1.647)
	tracef.write(f"1361 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1361kbit")
	time.sleep(1.486)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(1.463)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(1.432)
	tracef.write(f"1050 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1050kbit")
	time.sleep(1.555)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(1.607)
	tracef.write(f"1550 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1550kbit")
	time.sleep(1.591)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(1.5)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(1.413)
	tracef.write(f"1121 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1121kbit")
	time.sleep(1.646)
	tracef.write(f"1239 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1239kbit")
	time.sleep(1.436)
	tracef.write(f"999 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 999kbit")
	time.sleep(1.535)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(1.716)
	tracef.write(f"1344 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1344kbit")
	time.sleep(1.656)
	tracef.write(f"1207 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1207kbit")
	time.sleep(1.518)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(1.633)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(1.673)
	tracef.write(f"1528 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1528kbit")
	time.sleep(1.549)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.486)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(1.408)
	tracef.write(f"1411 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1411kbit")
	time.sleep(1.657)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(1.614)
	tracef.write(f"973 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 973kbit")
	time.sleep(1.442)
	tracef.write(f"1193 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1193kbit")
	time.sleep(1.55)
	tracef.write(f"1214 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1214kbit")
	time.sleep(1.611)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(1.469)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(1.558)
	tracef.write(f"1068 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1068kbit")
	time.sleep(1.631)
	tracef.write(f"1149 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1149kbit")
	time.sleep(1.467)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(1.601)
	tracef.write(f"1318 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1318kbit")
	time.sleep(1.419)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(1.536)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(1.508)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(1.572)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(1.445)
	tracef.write(f"1054 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1054kbit")
	time.sleep(1.503)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(1.596)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(1.433)
	tracef.write(f"1399 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1399kbit")
	time.sleep(1.659)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(1.669)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(1.561)
	tracef.write(f"1159 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1159kbit")
	time.sleep(1.453)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(1.72)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(1.417)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(1.412)
	tracef.write(f"1318 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1318kbit")
	time.sleep(1.709)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(1.533)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(1.551)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(1.442)
	tracef.write(f"1068 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1068kbit")
	time.sleep(1.552)
	tracef.write(f"968 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 968kbit")
	time.sleep(1.476)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(1.689)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(1.414)
	tracef.write(f"1168 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1168kbit")
	time.sleep(1.423)
	tracef.write(f"1168 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1168kbit")
	time.sleep(1.423)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()