#t:1907-2603 ; rate:1246-1329 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace219.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace219.txt", 'a+')
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1300kbit")
	time.sleep(2.345)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(2.367)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(2.313)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(2.569)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.549)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(2.145)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(2.494)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(2.496)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(2.141)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(2.166)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(2.221)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(2.043)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(2.569)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.41)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(2.244)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(2.439)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(1.918)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(2.3)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(2.578)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(2.154)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(2.062)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(1.911)
	tracef.write(f"1320 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1320kbit")
	time.sleep(2.603)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(2.416)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(2.066)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(2.112)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(2.392)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(2.508)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(2.322)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(2.348)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(2.36)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(2.111)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(2.326)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(2.376)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(2.568)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(2.187)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(2.515)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(2.188)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(2.005)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(2.12)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(2.053)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(2.061)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(2.061)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()