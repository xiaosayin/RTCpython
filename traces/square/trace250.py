#t:1143-2567 ; rate:1206-1415 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace250.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace250.txt", 'a+')
	tracef.write(f"1358 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1358kbit")
	time.sleep(1.954)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(2.334)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(2.396)
	tracef.write(f"1311 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1311kbit")
	time.sleep(1.741)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(1.534)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(2.404)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(1.919)
	tracef.write(f"1240 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1240kbit")
	time.sleep(2.229)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(2.52)
	tracef.write(f"1214 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1214kbit")
	time.sleep(1.359)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(1.638)
	tracef.write(f"1401 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1401kbit")
	time.sleep(1.531)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(2.068)
	tracef.write(f"1288 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1288kbit")
	time.sleep(2.261)
	tracef.write(f"1323 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1323kbit")
	time.sleep(2.061)
	tracef.write(f"1381 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1381kbit")
	time.sleep(1.406)
	tracef.write(f"1371 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1371kbit")
	time.sleep(2.286)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(2.533)
	tracef.write(f"1310 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1310kbit")
	time.sleep(1.47)
	tracef.write(f"1216 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1216kbit")
	time.sleep(2.269)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(1.56)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(1.65)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(1.392)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(2.225)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(1.974)
	tracef.write(f"1360 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1360kbit")
	time.sleep(1.774)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(1.909)
	tracef.write(f"1307 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1307kbit")
	time.sleep(2.478)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.499)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(1.301)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(1.833)
	tracef.write(f"1275 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1275kbit")
	time.sleep(2.565)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(1.857)
	tracef.write(f"1301 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1301kbit")
	time.sleep(1.143)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(2.194)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(1.925)
	tracef.write(f"1214 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1214kbit")
	time.sleep(1.622)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(1.997)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(2.141)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(1.791)
	tracef.write(f"1362 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1362kbit")
	time.sleep(1.397)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(2.419)
	tracef.write(f"1269 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1269kbit")
	time.sleep(1.171)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(1.19)
	tracef.write(f"1255 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1255kbit")
	time.sleep(2.103)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(2.214)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(2.172)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(1.191)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(1.99)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(1.528)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(1.528)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()