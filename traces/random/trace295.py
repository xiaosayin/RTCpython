#t:719-723 ; rate:1041-2837 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace295.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace295.txt", 'a+')
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1380kbit")
	time.sleep(0.721)
	tracef.write(f"2328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2328kbit")
	time.sleep(0.723)
	tracef.write(f"1612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1612kbit")
	time.sleep(0.72)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.723)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.723)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.722)
	tracef.write(f"2278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2278kbit")
	time.sleep(0.721)
	tracef.write(f"2510 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2510kbit")
	time.sleep(0.721)
	tracef.write(f"2678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2678kbit")
	time.sleep(0.723)
	tracef.write(f"2283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2283kbit")
	time.sleep(0.72)
	tracef.write(f"2410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2410kbit")
	time.sleep(0.721)
	tracef.write(f"1785 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1785kbit")
	time.sleep(0.722)
	tracef.write(f"2309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2309kbit")
	time.sleep(0.72)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(0.719)
	tracef.write(f"1361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1361kbit")
	time.sleep(0.722)
	tracef.write(f"1099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1099kbit")
	time.sleep(0.722)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(0.722)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(0.72)
	tracef.write(f"2328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2328kbit")
	time.sleep(0.722)
	tracef.write(f"2791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2791kbit")
	time.sleep(0.719)
	tracef.write(f"1678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1678kbit")
	time.sleep(0.721)
	tracef.write(f"1320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1320kbit")
	time.sleep(0.72)
	tracef.write(f"2493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2493kbit")
	time.sleep(0.719)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.721)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.72)
	tracef.write(f"1663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1663kbit")
	time.sleep(0.723)
	tracef.write(f"1980 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1980kbit")
	time.sleep(0.722)
	tracef.write(f"2151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2151kbit")
	time.sleep(0.722)
	tracef.write(f"1768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1768kbit")
	time.sleep(0.721)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(0.719)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.722)
	tracef.write(f"2630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2630kbit")
	time.sleep(0.723)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.723)
	tracef.write(f"2711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2711kbit")
	time.sleep(0.719)
	tracef.write(f"2302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2302kbit")
	time.sleep(0.722)
	tracef.write(f"1877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1877kbit")
	time.sleep(0.72)
	tracef.write(f"1635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1635kbit")
	time.sleep(0.723)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.719)
	tracef.write(f"1935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1935kbit")
	time.sleep(0.722)
	tracef.write(f"1982 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1982kbit")
	time.sleep(0.72)
	tracef.write(f"2294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2294kbit")
	time.sleep(0.719)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.723)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.721)
	tracef.write(f"2798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2798kbit")
	time.sleep(0.72)
	tracef.write(f"2087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2087kbit")
	time.sleep(0.723)
	tracef.write(f"1635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1635kbit")
	time.sleep(0.719)
	tracef.write(f"2802 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2802kbit")
	time.sleep(0.721)
	tracef.write(f"2096 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2096kbit")
	time.sleep(0.721)
	tracef.write(f"2703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2703kbit")
	time.sleep(0.72)
	tracef.write(f"2244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2244kbit")
	time.sleep(0.719)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(0.722)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.72)
	tracef.write(f"2271 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2271kbit")
	time.sleep(0.723)
	tracef.write(f"2398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2398kbit")
	time.sleep(0.723)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(0.722)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.72)
	tracef.write(f"2098 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2098kbit")
	time.sleep(0.72)
	tracef.write(f"2807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2807kbit")
	time.sleep(0.72)
	tracef.write(f"1733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1733kbit")
	time.sleep(0.723)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(0.723)
	tracef.write(f"1318 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1318kbit")
	time.sleep(0.722)
	tracef.write(f"2266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2266kbit")
	time.sleep(0.72)
	tracef.write(f"2004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2004kbit")
	time.sleep(0.72)
	tracef.write(f"2805 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2805kbit")
	time.sleep(0.723)
	tracef.write(f"2425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2425kbit")
	time.sleep(0.723)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.719)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.719)
	tracef.write(f"1185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1185kbit")
	time.sleep(0.722)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(0.721)
	tracef.write(f"1799 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1799kbit")
	time.sleep(0.722)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(0.719)
	tracef.write(f"2808 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2808kbit")
	time.sleep(0.721)
	tracef.write(f"1066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1066kbit")
	time.sleep(0.723)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.723)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(0.719)
	tracef.write(f"2593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2593kbit")
	time.sleep(0.72)
	tracef.write(f"1974 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1974kbit")
	time.sleep(0.722)
	tracef.write(f"2443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2443kbit")
	time.sleep(0.72)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.719)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.721)
	tracef.write(f"1169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1169kbit")
	time.sleep(0.722)
	tracef.write(f"2624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2624kbit")
	time.sleep(0.72)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(0.72)
	tracef.write(f"2022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2022kbit")
	time.sleep(0.721)
	tracef.write(f"2273 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2273kbit")
	time.sleep(0.722)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.721)
	tracef.write(f"2817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2817kbit")
	time.sleep(0.723)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.72)
	tracef.write(f"1422 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1422kbit")
	time.sleep(0.721)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.723)
	tracef.write(f"2289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2289kbit")
	time.sleep(0.719)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.722)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.722)
	tracef.write(f"1698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1698kbit")
	time.sleep(0.721)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.72)
	tracef.write(f"1449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1449kbit")
	time.sleep(0.72)
	tracef.write(f"2027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2027kbit")
	time.sleep(0.722)
	tracef.write(f"2361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2361kbit")
	time.sleep(0.723)
	tracef.write(f"2705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2705kbit")
	time.sleep(0.72)
	tracef.write(f"2521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2521kbit")
	time.sleep(0.721)
	tracef.write(f"2110 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2110kbit")
	time.sleep(0.723)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(0.722)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.72)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(0.721)
	tracef.write(f"2807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2807kbit")
	time.sleep(0.723)
	tracef.write(f"2069 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2069kbit")
	time.sleep(0.72)
	tracef.write(f"1971 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1971kbit")
	time.sleep(0.721)
	tracef.write(f"2591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2591kbit")
	time.sleep(0.722)
	tracef.write(f"2834 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2834kbit")
	time.sleep(0.722)
	tracef.write(f"2812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2812kbit")
	time.sleep(0.721)
	tracef.write(f"2832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2832kbit")
	time.sleep(0.721)
	tracef.write(f"2090 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2090kbit")
	time.sleep(0.723)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.723)
	tracef.write(f"2224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2224kbit")
	time.sleep(0.719)
	tracef.write(f"2058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2058kbit")
	time.sleep(0.721)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(0.72)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(0.722)
	tracef.write(f"1450 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1450kbit")
	time.sleep(0.719)
	tracef.write(f"1921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1921kbit")
	time.sleep(0.72)
	tracef.write(f"2804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2804kbit")
	time.sleep(0.719)
	tracef.write(f"2604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2604kbit")
	time.sleep(0.72)
	tracef.write(f"2572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2572kbit")
	time.sleep(0.72)
	tracef.write(f"2671 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2671kbit")
	time.sleep(0.719)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.721)
	tracef.write(f"1912 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1912kbit")
	time.sleep(0.72)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.72)
	tracef.write(f"2181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2181kbit")
	time.sleep(0.719)
	tracef.write(f"1724 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1724kbit")
	time.sleep(0.722)
	tracef.write(f"1708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1708kbit")
	time.sleep(0.723)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(0.721)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.721)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.721)
	tracef.write(f"2524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2524kbit")
	time.sleep(0.72)
	tracef.write(f"1672 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1672kbit")
	time.sleep(0.722)
	tracef.write(f"2599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2599kbit")
	time.sleep(0.72)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(0.72)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.721)
	tracef.write(f"2663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2663kbit")
	time.sleep(0.72)
	tracef.write(f"2349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2349kbit")
	time.sleep(0.723)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()