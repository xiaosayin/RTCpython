#t:2341-2747 ; rate:887-1530 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace97.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace97.txt", 'a+')
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 976kbit")
	time.sleep(2.498)
	tracef.write(f"1339 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1339kbit")
	time.sleep(2.36)
	tracef.write(f"908 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 908kbit")
	time.sleep(2.663)
	tracef.write(f"1016 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1016kbit")
	time.sleep(2.716)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(2.561)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(2.741)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(2.642)
	tracef.write(f"1103 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1103kbit")
	time.sleep(2.405)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(2.639)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(2.597)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(2.506)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(2.524)
	tracef.write(f"1002 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1002kbit")
	time.sleep(2.5)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(2.617)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(2.377)
	tracef.write(f"1484 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1484kbit")
	time.sleep(2.741)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(2.41)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(2.726)
	tracef.write(f"1153 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1153kbit")
	time.sleep(2.63)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(2.542)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(2.51)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(2.652)
	tracef.write(f"966 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 966kbit")
	time.sleep(2.593)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(2.582)
	tracef.write(f"1228 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1228kbit")
	time.sleep(2.36)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(2.442)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(2.456)
	tracef.write(f"1379 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1379kbit")
	time.sleep(2.512)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(2.504)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(2.722)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(2.503)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(2.419)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(2.477)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(2.375)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(2.413)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(2.628)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(2.581)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(2.499)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(2.499)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()