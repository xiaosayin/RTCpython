#t:626-965 ; rate:766-2525 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace328.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace328.txt", 'a+')
	tracef.write(f"2511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2511kbit")
	time.sleep(0.826)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.678)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.627)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.954)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.826)
	tracef.write(f"2296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2296kbit")
	time.sleep(0.864)
	tracef.write(f"1826 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1826kbit")
	time.sleep(0.907)
	tracef.write(f"2324 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2324kbit")
	time.sleep(0.847)
	tracef.write(f"1722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1722kbit")
	time.sleep(0.726)
	tracef.write(f"877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 877kbit")
	time.sleep(0.706)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(0.667)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(0.844)
	tracef.write(f"793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 793kbit")
	time.sleep(0.95)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(0.772)
	tracef.write(f"2117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2117kbit")
	time.sleep(0.743)
	tracef.write(f"1921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1921kbit")
	time.sleep(0.945)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.962)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.766)
	tracef.write(f"2203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2203kbit")
	time.sleep(0.699)
	tracef.write(f"1082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1082kbit")
	time.sleep(0.877)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(0.931)
	tracef.write(f"2152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2152kbit")
	time.sleep(0.762)
	tracef.write(f"1775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1775kbit")
	time.sleep(0.632)
	tracef.write(f"1704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1704kbit")
	time.sleep(0.916)
	tracef.write(f"1764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1764kbit")
	time.sleep(0.803)
	tracef.write(f"1742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1742kbit")
	time.sleep(0.687)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.806)
	tracef.write(f"2262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2262kbit")
	time.sleep(0.774)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.892)
	tracef.write(f"1677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1677kbit")
	time.sleep(0.706)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(0.769)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.715)
	tracef.write(f"2063 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2063kbit")
	time.sleep(0.683)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(0.726)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.917)
	tracef.write(f"2348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2348kbit")
	time.sleep(0.965)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(0.859)
	tracef.write(f"1996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1996kbit")
	time.sleep(0.721)
	tracef.write(f"2166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2166kbit")
	time.sleep(0.961)
	tracef.write(f"1936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1936kbit")
	time.sleep(0.921)
	tracef.write(f"1379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1379kbit")
	time.sleep(0.838)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.844)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(0.761)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.8)
	tracef.write(f"2276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2276kbit")
	time.sleep(0.962)
	tracef.write(f"1719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1719kbit")
	time.sleep(0.727)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.819)
	tracef.write(f"2216 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2216kbit")
	time.sleep(0.71)
	tracef.write(f"1711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1711kbit")
	time.sleep(0.688)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.777)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(0.802)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.66)
	tracef.write(f"2190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2190kbit")
	time.sleep(0.657)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(0.709)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(0.651)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(0.963)
	tracef.write(f"2308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2308kbit")
	time.sleep(0.904)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.719)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.677)
	tracef.write(f"1809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1809kbit")
	time.sleep(0.908)
	tracef.write(f"1835 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1835kbit")
	time.sleep(0.642)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(0.697)
	tracef.write(f"805 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 805kbit")
	time.sleep(0.766)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(0.896)
	tracef.write(f"1536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1536kbit")
	time.sleep(0.943)
	tracef.write(f"2112 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2112kbit")
	time.sleep(0.688)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.711)
	tracef.write(f"1346 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1346kbit")
	time.sleep(0.764)
	tracef.write(f"2116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2116kbit")
	time.sleep(0.891)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.736)
	tracef.write(f"2191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2191kbit")
	time.sleep(0.754)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(0.801)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(0.961)
	tracef.write(f"1660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1660kbit")
	time.sleep(0.844)
	tracef.write(f"1382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1382kbit")
	time.sleep(0.77)
	tracef.write(f"864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 864kbit")
	time.sleep(0.695)
	tracef.write(f"2063 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2063kbit")
	time.sleep(0.915)
	tracef.write(f"2150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2150kbit")
	time.sleep(0.882)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.925)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.696)
	tracef.write(f"1897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1897kbit")
	time.sleep(0.717)
	tracef.write(f"1829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1829kbit")
	time.sleep(0.796)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(0.942)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.686)
	tracef.write(f"2176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2176kbit")
	time.sleep(0.707)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.846)
	tracef.write(f"966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 966kbit")
	time.sleep(0.933)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.953)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.958)
	tracef.write(f"2312 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2312kbit")
	time.sleep(0.781)
	tracef.write(f"2317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2317kbit")
	time.sleep(0.704)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(0.631)
	tracef.write(f"2430 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2430kbit")
	time.sleep(0.739)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(0.913)
	tracef.write(f"1067 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1067kbit")
	time.sleep(0.947)
	tracef.write(f"1942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1942kbit")
	time.sleep(0.641)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(0.804)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(0.627)
	tracef.write(f"810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 810kbit")
	time.sleep(0.847)
	tracef.write(f"2123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2123kbit")
	time.sleep(0.761)
	tracef.write(f"2420 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2420kbit")
	time.sleep(0.696)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(0.681)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(0.884)
	tracef.write(f"2041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2041kbit")
	time.sleep(0.791)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.759)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.948)
	tracef.write(f"2028 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2028kbit")
	time.sleep(0.68)
	tracef.write(f"1685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1685kbit")
	time.sleep(0.828)
	tracef.write(f"1523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1523kbit")
	time.sleep(0.807)
	tracef.write(f"914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 914kbit")
	time.sleep(0.953)
	tracef.write(f"2501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2501kbit")
	time.sleep(0.77)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.791)
	tracef.write(f"1927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1927kbit")
	time.sleep(0.824)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.954)
	tracef.write(f"2060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2060kbit")
	time.sleep(0.66)
	tracef.write(f"1425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1425kbit")
	time.sleep(0.679)
	tracef.write(f"1939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1939kbit")
	time.sleep(0.88)
	tracef.write(f"2238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2238kbit")
	time.sleep(0.631)
	tracef.write(f"808 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 808kbit")
	time.sleep(0.737)
	tracef.write(f"1839 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1839kbit")
	time.sleep(0.872)
	tracef.write(f"2040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2040kbit")
	time.sleep(0.697)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.831)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.8)
	tracef.write(f"1565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1565kbit")
	time.sleep(0.87)
	tracef.write(f"2349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2349kbit")
	time.sleep(0.957)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.87)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()