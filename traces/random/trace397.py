#t:379-429 ; rate:1150-2501 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace397.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace397.txt", 'a+')
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1272kbit")
	time.sleep(0.406)
	tracef.write(f"2037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2037kbit")
	time.sleep(0.379)
	tracef.write(f"1736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1736kbit")
	time.sleep(0.425)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(0.419)
	tracef.write(f"1669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1669kbit")
	time.sleep(0.418)
	tracef.write(f"2267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2267kbit")
	time.sleep(0.393)
	tracef.write(f"2138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2138kbit")
	time.sleep(0.389)
	tracef.write(f"2287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2287kbit")
	time.sleep(0.393)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.409)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.383)
	tracef.write(f"1817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1817kbit")
	time.sleep(0.396)
	tracef.write(f"2354 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2354kbit")
	time.sleep(0.394)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.391)
	tracef.write(f"2019 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2019kbit")
	time.sleep(0.383)
	tracef.write(f"1841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1841kbit")
	time.sleep(0.396)
	tracef.write(f"1927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1927kbit")
	time.sleep(0.402)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.384)
	tracef.write(f"1723 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1723kbit")
	time.sleep(0.425)
	tracef.write(f"2150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2150kbit")
	time.sleep(0.403)
	tracef.write(f"1937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1937kbit")
	time.sleep(0.4)
	tracef.write(f"2225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2225kbit")
	time.sleep(0.406)
	tracef.write(f"1877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1877kbit")
	time.sleep(0.38)
	tracef.write(f"1732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1732kbit")
	time.sleep(0.417)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(0.409)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.38)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.402)
	tracef.write(f"1387 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1387kbit")
	time.sleep(0.405)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(0.389)
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2381kbit")
	time.sleep(0.422)
	tracef.write(f"1753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1753kbit")
	time.sleep(0.393)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.392)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(0.381)
	tracef.write(f"2104 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2104kbit")
	time.sleep(0.408)
	tracef.write(f"1579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1579kbit")
	time.sleep(0.392)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.415)
	tracef.write(f"1800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1800kbit")
	time.sleep(0.389)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(0.388)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.388)
	tracef.write(f"2044 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2044kbit")
	time.sleep(0.393)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(0.391)
	tracef.write(f"2050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2050kbit")
	time.sleep(0.407)
	tracef.write(f"1697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1697kbit")
	time.sleep(0.429)
	tracef.write(f"1801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1801kbit")
	time.sleep(0.421)
	tracef.write(f"1750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1750kbit")
	time.sleep(0.389)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.382)
	tracef.write(f"1786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1786kbit")
	time.sleep(0.41)
	tracef.write(f"1460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1460kbit")
	time.sleep(0.406)
	tracef.write(f"1349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1349kbit")
	time.sleep(0.406)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.419)
	tracef.write(f"1824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1824kbit")
	time.sleep(0.394)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(0.381)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(0.428)
	tracef.write(f"2342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2342kbit")
	time.sleep(0.387)
	tracef.write(f"1912 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1912kbit")
	time.sleep(0.395)
	tracef.write(f"2392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2392kbit")
	time.sleep(0.385)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.395)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(0.401)
	tracef.write(f"1425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1425kbit")
	time.sleep(0.4)
	tracef.write(f"1875 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1875kbit")
	time.sleep(0.424)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.387)
	tracef.write(f"1690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1690kbit")
	time.sleep(0.404)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.418)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.412)
	tracef.write(f"1820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1820kbit")
	time.sleep(0.425)
	tracef.write(f"2071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2071kbit")
	time.sleep(0.422)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.427)
	tracef.write(f"2040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2040kbit")
	time.sleep(0.388)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.399)
	tracef.write(f"2083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2083kbit")
	time.sleep(0.412)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.394)
	tracef.write(f"2440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2440kbit")
	time.sleep(0.413)
	tracef.write(f"1487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1487kbit")
	time.sleep(0.41)
	tracef.write(f"1889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1889kbit")
	time.sleep(0.388)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.416)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(0.41)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(0.429)
	tracef.write(f"1838 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1838kbit")
	time.sleep(0.386)
	tracef.write(f"1812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1812kbit")
	time.sleep(0.421)
	tracef.write(f"1275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1275kbit")
	time.sleep(0.388)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.387)
	tracef.write(f"1832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1832kbit")
	time.sleep(0.417)
	tracef.write(f"1678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1678kbit")
	time.sleep(0.401)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.386)
	tracef.write(f"2419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2419kbit")
	time.sleep(0.416)
	tracef.write(f"1851 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1851kbit")
	time.sleep(0.394)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.426)
	tracef.write(f"2478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2478kbit")
	time.sleep(0.381)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.414)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(0.405)
	tracef.write(f"1604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1604kbit")
	time.sleep(0.41)
	tracef.write(f"2186 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2186kbit")
	time.sleep(0.421)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.427)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(0.401)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.381)
	tracef.write(f"1666 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1666kbit")
	time.sleep(0.394)
	tracef.write(f"1447 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1447kbit")
	time.sleep(0.409)
	tracef.write(f"1690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1690kbit")
	time.sleep(0.41)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(0.383)
	tracef.write(f"2035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2035kbit")
	time.sleep(0.407)
	tracef.write(f"1245 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1245kbit")
	time.sleep(0.386)
	tracef.write(f"1669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1669kbit")
	time.sleep(0.407)
	tracef.write(f"1336 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1336kbit")
	time.sleep(0.418)
	tracef.write(f"1635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1635kbit")
	time.sleep(0.421)
	tracef.write(f"2316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2316kbit")
	time.sleep(0.395)
	tracef.write(f"2069 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2069kbit")
	time.sleep(0.379)
	tracef.write(f"1726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1726kbit")
	time.sleep(0.411)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.389)
	tracef.write(f"1778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1778kbit")
	time.sleep(0.417)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(0.39)
	tracef.write(f"1688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1688kbit")
	time.sleep(0.399)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.416)
	tracef.write(f"2001 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2001kbit")
	time.sleep(0.402)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(0.383)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.427)
	tracef.write(f"2248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2248kbit")
	time.sleep(0.387)
	tracef.write(f"2344 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2344kbit")
	time.sleep(0.418)
	tracef.write(f"1854 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1854kbit")
	time.sleep(0.394)
	tracef.write(f"2267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2267kbit")
	time.sleep(0.424)
	tracef.write(f"1985 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1985kbit")
	time.sleep(0.381)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.412)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.395)
	tracef.write(f"2090 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2090kbit")
	time.sleep(0.394)
	tracef.write(f"2085 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2085kbit")
	time.sleep(0.388)
	tracef.write(f"2226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2226kbit")
	time.sleep(0.398)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(0.383)
	tracef.write(f"1708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1708kbit")
	time.sleep(0.389)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.417)
	tracef.write(f"2007 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2007kbit")
	time.sleep(0.419)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.38)
	tracef.write(f"1839 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1839kbit")
	time.sleep(0.419)
	tracef.write(f"2149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2149kbit")
	time.sleep(0.393)
	tracef.write(f"2357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2357kbit")
	time.sleep(0.405)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(0.418)
	tracef.write(f"1828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1828kbit")
	time.sleep(0.384)
	tracef.write(f"2493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2493kbit")
	time.sleep(0.405)
	tracef.write(f"2328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2328kbit")
	time.sleep(0.42)
	tracef.write(f"2127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2127kbit")
	time.sleep(0.385)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.407)
	tracef.write(f"2340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2340kbit")
	time.sleep(0.416)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.38)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.389)
	tracef.write(f"1513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1513kbit")
	time.sleep(0.392)
	tracef.write(f"1727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1727kbit")
	time.sleep(0.401)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.394)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.386)
	tracef.write(f"2308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2308kbit")
	time.sleep(0.395)
	tracef.write(f"2484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2484kbit")
	time.sleep(0.38)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.406)
	tracef.write(f"2030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2030kbit")
	time.sleep(0.402)
	tracef.write(f"1584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1584kbit")
	time.sleep(0.4)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.384)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.393)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.4)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(0.385)
	tracef.write(f"2114 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2114kbit")
	time.sleep(0.379)
	tracef.write(f"2031 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2031kbit")
	time.sleep(0.393)
	tracef.write(f"2249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2249kbit")
	time.sleep(0.395)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.405)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.379)
	tracef.write(f"1711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1711kbit")
	time.sleep(0.406)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.417)
	tracef.write(f"1166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1166kbit")
	time.sleep(0.399)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.383)
	tracef.write(f"2129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2129kbit")
	time.sleep(0.427)
	tracef.write(f"1623 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1623kbit")
	time.sleep(0.428)
	tracef.write(f"2091 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2091kbit")
	time.sleep(0.405)
	tracef.write(f"2447 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2447kbit")
	time.sleep(0.42)
	tracef.write(f"2064 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2064kbit")
	time.sleep(0.386)
	tracef.write(f"1394 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1394kbit")
	time.sleep(0.423)
	tracef.write(f"1831 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1831kbit")
	time.sleep(0.427)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.416)
	tracef.write(f"1953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1953kbit")
	time.sleep(0.423)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.412)
	tracef.write(f"2200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2200kbit")
	time.sleep(0.429)
	tracef.write(f"2174 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2174kbit")
	time.sleep(0.427)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(0.41)
	tracef.write(f"1568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1568kbit")
	time.sleep(0.421)
	tracef.write(f"2272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2272kbit")
	time.sleep(0.404)
	tracef.write(f"2108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2108kbit")
	time.sleep(0.38)
	tracef.write(f"2439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2439kbit")
	time.sleep(0.384)
	tracef.write(f"1360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1360kbit")
	time.sleep(0.382)
	tracef.write(f"2044 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2044kbit")
	time.sleep(0.415)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.417)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.406)
	tracef.write(f"1993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1993kbit")
	time.sleep(0.393)
	tracef.write(f"2400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2400kbit")
	time.sleep(0.397)
	tracef.write(f"2079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2079kbit")
	time.sleep(0.421)
	tracef.write(f"1728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1728kbit")
	time.sleep(0.383)
	tracef.write(f"2138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2138kbit")
	time.sleep(0.395)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(0.388)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.385)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(0.389)
	tracef.write(f"2124 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2124kbit")
	time.sleep(0.423)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.382)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.419)
	tracef.write(f"2122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2122kbit")
	time.sleep(0.393)
	tracef.write(f"2235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2235kbit")
	time.sleep(0.416)
	tracef.write(f"1224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1224kbit")
	time.sleep(0.414)
	tracef.write(f"2408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2408kbit")
	time.sleep(0.427)
	tracef.write(f"2439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2439kbit")
	time.sleep(0.385)
	tracef.write(f"2169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2169kbit")
	time.sleep(0.418)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(0.399)
	tracef.write(f"1972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1972kbit")
	time.sleep(0.399)
	tracef.write(f"1811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1811kbit")
	time.sleep(0.386)
	tracef.write(f"2377 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2377kbit")
	time.sleep(0.39)
	tracef.write(f"1940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1940kbit")
	time.sleep(0.38)
	tracef.write(f"1609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1609kbit")
	time.sleep(0.408)
	tracef.write(f"2142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2142kbit")
	time.sleep(0.409)
	tracef.write(f"1344 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1344kbit")
	time.sleep(0.428)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(0.381)
	tracef.write(f"1963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1963kbit")
	time.sleep(0.406)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.429)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.381)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.408)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(0.39)
	tracef.write(f"1853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1853kbit")
	time.sleep(0.425)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.415)
	tracef.write(f"1773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1773kbit")
	time.sleep(0.383)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(0.426)
	tracef.write(f"2076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2076kbit")
	time.sleep(0.381)
	tracef.write(f"1783 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1783kbit")
	time.sleep(0.414)
	tracef.write(f"1168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1168kbit")
	time.sleep(0.405)
	tracef.write(f"2030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2030kbit")
	time.sleep(0.401)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.429)
	tracef.write(f"1528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1528kbit")
	time.sleep(0.416)
	tracef.write(f"1963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1963kbit")
	time.sleep(0.427)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.416)
	tracef.write(f"2181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2181kbit")
	time.sleep(0.426)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(0.401)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(0.419)
	tracef.write(f"2179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2179kbit")
	time.sleep(0.418)
	tracef.write(f"2019 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2019kbit")
	time.sleep(0.406)
	tracef.write(f"1780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1780kbit")
	time.sleep(0.426)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.385)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.426)
	tracef.write(f"1777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1777kbit")
	time.sleep(0.399)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.41)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(0.393)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.404)
	tracef.write(f"1542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1542kbit")
	time.sleep(0.395)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.414)
	tracef.write(f"2111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2111kbit")
	time.sleep(0.4)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(0.418)
	tracef.write(f"1214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1214kbit")
	time.sleep(0.381)
	tracef.write(f"1997 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1997kbit")
	time.sleep(0.404)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.381)
	tracef.write(f"2319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2319kbit")
	time.sleep(0.426)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(0.405)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(0.398)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()