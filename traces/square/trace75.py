#t:1903-2361 ; rate:922-1466 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace75.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace75.txt", 'a+')
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1227kbit")
	time.sleep(2.012)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(2.266)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(2.273)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(2.206)
	tracef.write(f"1309 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1309kbit")
	time.sleep(1.973)
	tracef.write(f"1121 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1121kbit")
	time.sleep(1.961)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(2.022)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(1.905)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(2.175)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(2.017)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(2.225)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(2.172)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(2.071)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(1.916)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(2.082)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(2.071)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(2.228)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(2.226)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(2.125)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(2.216)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(1.948)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(2.311)
	tracef.write(f"1332 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1332kbit")
	time.sleep(2.138)
	tracef.write(f"1423 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1423kbit")
	time.sleep(2.353)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(2.237)
	tracef.write(f"1165 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1165kbit")
	time.sleep(2.222)
	tracef.write(f"1143 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1143kbit")
	time.sleep(2.291)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(1.94)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(2.229)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(2.14)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(2.149)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(2.295)
	tracef.write(f"1449 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1449kbit")
	time.sleep(1.912)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(2.058)
	tracef.write(f"1022 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1022kbit")
	time.sleep(2.03)
	tracef.write(f"1069 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1069kbit")
	time.sleep(2.039)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(2.037)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(2.012)
	tracef.write(f"1303 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1303kbit")
	time.sleep(2.212)
	tracef.write(f"1168 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1168kbit")
	time.sleep(2.035)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(2.055)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(2.078)
	tracef.write(f"1346 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1346kbit")
	time.sleep(2.03)
	tracef.write(f"1063 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1063kbit")
	time.sleep(2.277)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(1.925)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(1.925)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()