#t:1480-1755 ; rate:812-1581 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace204.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace204.txt", 'a+')
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1357kbit")
	time.sleep(1.564)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(1.686)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(1.545)
	tracef.write(f"1056 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1056kbit")
	time.sleep(1.55)
	tracef.write(f"1509 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1509kbit")
	time.sleep(1.69)
	tracef.write(f"1533 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1533kbit")
	time.sleep(1.576)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(1.509)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(1.737)
	tracef.write(f"1205 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1205kbit")
	time.sleep(1.493)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(1.551)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(1.644)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(1.529)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(1.743)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(1.49)
	tracef.write(f"1044 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1044kbit")
	time.sleep(1.569)
	tracef.write(f"1557 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1557kbit")
	time.sleep(1.586)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(1.625)
	tracef.write(f"1011 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1011kbit")
	time.sleep(1.506)
	tracef.write(f"1354 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1354kbit")
	time.sleep(1.751)
	tracef.write(f"1117 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1117kbit")
	time.sleep(1.667)
	tracef.write(f"1481 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1481kbit")
	time.sleep(1.493)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(1.592)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(1.611)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(1.754)
	tracef.write(f"907 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 907kbit")
	time.sleep(1.734)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(1.549)
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1272kbit")
	time.sleep(1.725)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(1.734)
	tracef.write(f"1011 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1011kbit")
	time.sleep(1.557)
	tracef.write(f"891 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 891kbit")
	time.sleep(1.513)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(1.507)
	tracef.write(f"1349 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1349kbit")
	time.sleep(1.691)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(1.563)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(1.527)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(1.674)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(1.565)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(1.617)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(1.508)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(1.632)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(1.541)
	tracef.write(f"1354 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1354kbit")
	time.sleep(1.664)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(1.684)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(1.574)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(1.643)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(1.755)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(1.53)
	tracef.write(f"1205 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1205kbit")
	time.sleep(1.706)
	tracef.write(f"1073 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1073kbit")
	time.sleep(1.61)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(1.655)
	tracef.write(f"1011 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1011kbit")
	time.sleep(1.516)
	tracef.write(f"816 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 816kbit")
	time.sleep(1.686)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(1.712)
	tracef.write(f"1096 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1096kbit")
	time.sleep(1.488)
	tracef.write(f"1578 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1578kbit")
	time.sleep(1.603)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(1.675)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(1.642)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(1.542)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(1.546)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(1.639)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(1.641)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(1.641)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()