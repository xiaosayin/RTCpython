#t:600-732 ; rate:1761-2818 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace352.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace352.txt", 'a+')
	tracef.write(f"2541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2541kbit")
	time.sleep(0.667)
	tracef.write(f"2522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2522kbit")
	time.sleep(0.648)
	tracef.write(f"2598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2598kbit")
	time.sleep(0.683)
	tracef.write(f"2392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2392kbit")
	time.sleep(0.692)
	tracef.write(f"2485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2485kbit")
	time.sleep(0.603)
	tracef.write(f"2062 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2062kbit")
	time.sleep(0.704)
	tracef.write(f"2113 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2113kbit")
	time.sleep(0.638)
	tracef.write(f"2251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2251kbit")
	time.sleep(0.69)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.607)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.615)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.673)
	tracef.write(f"1833 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1833kbit")
	time.sleep(0.647)
	tracef.write(f"2817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2817kbit")
	time.sleep(0.702)
	tracef.write(f"2607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2607kbit")
	time.sleep(0.608)
	tracef.write(f"1765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1765kbit")
	time.sleep(0.63)
	tracef.write(f"2588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2588kbit")
	time.sleep(0.656)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.702)
	tracef.write(f"2389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2389kbit")
	time.sleep(0.686)
	tracef.write(f"1907 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1907kbit")
	time.sleep(0.636)
	tracef.write(f"2338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2338kbit")
	time.sleep(0.681)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.662)
	tracef.write(f"2627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2627kbit")
	time.sleep(0.728)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.671)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.715)
	tracef.write(f"2180 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2180kbit")
	time.sleep(0.619)
	tracef.write(f"1876 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1876kbit")
	time.sleep(0.701)
	tracef.write(f"2074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2074kbit")
	time.sleep(0.634)
	tracef.write(f"2089 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2089kbit")
	time.sleep(0.635)
	tracef.write(f"2616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2616kbit")
	time.sleep(0.616)
	tracef.write(f"2587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2587kbit")
	time.sleep(0.673)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.713)
	tracef.write(f"1822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1822kbit")
	time.sleep(0.706)
	tracef.write(f"1851 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1851kbit")
	time.sleep(0.648)
	tracef.write(f"2688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2688kbit")
	time.sleep(0.712)
	tracef.write(f"2170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2170kbit")
	time.sleep(0.729)
	tracef.write(f"2042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2042kbit")
	time.sleep(0.611)
	tracef.write(f"2410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2410kbit")
	time.sleep(0.631)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.72)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.673)
	tracef.write(f"2616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2616kbit")
	time.sleep(0.643)
	tracef.write(f"1813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1813kbit")
	time.sleep(0.639)
	tracef.write(f"2202 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2202kbit")
	time.sleep(0.689)
	tracef.write(f"2705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2705kbit")
	time.sleep(0.679)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.726)
	tracef.write(f"2056 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2056kbit")
	time.sleep(0.617)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.637)
	tracef.write(f"2427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2427kbit")
	time.sleep(0.697)
	tracef.write(f"1918 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1918kbit")
	time.sleep(0.643)
	tracef.write(f"2276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2276kbit")
	time.sleep(0.721)
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2381kbit")
	time.sleep(0.698)
	tracef.write(f"2738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2738kbit")
	time.sleep(0.694)
	tracef.write(f"1863 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1863kbit")
	time.sleep(0.719)
	tracef.write(f"2799 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2799kbit")
	time.sleep(0.684)
	tracef.write(f"2498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2498kbit")
	time.sleep(0.645)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.615)
	tracef.write(f"2083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2083kbit")
	time.sleep(0.609)
	tracef.write(f"2086 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2086kbit")
	time.sleep(0.718)
	tracef.write(f"2136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2136kbit")
	time.sleep(0.691)
	tracef.write(f"2566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2566kbit")
	time.sleep(0.702)
	tracef.write(f"2064 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2064kbit")
	time.sleep(0.711)
	tracef.write(f"2437 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2437kbit")
	time.sleep(0.655)
	tracef.write(f"1837 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1837kbit")
	time.sleep(0.606)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.601)
	tracef.write(f"2792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2792kbit")
	time.sleep(0.706)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.6)
	tracef.write(f"2257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2257kbit")
	time.sleep(0.694)
	tracef.write(f"1962 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1962kbit")
	time.sleep(0.65)
	tracef.write(f"2184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2184kbit")
	time.sleep(0.658)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.665)
	tracef.write(f"2662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2662kbit")
	time.sleep(0.712)
	tracef.write(f"2651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2651kbit")
	time.sleep(0.687)
	tracef.write(f"1896 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1896kbit")
	time.sleep(0.732)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.679)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.711)
	tracef.write(f"2777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2777kbit")
	time.sleep(0.634)
	tracef.write(f"2527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2527kbit")
	time.sleep(0.623)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.656)
	tracef.write(f"2710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2710kbit")
	time.sleep(0.719)
	tracef.write(f"2341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2341kbit")
	time.sleep(0.662)
	tracef.write(f"1889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1889kbit")
	time.sleep(0.62)
	tracef.write(f"2604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2604kbit")
	time.sleep(0.636)
	tracef.write(f"2194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2194kbit")
	time.sleep(0.638)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.7)
	tracef.write(f"2230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2230kbit")
	time.sleep(0.66)
	tracef.write(f"2576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2576kbit")
	time.sleep(0.658)
	tracef.write(f"2551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2551kbit")
	time.sleep(0.628)
	tracef.write(f"1814 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1814kbit")
	time.sleep(0.604)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.696)
	tracef.write(f"2451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2451kbit")
	time.sleep(0.672)
	tracef.write(f"2644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2644kbit")
	time.sleep(0.665)
	tracef.write(f"2154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2154kbit")
	time.sleep(0.71)
	tracef.write(f"2669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2669kbit")
	time.sleep(0.671)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.638)
	tracef.write(f"2276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2276kbit")
	time.sleep(0.652)
	tracef.write(f"1873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1873kbit")
	time.sleep(0.633)
	tracef.write(f"2619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2619kbit")
	time.sleep(0.641)
	tracef.write(f"2804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2804kbit")
	time.sleep(0.637)
	tracef.write(f"1835 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1835kbit")
	time.sleep(0.601)
	tracef.write(f"1817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1817kbit")
	time.sleep(0.671)
	tracef.write(f"2096 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2096kbit")
	time.sleep(0.724)
	tracef.write(f"2166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2166kbit")
	time.sleep(0.726)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.704)
	tracef.write(f"2499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2499kbit")
	time.sleep(0.635)
	tracef.write(f"2034 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2034kbit")
	time.sleep(0.629)
	tracef.write(f"2087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2087kbit")
	time.sleep(0.672)
	tracef.write(f"2299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2299kbit")
	time.sleep(0.666)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.615)
	tracef.write(f"2156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2156kbit")
	time.sleep(0.683)
	tracef.write(f"2490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2490kbit")
	time.sleep(0.657)
	tracef.write(f"1766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1766kbit")
	time.sleep(0.652)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.628)
	tracef.write(f"2612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2612kbit")
	time.sleep(0.696)
	tracef.write(f"2741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2741kbit")
	time.sleep(0.697)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.641)
	tracef.write(f"2609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2609kbit")
	time.sleep(0.662)
	tracef.write(f"1863 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1863kbit")
	time.sleep(0.716)
	tracef.write(f"1945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1945kbit")
	time.sleep(0.656)
	tracef.write(f"1828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1828kbit")
	time.sleep(0.683)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.647)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.704)
	tracef.write(f"2152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2152kbit")
	time.sleep(0.642)
	tracef.write(f"2476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2476kbit")
	time.sleep(0.732)
	tracef.write(f"2481 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2481kbit")
	time.sleep(0.617)
	tracef.write(f"2635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2635kbit")
	time.sleep(0.626)
	tracef.write(f"2568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2568kbit")
	time.sleep(0.697)
	tracef.write(f"2478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2478kbit")
	time.sleep(0.682)
	tracef.write(f"2376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2376kbit")
	time.sleep(0.686)
	tracef.write(f"2278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2278kbit")
	time.sleep(0.609)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.642)
	tracef.write(f"2439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2439kbit")
	time.sleep(0.653)
	tracef.write(f"2319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2319kbit")
	time.sleep(0.614)
	tracef.write(f"2565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2565kbit")
	time.sleep(0.632)
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2381kbit")
	time.sleep(0.641)
	tracef.write(f"2020 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2020kbit")
	time.sleep(0.601)
	tracef.write(f"1909 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1909kbit")
	time.sleep(0.626)
	tracef.write(f"1810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1810kbit")
	time.sleep(0.647)
	tracef.write(f"1842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1842kbit")
	time.sleep(0.642)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.723)
	tracef.write(f"2443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2443kbit")
	time.sleep(0.67)
	tracef.write(f"1801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1801kbit")
	time.sleep(0.693)
	tracef.write(f"2136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2136kbit")
	time.sleep(0.715)
	tracef.write(f"1921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1921kbit")
	time.sleep(0.644)
	tracef.write(f"2413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2413kbit")
	time.sleep(0.651)
	tracef.write(f"2170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2170kbit")
	time.sleep(0.639)
	tracef.write(f"2000 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2000kbit")
	time.sleep(0.606)
	tracef.write(f"2612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2612kbit")
	time.sleep(0.684)
	tracef.write(f"2536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2536kbit")
	time.sleep(0.674)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.61)
	tracef.write(f"1834 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1834kbit")
	time.sleep(0.678)
	tracef.write(f"2693 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2693kbit")
	time.sleep(0.6)
	tracef.write(f"2268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2268kbit")
	time.sleep(0.601)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()