#t:1071-1414 ; rate:874-1571 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace286.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace286.txt", 'a+')
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1170kbit")
	time.sleep(1.092)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(1.088)
	tracef.write(f"1165 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1165kbit")
	time.sleep(1.385)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(1.25)
	tracef.write(f"1185 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1185kbit")
	time.sleep(1.365)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(1.4)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(1.191)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(1.238)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(1.352)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(1.375)
	tracef.write(f"1506 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1506kbit")
	time.sleep(1.229)
	tracef.write(f"1154 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1154kbit")
	time.sleep(1.155)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(1.34)
	tracef.write(f"1447 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1447kbit")
	time.sleep(1.272)
	tracef.write(f"978 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 978kbit")
	time.sleep(1.398)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(1.072)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(1.182)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(1.293)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(1.182)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(1.135)
	tracef.write(f"1292 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1292kbit")
	time.sleep(1.117)
	tracef.write(f"1499 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1499kbit")
	time.sleep(1.232)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(1.148)
	tracef.write(f"1149 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1149kbit")
	time.sleep(1.396)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(1.213)
	tracef.write(f"928 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 928kbit")
	time.sleep(1.248)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(1.382)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(1.24)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(1.283)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(1.209)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(1.271)
	tracef.write(f"1309 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1309kbit")
	time.sleep(1.346)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(1.118)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(1.359)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(1.126)
	tracef.write(f"1311 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1311kbit")
	time.sleep(1.1)
	tracef.write(f"1425 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1425kbit")
	time.sleep(1.323)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(1.106)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(1.126)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(1.249)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(1.281)
	tracef.write(f"1269 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1269kbit")
	time.sleep(1.354)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(1.286)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(1.085)
	tracef.write(f"1018 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1018kbit")
	time.sleep(1.071)
	tracef.write(f"962 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 962kbit")
	time.sleep(1.188)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(1.214)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(1.286)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(1.167)
	tracef.write(f"1108 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1108kbit")
	time.sleep(1.082)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(1.356)
	tracef.write(f"1566 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1566kbit")
	time.sleep(1.211)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(1.384)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(1.092)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(1.106)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(1.133)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(1.206)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(1.218)
	tracef.write(f"1143 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1143kbit")
	time.sleep(1.086)
	tracef.write(f"1350 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1350kbit")
	time.sleep(1.152)
	tracef.write(f"1273 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1273kbit")
	time.sleep(1.092)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(1.21)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(1.329)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(1.285)
	tracef.write(f"1237 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1237kbit")
	time.sleep(1.261)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(1.082)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(1.096)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(1.075)
	tracef.write(f"1343 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1343kbit")
	time.sleep(1.345)
	tracef.write(f"996 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 996kbit")
	time.sleep(1.218)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(1.209)
	tracef.write(f"1492 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1492kbit")
	time.sleep(1.184)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(1.125)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(1.327)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(1.411)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(1.248)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(1.204)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.099)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.099)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()