#t:1119-2468 ; rate:907-1308 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace30.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace30.txt", 'a+')
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1284kbit")
	time.sleep(1.458)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(1.688)
	tracef.write(f"977 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 977kbit")
	time.sleep(2.393)
	tracef.write(f"1166 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1166kbit")
	time.sleep(2.281)
	tracef.write(f"1273 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1273kbit")
	time.sleep(1.405)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(2.456)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(1.643)
	tracef.write(f"1207 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1207kbit")
	time.sleep(1.818)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(1.797)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(2.413)
	tracef.write(f"972 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 972kbit")
	time.sleep(1.51)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(2.326)
	tracef.write(f"923 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 923kbit")
	time.sleep(1.411)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(2.012)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(1.709)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(2.307)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(1.181)
	tracef.write(f"910 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 910kbit")
	time.sleep(1.724)
	tracef.write(f"978 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 978kbit")
	time.sleep(2.098)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(2.09)
	tracef.write(f"1085 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1085kbit")
	time.sleep(1.761)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(1.517)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(2.041)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(1.543)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(2.114)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(1.594)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(2.2)
	tracef.write(f"1138 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1138kbit")
	time.sleep(1.13)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.307)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(1.155)
	tracef.write(f"1269 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1269kbit")
	time.sleep(1.872)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(1.267)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(1.306)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(2.464)
	tracef.write(f"1211 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1211kbit")
	time.sleep(2.221)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(1.934)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(2.307)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(2.092)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(1.848)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(1.12)
	tracef.write(f"990 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 990kbit")
	time.sleep(2.212)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(1.793)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(1.723)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(1.927)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(1.731)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(2.186)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(1.391)
	tracef.write(f"1096 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1096kbit")
	time.sleep(1.373)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(2.319)
	tracef.write(f"1132 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1132kbit")
	time.sleep(2.102)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(2.34)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(2.307)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(2.307)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()