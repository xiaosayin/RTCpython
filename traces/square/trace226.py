#t:1276-2538 ; rate:1013-1362 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace226.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace226.txt", 'a+')
	tracef.write(f"1218 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1218kbit")
	time.sleep(2.295)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(1.775)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(1.779)
	tracef.write(f"1239 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1239kbit")
	time.sleep(1.685)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(2.403)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(2.122)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.781)
	tracef.write(f"1339 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1339kbit")
	time.sleep(1.723)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(2.415)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(2.405)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(1.748)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(1.694)
	tracef.write(f"1359 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1359kbit")
	time.sleep(2.236)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(1.373)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(1.304)
	tracef.write(f"1218 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1218kbit")
	time.sleep(1.502)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(1.777)
	tracef.write(f"1344 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1344kbit")
	time.sleep(2.171)
	tracef.write(f"1320 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1320kbit")
	time.sleep(2.332)
	tracef.write(f"1013 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1013kbit")
	time.sleep(1.909)
	tracef.write(f"1233 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1233kbit")
	time.sleep(1.336)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(1.343)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(2.114)
	tracef.write(f"1138 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1138kbit")
	time.sleep(2.095)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(1.881)
	tracef.write(f"1277 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1277kbit")
	time.sleep(2.178)
	tracef.write(f"1143 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1143kbit")
	time.sleep(2.2)
	tracef.write(f"1028 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1028kbit")
	time.sleep(1.86)
	tracef.write(f"1146 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1146kbit")
	time.sleep(1.714)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(1.611)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(2.268)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(1.776)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(1.623)
	tracef.write(f"1143 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1143kbit")
	time.sleep(1.852)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(1.487)
	tracef.write(f"1255 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1255kbit")
	time.sleep(2.06)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(2.245)
	tracef.write(f"1056 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1056kbit")
	time.sleep(2.369)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(1.558)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(1.391)
	tracef.write(f"1083 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1083kbit")
	time.sleep(1.53)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(2.087)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(1.995)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(2.462)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(1.758)
	tracef.write(f"1081 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1081kbit")
	time.sleep(1.732)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(1.446)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(2.402)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(2.296)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(2.488)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(2.488)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()