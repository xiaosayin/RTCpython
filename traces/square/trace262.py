#t:2142-2541 ; rate:918-1463 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace262.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace262.txt", 'a+')
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1430kbit")
	time.sleep(2.531)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(2.221)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(2.287)
	tracef.write(f"1124 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1124kbit")
	time.sleep(2.227)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.441)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(2.419)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(2.338)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(2.167)
	tracef.write(f"1129 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1129kbit")
	time.sleep(2.223)
	tracef.write(f"1460 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1460kbit")
	time.sleep(2.519)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(2.268)
	tracef.write(f"1195 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1195kbit")
	time.sleep(2.438)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(2.416)
	tracef.write(f"979 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 979kbit")
	time.sleep(2.258)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(2.332)
	tracef.write(f"1335 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1335kbit")
	time.sleep(2.153)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(2.164)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(2.507)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(2.497)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(2.404)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(2.242)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(2.502)
	tracef.write(f"1025 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1025kbit")
	time.sleep(2.343)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(2.231)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(2.186)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.228)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.263)
	tracef.write(f"1144 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1144kbit")
	time.sleep(2.451)
	tracef.write(f"965 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 965kbit")
	time.sleep(2.492)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(2.209)
	tracef.write(f"1377 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1377kbit")
	time.sleep(2.248)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(2.374)
	tracef.write(f"993 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 993kbit")
	time.sleep(2.246)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.147)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(2.17)
	tracef.write(f"966 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 966kbit")
	time.sleep(2.148)
	tracef.write(f"1068 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1068kbit")
	time.sleep(2.379)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(2.534)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(2.504)
	tracef.write(f"1356 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1356kbit")
	time.sleep(2.348)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(2.228)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(2.228)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()