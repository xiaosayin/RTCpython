#t:1966-2962 ; rate:1210-1269 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace129.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace129.txt", 'a+')
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1258kbit")
	time.sleep(2.923)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(2.527)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(2.495)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(1.992)
	tracef.write(f"1220 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1220kbit")
	time.sleep(1.976)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(2.674)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(2.034)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.737)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(2.824)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(2.818)
	tracef.write(f"1214 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1214kbit")
	time.sleep(2.387)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(2.199)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(2.849)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(2.312)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(2.176)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(2.88)
	tracef.write(f"1238 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1238kbit")
	time.sleep(2.873)
	tracef.write(f"1228 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1228kbit")
	time.sleep(2.205)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.178)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(2.012)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(2.864)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(2.323)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(2.233)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.347)
	tracef.write(f"1233 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1233kbit")
	time.sleep(2.736)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(2.743)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(2.337)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(2.366)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(2.529)
	tracef.write(f"1216 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1216kbit")
	time.sleep(2.895)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(2.72)
	tracef.write(f"1262 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1262kbit")
	time.sleep(2.745)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(2.101)
	tracef.write(f"1224 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1224kbit")
	time.sleep(2.239)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(2.777)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(2.012)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(2.891)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(1.988)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(2.632)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(2.632)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()