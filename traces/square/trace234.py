#t:1107-2783 ; rate:1106-1431 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace234.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace234.txt", 'a+')
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1398kbit")
	time.sleep(1.614)
	tracef.write(f"1237 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1237kbit")
	time.sleep(1.56)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(1.791)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(1.55)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(1.213)
	tracef.write(f"1166 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1166kbit")
	time.sleep(1.694)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(2.42)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(2.719)
	tracef.write(f"1178 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1178kbit")
	time.sleep(1.68)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(2.669)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(1.77)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(2.739)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(1.72)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(1.504)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(2.57)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(1.626)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(1.471)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(1.214)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(1.719)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(1.489)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(1.521)
	tracef.write(f"1129 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1129kbit")
	time.sleep(2.604)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(1.427)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(2.698)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(2.551)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(2.317)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(1.705)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(2.0)
	tracef.write(f"1216 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1216kbit")
	time.sleep(1.352)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(2.783)
	tracef.write(f"1127 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1127kbit")
	time.sleep(1.863)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(1.121)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(2.388)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(2.326)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(2.055)
	tracef.write(f"1186 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1186kbit")
	time.sleep(2.153)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(2.056)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(1.244)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(1.237)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(2.658)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(2.745)
	tracef.write(f"1269 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1269kbit")
	time.sleep(1.131)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(2.104)
	tracef.write(f"1314 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1314kbit")
	time.sleep(2.292)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(2.335)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(2.559)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(1.664)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(2.157)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(2.011)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(2.011)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()