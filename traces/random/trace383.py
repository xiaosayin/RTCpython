#t:636-646 ; rate:766-2265 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace383.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace383.txt", 'a+')
	tracef.write(f"2026 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2026kbit")
	time.sleep(0.643)
	tracef.write(f"767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 767kbit")
	time.sleep(0.64)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.641)
	tracef.write(f"1577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1577kbit")
	time.sleep(0.642)
	tracef.write(f"850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 850kbit")
	time.sleep(0.642)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(0.646)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(0.636)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.642)
	tracef.write(f"2147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2147kbit")
	time.sleep(0.64)
	tracef.write(f"2170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2170kbit")
	time.sleep(0.638)
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1272kbit")
	time.sleep(0.641)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(0.638)
	tracef.write(f"780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 780kbit")
	time.sleep(0.638)
	tracef.write(f"1288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1288kbit")
	time.sleep(0.644)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.638)
	tracef.write(f"2082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2082kbit")
	time.sleep(0.639)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(0.638)
	tracef.write(f"1181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1181kbit")
	time.sleep(0.645)
	tracef.write(f"2149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2149kbit")
	time.sleep(0.644)
	tracef.write(f"2026 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2026kbit")
	time.sleep(0.645)
	tracef.write(f"2247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2247kbit")
	time.sleep(0.642)
	tracef.write(f"1981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1981kbit")
	time.sleep(0.644)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.643)
	tracef.write(f"1967 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1967kbit")
	time.sleep(0.646)
	tracef.write(f"2047 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2047kbit")
	time.sleep(0.636)
	tracef.write(f"823 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 823kbit")
	time.sleep(0.646)
	tracef.write(f"1734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1734kbit")
	time.sleep(0.639)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.641)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(0.639)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.646)
	tracef.write(f"1847 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1847kbit")
	time.sleep(0.639)
	tracef.write(f"1757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1757kbit")
	time.sleep(0.645)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(0.646)
	tracef.write(f"1119 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1119kbit")
	time.sleep(0.644)
	tracef.write(f"1618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1618kbit")
	time.sleep(0.646)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.642)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.637)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.643)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(0.645)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(0.637)
	tracef.write(f"825 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 825kbit")
	time.sleep(0.64)
	tracef.write(f"1662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1662kbit")
	time.sleep(0.641)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(0.64)
	tracef.write(f"2144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2144kbit")
	time.sleep(0.639)
	tracef.write(f"2146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2146kbit")
	time.sleep(0.639)
	tracef.write(f"883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 883kbit")
	time.sleep(0.646)
	tracef.write(f"2068 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2068kbit")
	time.sleep(0.638)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.638)
	tracef.write(f"2137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2137kbit")
	time.sleep(0.636)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(0.646)
	tracef.write(f"1749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1749kbit")
	time.sleep(0.638)
	tracef.write(f"1660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1660kbit")
	time.sleep(0.642)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.639)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(0.646)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(0.64)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(0.638)
	tracef.write(f"1773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1773kbit")
	time.sleep(0.64)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.644)
	tracef.write(f"1988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1988kbit")
	time.sleep(0.639)
	tracef.write(f"2131 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2131kbit")
	time.sleep(0.638)
	tracef.write(f"891 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 891kbit")
	time.sleep(0.636)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(0.645)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.644)
	tracef.write(f"1812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1812kbit")
	time.sleep(0.646)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(0.637)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(0.644)
	tracef.write(f"986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 986kbit")
	time.sleep(0.636)
	tracef.write(f"1523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1523kbit")
	time.sleep(0.643)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(0.638)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(0.643)
	tracef.write(f"994 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 994kbit")
	time.sleep(0.645)
	tracef.write(f"2083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2083kbit")
	time.sleep(0.646)
	tracef.write(f"2015 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2015kbit")
	time.sleep(0.645)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(0.64)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.646)
	tracef.write(f"1842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1842kbit")
	time.sleep(0.641)
	tracef.write(f"2084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2084kbit")
	time.sleep(0.646)
	tracef.write(f"1840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1840kbit")
	time.sleep(0.644)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(0.642)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(0.636)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(0.637)
	tracef.write(f"1823 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1823kbit")
	time.sleep(0.641)
	tracef.write(f"993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 993kbit")
	time.sleep(0.641)
	tracef.write(f"1635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1635kbit")
	time.sleep(0.646)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.64)
	tracef.write(f"1952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1952kbit")
	time.sleep(0.638)
	tracef.write(f"1885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1885kbit")
	time.sleep(0.646)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(0.645)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.645)
	tracef.write(f"2205 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2205kbit")
	time.sleep(0.644)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.646)
	tracef.write(f"1686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1686kbit")
	time.sleep(0.641)
	tracef.write(f"1738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1738kbit")
	time.sleep(0.637)
	tracef.write(f"991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 991kbit")
	time.sleep(0.639)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(0.639)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.643)
	tracef.write(f"1928 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1928kbit")
	time.sleep(0.643)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.64)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.64)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.641)
	tracef.write(f"2183 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2183kbit")
	time.sleep(0.644)
	tracef.write(f"990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 990kbit")
	time.sleep(0.642)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.642)
	tracef.write(f"1333 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1333kbit")
	time.sleep(0.64)
	tracef.write(f"2198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2198kbit")
	time.sleep(0.644)
	tracef.write(f"1833 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1833kbit")
	time.sleep(0.641)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(0.643)
	tracef.write(f"1100 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1100kbit")
	time.sleep(0.636)
	tracef.write(f"1912 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1912kbit")
	time.sleep(0.641)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(0.643)
	tracef.write(f"1158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1158kbit")
	time.sleep(0.64)
	tracef.write(f"1100 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1100kbit")
	time.sleep(0.644)
	tracef.write(f"1677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1677kbit")
	time.sleep(0.64)
	tracef.write(f"1764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1764kbit")
	time.sleep(0.64)
	tracef.write(f"1802 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1802kbit")
	time.sleep(0.636)
	tracef.write(f"1985 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1985kbit")
	time.sleep(0.64)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.64)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.639)
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1676kbit")
	time.sleep(0.64)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(0.643)
	tracef.write(f"2227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2227kbit")
	time.sleep(0.638)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.639)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(0.637)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.639)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.645)
	tracef.write(f"2176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2176kbit")
	time.sleep(0.644)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(0.636)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.639)
	tracef.write(f"2161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2161kbit")
	time.sleep(0.646)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(0.644)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.644)
	tracef.write(f"1952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1952kbit")
	time.sleep(0.636)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.638)
	tracef.write(f"1840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1840kbit")
	time.sleep(0.637)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(0.636)
	tracef.write(f"1740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1740kbit")
	time.sleep(0.644)
	tracef.write(f"1730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1730kbit")
	time.sleep(0.643)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(0.643)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.646)
	tracef.write(f"2238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2238kbit")
	time.sleep(0.646)
	tracef.write(f"1890 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1890kbit")
	time.sleep(0.64)
	tracef.write(f"2190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2190kbit")
	time.sleep(0.642)
	tracef.write(f"1352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1352kbit")
	time.sleep(0.646)
	tracef.write(f"1520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1520kbit")
	time.sleep(0.639)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(0.637)
	tracef.write(f"929 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 929kbit")
	time.sleep(0.638)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(0.645)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.639)
	tracef.write(f"1343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1343kbit")
	time.sleep(0.646)
	tracef.write(f"2079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2079kbit")
	time.sleep(0.64)
	tracef.write(f"2237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2237kbit")
	time.sleep(0.643)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.636)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.642)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.637)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.646)
	tracef.write(f"2057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2057kbit")
	time.sleep(0.636)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()