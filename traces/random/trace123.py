#t:119-788 ; rate:951-1802 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace123.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace123.txt", 'a+')
	tracef.write(f"1350 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1350kbit")
	time.sleep(0.585)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(0.543)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.483)
	tracef.write(f"1544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1544kbit")
	time.sleep(0.442)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(0.47)
	tracef.write(f"1158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1158kbit")
	time.sleep(0.173)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.334)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(0.744)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(0.183)
	tracef.write(f"995 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 995kbit")
	time.sleep(0.23)
	tracef.write(f"1745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1745kbit")
	time.sleep(0.191)
	tracef.write(f"1725 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1725kbit")
	time.sleep(0.634)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(0.528)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.555)
	tracef.write(f"1120 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1120kbit")
	time.sleep(0.418)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(0.748)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.526)
	tracef.write(f"1185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1185kbit")
	time.sleep(0.533)
	tracef.write(f"1730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1730kbit")
	time.sleep(0.52)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(0.39)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(0.142)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(0.486)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.638)
	tracef.write(f"1708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1708kbit")
	time.sleep(0.783)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.582)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(0.277)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(0.626)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.785)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(0.139)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.226)
	tracef.write(f"1211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1211kbit")
	time.sleep(0.196)
	tracef.write(f"1744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1744kbit")
	time.sleep(0.434)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(0.393)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(0.462)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(0.462)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(0.728)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(0.546)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.458)
	tracef.write(f"1092 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1092kbit")
	time.sleep(0.497)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(0.4)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.588)
	tracef.write(f"1675 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1675kbit")
	time.sleep(0.218)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(0.27)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.553)
	tracef.write(f"1016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1016kbit")
	time.sleep(0.675)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(0.605)
	tracef.write(f"997 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 997kbit")
	time.sleep(0.648)
	tracef.write(f"1149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1149kbit")
	time.sleep(0.245)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.213)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.477)
	tracef.write(f"1591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1591kbit")
	time.sleep(0.141)
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1272kbit")
	time.sleep(0.785)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.608)
	tracef.write(f"1801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1801kbit")
	time.sleep(0.745)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.18)
	tracef.write(f"1165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1165kbit")
	time.sleep(0.584)
	tracef.write(f"1446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1446kbit")
	time.sleep(0.192)
	tracef.write(f"1138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1138kbit")
	time.sleep(0.283)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.593)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.148)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(0.75)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(0.429)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(0.382)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(0.267)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.357)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(0.454)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(0.528)
	tracef.write(f"1159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1159kbit")
	time.sleep(0.415)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(0.743)
	tracef.write(f"1696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1696kbit")
	time.sleep(0.245)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(0.178)
	tracef.write(f"989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 989kbit")
	time.sleep(0.196)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(0.243)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.171)
	tracef.write(f"1785 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1785kbit")
	time.sleep(0.6)
	tracef.write(f"1513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1513kbit")
	time.sleep(0.578)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(0.401)
	tracef.write(f"1020 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1020kbit")
	time.sleep(0.656)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.562)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(0.158)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(0.372)
	tracef.write(f"1083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1083kbit")
	time.sleep(0.194)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.33)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.347)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.122)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.163)
	tracef.write(f"977 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 977kbit")
	time.sleep(0.407)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(0.71)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.737)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(0.231)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(0.679)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.675)
	tracef.write(f"1703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1703kbit")
	time.sleep(0.627)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(0.283)
	tracef.write(f"1688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1688kbit")
	time.sleep(0.559)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(0.721)
	tracef.write(f"1577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1577kbit")
	time.sleep(0.231)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.154)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.409)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(0.142)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(0.475)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.596)
	tracef.write(f"1340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1340kbit")
	time.sleep(0.32)
	tracef.write(f"1178 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1178kbit")
	time.sleep(0.697)
	tracef.write(f"1228 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1228kbit")
	time.sleep(0.284)
	tracef.write(f"1701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1701kbit")
	time.sleep(0.512)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.281)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.379)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(0.575)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.119)
	tracef.write(f"1728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1728kbit")
	time.sleep(0.238)
	tracef.write(f"1665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1665kbit")
	time.sleep(0.207)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(0.668)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.226)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.396)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.121)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(0.386)
	tracef.write(f"1756 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1756kbit")
	time.sleep(0.138)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(0.221)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(0.733)
	tracef.write(f"1704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1704kbit")
	time.sleep(0.591)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(0.158)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(0.744)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.747)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.261)
	tracef.write(f"1069 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1069kbit")
	time.sleep(0.227)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.732)
	tracef.write(f"1565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1565kbit")
	time.sleep(0.483)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(0.755)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(0.465)
	tracef.write(f"1654 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1654kbit")
	time.sleep(0.252)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(0.453)
	tracef.write(f"1215 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1215kbit")
	time.sleep(0.449)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.349)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(0.202)
	tracef.write(f"1352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1352kbit")
	time.sleep(0.281)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.766)
	tracef.write(f"1484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1484kbit")
	time.sleep(0.215)
	tracef.write(f"1716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1716kbit")
	time.sleep(0.389)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(0.125)
	tracef.write(f"1800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1800kbit")
	time.sleep(0.46)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(0.433)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(0.68)
	tracef.write(f"1687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1687kbit")
	time.sleep(0.374)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.773)
	tracef.write(f"964 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 964kbit")
	time.sleep(0.484)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(0.78)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.44)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.232)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(0.714)
	tracef.write(f"1791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1791kbit")
	time.sleep(0.182)
	tracef.write(f"1091 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1091kbit")
	time.sleep(0.589)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.378)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(0.338)
	tracef.write(f"963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 963kbit")
	time.sleep(0.669)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(0.589)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(0.453)
	tracef.write(f"1698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1698kbit")
	time.sleep(0.641)
	tracef.write(f"1685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1685kbit")
	time.sleep(0.243)
	tracef.write(f"1315 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1315kbit")
	time.sleep(0.655)
	tracef.write(f"1776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1776kbit")
	time.sleep(0.704)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(0.749)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.161)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.215)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.437)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(0.514)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.782)
	tracef.write(f"1203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1203kbit")
	time.sleep(0.64)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(0.633)
	tracef.write(f"1534 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1534kbit")
	time.sleep(0.454)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(0.19)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.309)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.76)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(0.562)
	tracef.write(f"1421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1421kbit")
	time.sleep(0.697)
	tracef.write(f"1103 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1103kbit")
	time.sleep(0.174)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.129)
	tracef.write(f"1745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1745kbit")
	time.sleep(0.176)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(0.712)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(0.311)
	tracef.write(f"957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 957kbit")
	time.sleep(0.125)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.761)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(0.261)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(0.355)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.677)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.53)
	tracef.write(f"1215 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1215kbit")
	time.sleep(0.438)
	tracef.write(f"1002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1002kbit")
	time.sleep(0.495)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.395)
	tracef.write(f"1029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1029kbit")
	time.sleep(0.683)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(0.301)
	tracef.write(f"1052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1052kbit")
	time.sleep(0.715)
	tracef.write(f"1709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1709kbit")
	time.sleep(0.166)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(0.74)
	tracef.write(f"1793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1793kbit")
	time.sleep(0.549)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.341)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(0.471)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(0.219)
	tracef.write(f"1792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1792kbit")
	time.sleep(0.163)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.454)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(0.683)
	tracef.write(f"1786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1786kbit")
	time.sleep(0.447)
	tracef.write(f"1745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1745kbit")
	time.sleep(0.473)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.361)
	tracef.write(f"1656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1656kbit")
	time.sleep(0.667)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(0.739)
	tracef.write(f"1519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1519kbit")
	time.sleep(0.544)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(0.373)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.527)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.558)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(0.418)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(0.361)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(0.63)
	tracef.write(f"1343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1343kbit")
	time.sleep(0.168)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(0.323)
	tracef.write(f"1623 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1623kbit")
	time.sleep(0.581)
	tracef.write(f"1220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1220kbit")
	time.sleep(0.427)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(0.52)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.693)
	tracef.write(f"1751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1751kbit")
	time.sleep(0.39)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.301)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.414)
	tracef.write(f"1047 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1047kbit")
	time.sleep(0.158)
	tracef.write(f"1207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1207kbit")
	time.sleep(0.591)
	tracef.write(f"1574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1574kbit")
	time.sleep(0.19)
	tracef.write(f"1402 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1402kbit")
	time.sleep(0.465)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()