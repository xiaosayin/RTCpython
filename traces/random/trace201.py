#t:493-562 ; rate:1225-2975 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace201.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace201.txt", 'a+')
	tracef.write(f"1726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1726kbit")
	time.sleep(0.537)
	tracef.write(f"2903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2903kbit")
	time.sleep(0.537)
	tracef.write(f"2369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2369kbit")
	time.sleep(0.519)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(0.519)
	tracef.write(f"2635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2635kbit")
	time.sleep(0.536)
	tracef.write(f"2593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2593kbit")
	time.sleep(0.531)
	tracef.write(f"2272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2272kbit")
	time.sleep(0.498)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.508)
	tracef.write(f"1750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1750kbit")
	time.sleep(0.56)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.533)
	tracef.write(f"2247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2247kbit")
	time.sleep(0.518)
	tracef.write(f"2141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2141kbit")
	time.sleep(0.513)
	tracef.write(f"1450 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1450kbit")
	time.sleep(0.532)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(0.514)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.558)
	tracef.write(f"1824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1824kbit")
	time.sleep(0.493)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.523)
	tracef.write(f"1723 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1723kbit")
	time.sleep(0.542)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.543)
	tracef.write(f"2258 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2258kbit")
	time.sleep(0.523)
	tracef.write(f"2253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2253kbit")
	time.sleep(0.51)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.514)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(0.549)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.499)
	tracef.write(f"2213 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2213kbit")
	time.sleep(0.548)
	tracef.write(f"2175 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2175kbit")
	time.sleep(0.521)
	tracef.write(f"2158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2158kbit")
	time.sleep(0.513)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(0.559)
	tracef.write(f"1454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1454kbit")
	time.sleep(0.5)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.56)
	tracef.write(f"2596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2596kbit")
	time.sleep(0.543)
	tracef.write(f"2471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2471kbit")
	time.sleep(0.527)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.503)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.507)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.514)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.53)
	tracef.write(f"2345 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2345kbit")
	time.sleep(0.551)
	tracef.write(f"2516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2516kbit")
	time.sleep(0.531)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.501)
	tracef.write(f"1717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1717kbit")
	time.sleep(0.523)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.534)
	tracef.write(f"1810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1810kbit")
	time.sleep(0.495)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.521)
	tracef.write(f"1381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1381kbit")
	time.sleep(0.521)
	tracef.write(f"2673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2673kbit")
	time.sleep(0.554)
	tracef.write(f"2950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2950kbit")
	time.sleep(0.528)
	tracef.write(f"2350 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2350kbit")
	time.sleep(0.549)
	tracef.write(f"1983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1983kbit")
	time.sleep(0.541)
	tracef.write(f"2682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2682kbit")
	time.sleep(0.56)
	tracef.write(f"2046 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2046kbit")
	time.sleep(0.542)
	tracef.write(f"1985 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1985kbit")
	time.sleep(0.528)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.505)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.539)
	tracef.write(f"2974 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2974kbit")
	time.sleep(0.542)
	tracef.write(f"2770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2770kbit")
	time.sleep(0.545)
	tracef.write(f"1785 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1785kbit")
	time.sleep(0.548)
	tracef.write(f"2173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2173kbit")
	time.sleep(0.528)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.5)
	tracef.write(f"2021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2021kbit")
	time.sleep(0.525)
	tracef.write(f"2495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2495kbit")
	time.sleep(0.555)
	tracef.write(f"2117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2117kbit")
	time.sleep(0.533)
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1272kbit")
	time.sleep(0.559)
	tracef.write(f"1830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1830kbit")
	time.sleep(0.505)
	tracef.write(f"2248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2248kbit")
	time.sleep(0.551)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.527)
	tracef.write(f"2943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2943kbit")
	time.sleep(0.519)
	tracef.write(f"2187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2187kbit")
	time.sleep(0.537)
	tracef.write(f"1510 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1510kbit")
	time.sleep(0.523)
	tracef.write(f"1905 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1905kbit")
	time.sleep(0.52)
	tracef.write(f"2200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2200kbit")
	time.sleep(0.56)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.56)
	tracef.write(f"2376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2376kbit")
	time.sleep(0.559)
	tracef.write(f"1825 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1825kbit")
	time.sleep(0.55)
	tracef.write(f"1738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1738kbit")
	time.sleep(0.498)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(0.526)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(0.54)
	tracef.write(f"2083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2083kbit")
	time.sleep(0.503)
	tracef.write(f"2041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2041kbit")
	time.sleep(0.56)
	tracef.write(f"2364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2364kbit")
	time.sleep(0.519)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.513)
	tracef.write(f"2268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2268kbit")
	time.sleep(0.553)
	tracef.write(f"1825 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1825kbit")
	time.sleep(0.505)
	tracef.write(f"2824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2824kbit")
	time.sleep(0.496)
	tracef.write(f"2513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2513kbit")
	time.sleep(0.525)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(0.557)
	tracef.write(f"2166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2166kbit")
	time.sleep(0.497)
	tracef.write(f"2456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2456kbit")
	time.sleep(0.557)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(0.54)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.525)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.539)
	tracef.write(f"2250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2250kbit")
	time.sleep(0.519)
	tracef.write(f"2888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2888kbit")
	time.sleep(0.519)
	tracef.write(f"1939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1939kbit")
	time.sleep(0.503)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(0.505)
	tracef.write(f"2706 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2706kbit")
	time.sleep(0.561)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.536)
	tracef.write(f"1966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1966kbit")
	time.sleep(0.515)
	tracef.write(f"1956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1956kbit")
	time.sleep(0.501)
	tracef.write(f"1804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1804kbit")
	time.sleep(0.554)
	tracef.write(f"2953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2953kbit")
	time.sleep(0.521)
	tracef.write(f"2625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2625kbit")
	time.sleep(0.562)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.497)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.531)
	tracef.write(f"1723 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1723kbit")
	time.sleep(0.531)
	tracef.write(f"1901 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1901kbit")
	time.sleep(0.533)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(0.545)
	tracef.write(f"2739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2739kbit")
	time.sleep(0.549)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(0.504)
	tracef.write(f"2261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2261kbit")
	time.sleep(0.51)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.538)
	tracef.write(f"2279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2279kbit")
	time.sleep(0.497)
	tracef.write(f"2428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2428kbit")
	time.sleep(0.548)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(0.562)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.537)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(0.5)
	tracef.write(f"2516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2516kbit")
	time.sleep(0.539)
	tracef.write(f"1949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1949kbit")
	time.sleep(0.509)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.553)
	tracef.write(f"2897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2897kbit")
	time.sleep(0.519)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(0.545)
	tracef.write(f"1280 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1280kbit")
	time.sleep(0.505)
	tracef.write(f"2883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2883kbit")
	time.sleep(0.55)
	tracef.write(f"2456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2456kbit")
	time.sleep(0.499)
	tracef.write(f"2882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2882kbit")
	time.sleep(0.523)
	tracef.write(f"2473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2473kbit")
	time.sleep(0.56)
	tracef.write(f"2325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2325kbit")
	time.sleep(0.51)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(0.495)
	tracef.write(f"1755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1755kbit")
	time.sleep(0.499)
	tracef.write(f"1741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1741kbit")
	time.sleep(0.555)
	tracef.write(f"2245 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2245kbit")
	time.sleep(0.561)
	tracef.write(f"2731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2731kbit")
	time.sleep(0.555)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.557)
	tracef.write(f"1717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1717kbit")
	time.sleep(0.516)
	tracef.write(f"2784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2784kbit")
	time.sleep(0.56)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.529)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.509)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.499)
	tracef.write(f"2633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2633kbit")
	time.sleep(0.538)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.524)
	tracef.write(f"2907 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2907kbit")
	time.sleep(0.548)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.5)
	tracef.write(f"2248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2248kbit")
	time.sleep(0.526)
	tracef.write(f"2002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2002kbit")
	time.sleep(0.556)
	tracef.write(f"2241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2241kbit")
	time.sleep(0.539)
	tracef.write(f"2871 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2871kbit")
	time.sleep(0.519)
	tracef.write(f"1696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1696kbit")
	time.sleep(0.513)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.51)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.517)
	tracef.write(f"1618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1618kbit")
	time.sleep(0.545)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.52)
	tracef.write(f"1301 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1301kbit")
	time.sleep(0.54)
	tracef.write(f"2698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2698kbit")
	time.sleep(0.545)
	tracef.write(f"1656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1656kbit")
	time.sleep(0.512)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(0.542)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.543)
	tracef.write(f"2129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2129kbit")
	time.sleep(0.545)
	tracef.write(f"2643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2643kbit")
	time.sleep(0.55)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.514)
	tracef.write(f"2296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2296kbit")
	time.sleep(0.525)
	tracef.write(f"2234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2234kbit")
	time.sleep(0.542)
	tracef.write(f"2330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2330kbit")
	time.sleep(0.537)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.538)
	tracef.write(f"1649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1649kbit")
	time.sleep(0.527)
	tracef.write(f"2665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2665kbit")
	time.sleep(0.503)
	tracef.write(f"2082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2082kbit")
	time.sleep(0.53)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(0.556)
	tracef.write(f"1686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1686kbit")
	time.sleep(0.526)
	tracef.write(f"2829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2829kbit")
	time.sleep(0.502)
	tracef.write(f"1738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1738kbit")
	time.sleep(0.526)
	tracef.write(f"1997 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1997kbit")
	time.sleep(0.542)
	tracef.write(f"2200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2200kbit")
	time.sleep(0.533)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(0.544)
	tracef.write(f"2805 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2805kbit")
	time.sleep(0.508)
	tracef.write(f"2728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2728kbit")
	time.sleep(0.535)
	tracef.write(f"1798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1798kbit")
	time.sleep(0.562)
	tracef.write(f"1988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1988kbit")
	time.sleep(0.506)
	tracef.write(f"2298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2298kbit")
	time.sleep(0.533)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.495)
	tracef.write(f"2044 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2044kbit")
	time.sleep(0.556)
	tracef.write(f"1657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1657kbit")
	time.sleep(0.509)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.515)
	tracef.write(f"2880 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2880kbit")
	time.sleep(0.503)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.508)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(0.5)
	tracef.write(f"1975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1975kbit")
	time.sleep(0.546)
	tracef.write(f"2289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2289kbit")
	time.sleep(0.555)
	tracef.write(f"1736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1736kbit")
	time.sleep(0.528)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(0.519)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.537)
	tracef.write(f"2953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2953kbit")
	time.sleep(0.514)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()