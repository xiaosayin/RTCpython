#t:1381-1965 ; rate:961-1494 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace316.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace316.txt", 'a+')
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1478kbit")
	time.sleep(1.815)
	tracef.write(f"1012 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1012kbit")
	time.sleep(1.92)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(1.543)
	tracef.write(f"1114 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1114kbit")
	time.sleep(1.56)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(1.93)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(1.783)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(1.734)
	tracef.write(f"1334 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1334kbit")
	time.sleep(1.393)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(1.504)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(1.866)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(1.913)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(1.651)
	tracef.write(f"965 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 965kbit")
	time.sleep(1.464)
	tracef.write(f"980 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 980kbit")
	time.sleep(1.5)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(1.674)
	tracef.write(f"978 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 978kbit")
	time.sleep(1.741)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(1.637)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(1.867)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(1.888)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(1.718)
	tracef.write(f"975 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 975kbit")
	time.sleep(1.604)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(1.837)
	tracef.write(f"1018 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1018kbit")
	time.sleep(1.4)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(1.578)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.418)
	tracef.write(f"991 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 991kbit")
	time.sleep(1.574)
	tracef.write(f"971 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 971kbit")
	time.sleep(1.7)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(1.475)
	tracef.write(f"1003 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1003kbit")
	time.sleep(1.824)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(1.737)
	tracef.write(f"1361 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1361kbit")
	time.sleep(1.649)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(1.94)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(1.514)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(1.667)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(1.831)
	tracef.write(f"1349 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1349kbit")
	time.sleep(1.851)
	tracef.write(f"1091 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1091kbit")
	time.sleep(1.614)
	tracef.write(f"1277 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1277kbit")
	time.sleep(1.53)
	tracef.write(f"1020 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1020kbit")
	time.sleep(1.927)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(1.868)
	tracef.write(f"1437 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1437kbit")
	time.sleep(1.899)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(1.763)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(1.842)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(1.638)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(1.668)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(1.762)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(1.764)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(1.607)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(1.738)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(1.819)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(1.544)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(1.776)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(1.732)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(1.941)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(1.51)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(1.776)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(1.776)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()