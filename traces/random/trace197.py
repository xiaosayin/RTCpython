#t:424-855 ; rate:1394-2867 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace197.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace197.txt", 'a+')
	tracef.write(f"2374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2374kbit")
	time.sleep(0.598)
	tracef.write(f"2840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2840kbit")
	time.sleep(0.505)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.78)
	tracef.write(f"2099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2099kbit")
	time.sleep(0.536)
	tracef.write(f"2134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2134kbit")
	time.sleep(0.802)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.796)
	tracef.write(f"2161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2161kbit")
	time.sleep(0.647)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(0.756)
	tracef.write(f"1686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1686kbit")
	time.sleep(0.68)
	tracef.write(f"2198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2198kbit")
	time.sleep(0.525)
	tracef.write(f"1768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1768kbit")
	time.sleep(0.685)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.482)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.602)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.841)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.468)
	tracef.write(f"2192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2192kbit")
	time.sleep(0.838)
	tracef.write(f"2846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2846kbit")
	time.sleep(0.634)
	tracef.write(f"2539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2539kbit")
	time.sleep(0.629)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.773)
	tracef.write(f"2710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2710kbit")
	time.sleep(0.853)
	tracef.write(f"2171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2171kbit")
	time.sleep(0.61)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.479)
	tracef.write(f"2657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2657kbit")
	time.sleep(0.547)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.736)
	tracef.write(f"2552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2552kbit")
	time.sleep(0.469)
	tracef.write(f"1845 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1845kbit")
	time.sleep(0.823)
	tracef.write(f"1798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1798kbit")
	time.sleep(0.441)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(0.845)
	tracef.write(f"2406 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2406kbit")
	time.sleep(0.637)
	tracef.write(f"1824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1824kbit")
	time.sleep(0.706)
	tracef.write(f"2162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2162kbit")
	time.sleep(0.827)
	tracef.write(f"2470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2470kbit")
	time.sleep(0.665)
	tracef.write(f"1820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1820kbit")
	time.sleep(0.429)
	tracef.write(f"1561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1561kbit")
	time.sleep(0.652)
	tracef.write(f"2217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2217kbit")
	time.sleep(0.527)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.71)
	tracef.write(f"2021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2021kbit")
	time.sleep(0.435)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.791)
	tracef.write(f"1495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1495kbit")
	time.sleep(0.553)
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1676kbit")
	time.sleep(0.657)
	tracef.write(f"2034 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2034kbit")
	time.sleep(0.531)
	tracef.write(f"2623 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2623kbit")
	time.sleep(0.735)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.469)
	tracef.write(f"2316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2316kbit")
	time.sleep(0.483)
	tracef.write(f"2385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2385kbit")
	time.sleep(0.799)
	tracef.write(f"2372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2372kbit")
	time.sleep(0.804)
	tracef.write(f"1922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1922kbit")
	time.sleep(0.728)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(0.701)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.67)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(0.565)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.764)
	tracef.write(f"1721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1721kbit")
	time.sleep(0.821)
	tracef.write(f"2693 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2693kbit")
	time.sleep(0.804)
	tracef.write(f"2484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2484kbit")
	time.sleep(0.848)
	tracef.write(f"2677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2677kbit")
	time.sleep(0.523)
	tracef.write(f"2007 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2007kbit")
	time.sleep(0.648)
	tracef.write(f"2600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2600kbit")
	time.sleep(0.658)
	tracef.write(f"2315 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2315kbit")
	time.sleep(0.73)
	tracef.write(f"2681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2681kbit")
	time.sleep(0.748)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(0.429)
	tracef.write(f"1896 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1896kbit")
	time.sleep(0.69)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.458)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.688)
	tracef.write(f"2655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2655kbit")
	time.sleep(0.686)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.783)
	tracef.write(f"2243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2243kbit")
	time.sleep(0.775)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.603)
	tracef.write(f"2179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2179kbit")
	time.sleep(0.554)
	tracef.write(f"2272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2272kbit")
	time.sleep(0.568)
	tracef.write(f"2662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2662kbit")
	time.sleep(0.677)
	tracef.write(f"1994 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1994kbit")
	time.sleep(0.456)
	tracef.write(f"1882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1882kbit")
	time.sleep(0.438)
	tracef.write(f"2148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2148kbit")
	time.sleep(0.51)
	tracef.write(f"2427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2427kbit")
	time.sleep(0.542)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.467)
	tracef.write(f"2637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2637kbit")
	time.sleep(0.816)
	tracef.write(f"2510 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2510kbit")
	time.sleep(0.449)
	tracef.write(f"1920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1920kbit")
	time.sleep(0.606)
	tracef.write(f"2092 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2092kbit")
	time.sleep(0.785)
	tracef.write(f"1859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1859kbit")
	time.sleep(0.428)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.521)
	tracef.write(f"1728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1728kbit")
	time.sleep(0.49)
	tracef.write(f"2200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2200kbit")
	time.sleep(0.847)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.665)
	tracef.write(f"2621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2621kbit")
	time.sleep(0.441)
	tracef.write(f"2579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2579kbit")
	time.sleep(0.666)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.518)
	tracef.write(f"2429 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2429kbit")
	time.sleep(0.657)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(0.518)
	tracef.write(f"2189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2189kbit")
	time.sleep(0.571)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.804)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.658)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.53)
	tracef.write(f"1926 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1926kbit")
	time.sleep(0.506)
	tracef.write(f"2437 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2437kbit")
	time.sleep(0.751)
	tracef.write(f"2698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2698kbit")
	time.sleep(0.694)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.651)
	tracef.write(f"2403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2403kbit")
	time.sleep(0.531)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(0.664)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(0.545)
	tracef.write(f"2088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2088kbit")
	time.sleep(0.837)
	tracef.write(f"2573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2573kbit")
	time.sleep(0.734)
	tracef.write(f"2349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2349kbit")
	time.sleep(0.568)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(0.503)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.68)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.809)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.771)
	tracef.write(f"2178 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2178kbit")
	time.sleep(0.663)
	tracef.write(f"1949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1949kbit")
	time.sleep(0.609)
	tracef.write(f"2030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2030kbit")
	time.sleep(0.67)
	tracef.write(f"2596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2596kbit")
	time.sleep(0.797)
	tracef.write(f"2077 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2077kbit")
	time.sleep(0.816)
	tracef.write(f"2730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2730kbit")
	time.sleep(0.62)
	tracef.write(f"2834 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2834kbit")
	time.sleep(0.49)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(0.646)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(0.634)
	tracef.write(f"1976 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1976kbit")
	time.sleep(0.629)
	tracef.write(f"2807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2807kbit")
	time.sleep(0.848)
	tracef.write(f"2024 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2024kbit")
	time.sleep(0.72)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.745)
	tracef.write(f"2668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2668kbit")
	time.sleep(0.625)
	tracef.write(f"2110 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2110kbit")
	time.sleep(0.644)
	tracef.write(f"2273 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2273kbit")
	time.sleep(0.757)
	tracef.write(f"1781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1781kbit")
	time.sleep(0.546)
	tracef.write(f"2177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2177kbit")
	time.sleep(0.562)
	tracef.write(f"2340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2340kbit")
	time.sleep(0.752)
	tracef.write(f"2640 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2640kbit")
	time.sleep(0.695)
	tracef.write(f"2806 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2806kbit")
	time.sleep(0.597)
	tracef.write(f"2400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2400kbit")
	time.sleep(0.579)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(0.848)
	tracef.write(f"1868 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1868kbit")
	time.sleep(0.852)
	tracef.write(f"1762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1762kbit")
	time.sleep(0.595)
	tracef.write(f"2214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2214kbit")
	time.sleep(0.503)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(0.831)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.715)
	tracef.write(f"2130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2130kbit")
	time.sleep(0.453)
	tracef.write(f"2831 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2831kbit")
	time.sleep(0.524)
	tracef.write(f"2238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2238kbit")
	time.sleep(0.61)
	tracef.write(f"2138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2138kbit")
	time.sleep(0.488)
	tracef.write(f"2405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2405kbit")
	time.sleep(0.7)
	tracef.write(f"2011 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2011kbit")
	time.sleep(0.568)
	tracef.write(f"1996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1996kbit")
	time.sleep(0.738)
	tracef.write(f"1936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1936kbit")
	time.sleep(0.734)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.447)
	tracef.write(f"2331 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2331kbit")
	time.sleep(0.81)
	tracef.write(f"1804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1804kbit")
	time.sleep(0.459)
	tracef.write(f"2071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2071kbit")
	time.sleep(0.787)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.628)
	tracef.write(f"2423 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2423kbit")
	time.sleep(0.592)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.828)
	tracef.write(f"2613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2613kbit")
	time.sleep(0.762)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.835)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.534)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.543)
	tracef.write(f"1462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1462kbit")
	time.sleep(0.568)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()