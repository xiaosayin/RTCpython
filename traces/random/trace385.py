#t:645-668 ; rate:806-2233 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace385.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace385.txt", 'a+')
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1676kbit")
	time.sleep(0.649)
	tracef.write(f"1991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1991kbit")
	time.sleep(0.653)
	tracef.write(f"1932 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1932kbit")
	time.sleep(0.667)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.662)
	tracef.write(f"1730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1730kbit")
	time.sleep(0.655)
	tracef.write(f"1868 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1868kbit")
	time.sleep(0.654)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.668)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.656)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(0.657)
	tracef.write(f"1966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1966kbit")
	time.sleep(0.666)
	tracef.write(f"1159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1159kbit")
	time.sleep(0.65)
	tracef.write(f"1288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1288kbit")
	time.sleep(0.66)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.662)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(0.647)
	tracef.write(f"2084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2084kbit")
	time.sleep(0.659)
	tracef.write(f"1323 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1323kbit")
	time.sleep(0.659)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.647)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(0.665)
	tracef.write(f"2141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2141kbit")
	time.sleep(0.664)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.645)
	tracef.write(f"1237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1237kbit")
	time.sleep(0.66)
	tracef.write(f"1101 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1101kbit")
	time.sleep(0.654)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(0.65)
	tracef.write(f"974 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 974kbit")
	time.sleep(0.647)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(0.654)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.652)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.646)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.655)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.663)
	tracef.write(f"2183 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2183kbit")
	time.sleep(0.667)
	tracef.write(f"1943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1943kbit")
	time.sleep(0.658)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(0.655)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.645)
	tracef.write(f"1739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1739kbit")
	time.sleep(0.648)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(0.655)
	tracef.write(f"1963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1963kbit")
	time.sleep(0.666)
	tracef.write(f"1158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1158kbit")
	time.sleep(0.647)
	tracef.write(f"831 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 831kbit")
	time.sleep(0.647)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.668)
	tracef.write(f"1579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1579kbit")
	time.sleep(0.666)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.665)
	tracef.write(f"2140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2140kbit")
	time.sleep(0.668)
	tracef.write(f"1664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1664kbit")
	time.sleep(0.657)
	tracef.write(f"1545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1545kbit")
	time.sleep(0.645)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.654)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(0.667)
	tracef.write(f"1682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1682kbit")
	time.sleep(0.664)
	tracef.write(f"1530 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1530kbit")
	time.sleep(0.667)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(0.645)
	tracef.write(f"830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 830kbit")
	time.sleep(0.661)
	tracef.write(f"1050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1050kbit")
	time.sleep(0.652)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.656)
	tracef.write(f"2050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2050kbit")
	time.sleep(0.653)
	tracef.write(f"1234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1234kbit")
	time.sleep(0.652)
	tracef.write(f"1881 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1881kbit")
	time.sleep(0.651)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.666)
	tracef.write(f"2222 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2222kbit")
	time.sleep(0.666)
	tracef.write(f"1332 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1332kbit")
	time.sleep(0.666)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.665)
	tracef.write(f"1509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1509kbit")
	time.sleep(0.648)
	tracef.write(f"1829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1829kbit")
	time.sleep(0.667)
	tracef.write(f"1946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1946kbit")
	time.sleep(0.658)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.664)
	tracef.write(f"1224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1224kbit")
	time.sleep(0.666)
	tracef.write(f"1050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1050kbit")
	time.sleep(0.66)
	tracef.write(f"2009 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2009kbit")
	time.sleep(0.665)
	tracef.write(f"1678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1678kbit")
	time.sleep(0.657)
	tracef.write(f"2022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2022kbit")
	time.sleep(0.663)
	tracef.write(f"1352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1352kbit")
	time.sleep(0.65)
	tracef.write(f"1462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1462kbit")
	time.sleep(0.661)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(0.657)
	tracef.write(f"1977 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1977kbit")
	time.sleep(0.651)
	tracef.write(f"1947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1947kbit")
	time.sleep(0.645)
	tracef.write(f"887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 887kbit")
	time.sleep(0.667)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.647)
	tracef.write(f"902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 902kbit")
	time.sleep(0.655)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(0.667)
	tracef.write(f"1092 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1092kbit")
	time.sleep(0.664)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.65)
	tracef.write(f"1049 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1049kbit")
	time.sleep(0.658)
	tracef.write(f"1495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1495kbit")
	time.sleep(0.647)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.668)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.667)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(0.649)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.652)
	tracef.write(f"1979 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1979kbit")
	time.sleep(0.651)
	tracef.write(f"1792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1792kbit")
	time.sleep(0.648)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.653)
	tracef.write(f"1848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1848kbit")
	time.sleep(0.661)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.66)
	tracef.write(f"1659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1659kbit")
	time.sleep(0.665)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.653)
	tracef.write(f"888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 888kbit")
	time.sleep(0.662)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(0.656)
	tracef.write(f"1498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1498kbit")
	time.sleep(0.656)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(0.663)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(0.661)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.66)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.664)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(0.65)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(0.652)
	tracef.write(f"1656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1656kbit")
	time.sleep(0.659)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.668)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.665)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(0.659)
	tracef.write(f"2160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2160kbit")
	time.sleep(0.665)
	tracef.write(f"1682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1682kbit")
	time.sleep(0.645)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(0.652)
	tracef.write(f"2036 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2036kbit")
	time.sleep(0.66)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.651)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.65)
	tracef.write(f"2064 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2064kbit")
	time.sleep(0.645)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.653)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(0.645)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(0.657)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(0.661)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(0.649)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(0.65)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(0.647)
	tracef.write(f"1718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1718kbit")
	time.sleep(0.647)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.663)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(0.649)
	tracef.write(f"1836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1836kbit")
	time.sleep(0.661)
	tracef.write(f"842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 842kbit")
	time.sleep(0.647)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.646)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(0.656)
	tracef.write(f"1963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1963kbit")
	time.sleep(0.646)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.653)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(0.647)
	tracef.write(f"844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 844kbit")
	time.sleep(0.664)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(0.652)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(0.653)
	tracef.write(f"2133 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2133kbit")
	time.sleep(0.645)
	tracef.write(f"1725 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1725kbit")
	time.sleep(0.667)
	tracef.write(f"2175 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2175kbit")
	time.sleep(0.666)
	tracef.write(f"1811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1811kbit")
	time.sleep(0.655)
	tracef.write(f"1922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1922kbit")
	time.sleep(0.66)
	tracef.write(f"1571 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1571kbit")
	time.sleep(0.65)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(0.647)
	tracef.write(f"2102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2102kbit")
	time.sleep(0.661)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(0.648)
	tracef.write(f"1827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1827kbit")
	time.sleep(0.648)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(0.659)
	tracef.write(f"1935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1935kbit")
	time.sleep(0.652)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(0.661)
	tracef.write(f"839 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 839kbit")
	time.sleep(0.645)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.655)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(0.664)
	tracef.write(f"858 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 858kbit")
	time.sleep(0.649)
	tracef.write(f"1706 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1706kbit")
	time.sleep(0.649)
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1511kbit")
	time.sleep(0.668)
	tracef.write(f"1682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1682kbit")
	time.sleep(0.65)
	tracef.write(f"1812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1812kbit")
	time.sleep(0.652)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()