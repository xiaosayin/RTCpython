#t:2403-2642 ; rate:1048-1557 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace381.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace381.txt", 'a+')
	tracef.write(f"1520 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1520kbit")
	time.sleep(2.438)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(2.517)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(2.513)
	tracef.write(f"1277 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1277kbit")
	time.sleep(2.615)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(2.52)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(2.434)
	tracef.write(f"1420 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1420kbit")
	time.sleep(2.418)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(2.46)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(2.565)
	tracef.write(f"1262 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1262kbit")
	time.sleep(2.416)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(2.444)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(2.483)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(2.454)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(2.579)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(2.451)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(2.455)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(2.452)
	tracef.write(f"1371 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1371kbit")
	time.sleep(2.549)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(2.532)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(2.633)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(2.476)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(2.574)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(2.451)
	tracef.write(f"1358 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1358kbit")
	time.sleep(2.439)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(2.472)
	tracef.write(f"1373 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1373kbit")
	time.sleep(2.533)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(2.441)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(2.636)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(2.596)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.507)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(2.468)
	tracef.write(f"1113 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1113kbit")
	time.sleep(2.448)
	tracef.write(f"1080 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1080kbit")
	time.sleep(2.633)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(2.485)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(2.439)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(2.42)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(2.494)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.567)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.567)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()