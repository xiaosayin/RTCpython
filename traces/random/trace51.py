#t:420-585 ; rate:1529-2573 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace51.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace51.txt", 'a+')
	tracef.write(f"1800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1800kbit")
	time.sleep(0.521)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.543)
	tracef.write(f"2524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2524kbit")
	time.sleep(0.524)
	tracef.write(f"1572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1572kbit")
	time.sleep(0.493)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.522)
	tracef.write(f"1796 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1796kbit")
	time.sleep(0.483)
	tracef.write(f"2545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2545kbit")
	time.sleep(0.531)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.454)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.44)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.55)
	tracef.write(f"2217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2217kbit")
	time.sleep(0.543)
	tracef.write(f"2016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2016kbit")
	time.sleep(0.468)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.547)
	tracef.write(f"2447 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2447kbit")
	time.sleep(0.471)
	tracef.write(f"2558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2558kbit")
	time.sleep(0.543)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.506)
	tracef.write(f"2442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2442kbit")
	time.sleep(0.455)
	tracef.write(f"2448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2448kbit")
	time.sleep(0.532)
	tracef.write(f"2332 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2332kbit")
	time.sleep(0.428)
	tracef.write(f"1753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1753kbit")
	time.sleep(0.567)
	tracef.write(f"1891 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1891kbit")
	time.sleep(0.509)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.537)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.535)
	tracef.write(f"2209 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2209kbit")
	time.sleep(0.459)
	tracef.write(f"2154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2154kbit")
	time.sleep(0.438)
	tracef.write(f"2286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2286kbit")
	time.sleep(0.565)
	tracef.write(f"2533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2533kbit")
	time.sleep(0.44)
	tracef.write(f"2163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2163kbit")
	time.sleep(0.509)
	tracef.write(f"1816 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1816kbit")
	time.sleep(0.47)
	tracef.write(f"2155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2155kbit")
	time.sleep(0.529)
	tracef.write(f"2562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2562kbit")
	time.sleep(0.421)
	tracef.write(f"1955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1955kbit")
	time.sleep(0.507)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.54)
	tracef.write(f"1953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1953kbit")
	time.sleep(0.449)
	tracef.write(f"2251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2251kbit")
	time.sleep(0.584)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.485)
	tracef.write(f"2421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2421kbit")
	time.sleep(0.466)
	tracef.write(f"2312 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2312kbit")
	time.sleep(0.433)
	tracef.write(f"2568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2568kbit")
	time.sleep(0.489)
	tracef.write(f"2043 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2043kbit")
	time.sleep(0.477)
	tracef.write(f"1981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1981kbit")
	time.sleep(0.524)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.47)
	tracef.write(f"2363 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2363kbit")
	time.sleep(0.51)
	tracef.write(f"2212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2212kbit")
	time.sleep(0.51)
	tracef.write(f"2085 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2085kbit")
	time.sleep(0.505)
	tracef.write(f"2546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2546kbit")
	time.sleep(0.486)
	tracef.write(f"1810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1810kbit")
	time.sleep(0.567)
	tracef.write(f"1663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1663kbit")
	time.sleep(0.521)
	tracef.write(f"2359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2359kbit")
	time.sleep(0.48)
	tracef.write(f"1814 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1814kbit")
	time.sleep(0.433)
	tracef.write(f"2572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2572kbit")
	time.sleep(0.556)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.438)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.512)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.435)
	tracef.write(f"2167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2167kbit")
	time.sleep(0.42)
	tracef.write(f"1536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1536kbit")
	time.sleep(0.522)
	tracef.write(f"1946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1946kbit")
	time.sleep(0.516)
	tracef.write(f"2289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2289kbit")
	time.sleep(0.42)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.465)
	tracef.write(f"2232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2232kbit")
	time.sleep(0.486)
	tracef.write(f"1933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1933kbit")
	time.sleep(0.516)
	tracef.write(f"2060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2060kbit")
	time.sleep(0.428)
	tracef.write(f"1737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1737kbit")
	time.sleep(0.525)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.485)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.458)
	tracef.write(f"1867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1867kbit")
	time.sleep(0.459)
	tracef.write(f"2082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2082kbit")
	time.sleep(0.434)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.511)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.511)
	tracef.write(f"1941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1941kbit")
	time.sleep(0.489)
	tracef.write(f"1689 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1689kbit")
	time.sleep(0.573)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.422)
	tracef.write(f"2224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2224kbit")
	time.sleep(0.436)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.569)
	tracef.write(f"2130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2130kbit")
	time.sleep(0.497)
	tracef.write(f"1602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1602kbit")
	time.sleep(0.571)
	tracef.write(f"2383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2383kbit")
	time.sleep(0.525)
	tracef.write(f"1949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1949kbit")
	time.sleep(0.51)
	tracef.write(f"2071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2071kbit")
	time.sleep(0.549)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.486)
	tracef.write(f"2133 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2133kbit")
	time.sleep(0.488)
	tracef.write(f"2075 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2075kbit")
	time.sleep(0.525)
	tracef.write(f"1734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1734kbit")
	time.sleep(0.544)
	tracef.write(f"2095 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2095kbit")
	time.sleep(0.495)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.454)
	tracef.write(f"2211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2211kbit")
	time.sleep(0.538)
	tracef.write(f"2134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2134kbit")
	time.sleep(0.472)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.471)
	tracef.write(f"1859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1859kbit")
	time.sleep(0.524)
	tracef.write(f"1866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1866kbit")
	time.sleep(0.545)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.485)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.465)
	tracef.write(f"2033 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2033kbit")
	time.sleep(0.584)
	tracef.write(f"2134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2134kbit")
	time.sleep(0.475)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.524)
	tracef.write(f"1986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1986kbit")
	time.sleep(0.573)
	tracef.write(f"2569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2569kbit")
	time.sleep(0.449)
	tracef.write(f"1685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1685kbit")
	time.sleep(0.444)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.567)
	tracef.write(f"1678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1678kbit")
	time.sleep(0.533)
	tracef.write(f"2265 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2265kbit")
	time.sleep(0.528)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.575)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.575)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.473)
	tracef.write(f"2009 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2009kbit")
	time.sleep(0.554)
	tracef.write(f"2297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2297kbit")
	time.sleep(0.58)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.458)
	tracef.write(f"1732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1732kbit")
	time.sleep(0.53)
	tracef.write(f"1780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1780kbit")
	time.sleep(0.437)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.469)
	tracef.write(f"2259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2259kbit")
	time.sleep(0.562)
	tracef.write(f"2266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2266kbit")
	time.sleep(0.575)
	tracef.write(f"1776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1776kbit")
	time.sleep(0.56)
	tracef.write(f"2568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2568kbit")
	time.sleep(0.478)
	tracef.write(f"1799 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1799kbit")
	time.sleep(0.568)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.535)
	tracef.write(f"2225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2225kbit")
	time.sleep(0.561)
	tracef.write(f"2276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2276kbit")
	time.sleep(0.448)
	tracef.write(f"2015 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2015kbit")
	time.sleep(0.493)
	tracef.write(f"2111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2111kbit")
	time.sleep(0.481)
	tracef.write(f"2096 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2096kbit")
	time.sleep(0.483)
	tracef.write(f"1830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1830kbit")
	time.sleep(0.464)
	tracef.write(f"1962 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1962kbit")
	time.sleep(0.556)
	tracef.write(f"2390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2390kbit")
	time.sleep(0.452)
	tracef.write(f"1875 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1875kbit")
	time.sleep(0.529)
	tracef.write(f"2497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2497kbit")
	time.sleep(0.469)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.519)
	tracef.write(f"1750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1750kbit")
	time.sleep(0.515)
	tracef.write(f"2546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2546kbit")
	time.sleep(0.518)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.42)
	tracef.write(f"1848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1848kbit")
	time.sleep(0.545)
	tracef.write(f"2523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2523kbit")
	time.sleep(0.475)
	tracef.write(f"2317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2317kbit")
	time.sleep(0.437)
	tracef.write(f"2162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2162kbit")
	time.sleep(0.555)
	tracef.write(f"2177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2177kbit")
	time.sleep(0.482)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.448)
	tracef.write(f"2219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2219kbit")
	time.sleep(0.436)
	tracef.write(f"1791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1791kbit")
	time.sleep(0.562)
	tracef.write(f"2443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2443kbit")
	time.sleep(0.421)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.441)
	tracef.write(f"2439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2439kbit")
	time.sleep(0.522)
	tracef.write(f"1697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1697kbit")
	time.sleep(0.46)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(0.54)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.485)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.457)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.469)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.468)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.524)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.562)
	tracef.write(f"2395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2395kbit")
	time.sleep(0.552)
	tracef.write(f"1960 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1960kbit")
	time.sleep(0.573)
	tracef.write(f"1574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1574kbit")
	time.sleep(0.481)
	tracef.write(f"2124 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2124kbit")
	time.sleep(0.488)
	tracef.write(f"2111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2111kbit")
	time.sleep(0.453)
	tracef.write(f"2122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2122kbit")
	time.sleep(0.512)
	tracef.write(f"1837 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1837kbit")
	time.sleep(0.509)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.442)
	tracef.write(f"1721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1721kbit")
	time.sleep(0.542)
	tracef.write(f"2530 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2530kbit")
	time.sleep(0.468)
	tracef.write(f"2224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2224kbit")
	time.sleep(0.469)
	tracef.write(f"2125 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2125kbit")
	time.sleep(0.536)
	tracef.write(f"2178 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2178kbit")
	time.sleep(0.521)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.469)
	tracef.write(f"1855 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1855kbit")
	time.sleep(0.554)
	tracef.write(f"1940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1940kbit")
	time.sleep(0.454)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.517)
	tracef.write(f"2070 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2070kbit")
	time.sleep(0.461)
	tracef.write(f"1678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1678kbit")
	time.sleep(0.463)
	tracef.write(f"1924 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1924kbit")
	time.sleep(0.525)
	tracef.write(f"1836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1836kbit")
	time.sleep(0.575)
	tracef.write(f"1843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1843kbit")
	time.sleep(0.431)
	tracef.write(f"2467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2467kbit")
	time.sleep(0.509)
	tracef.write(f"1746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1746kbit")
	time.sleep(0.459)
	tracef.write(f"1533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1533kbit")
	time.sleep(0.478)
	tracef.write(f"1852 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1852kbit")
	time.sleep(0.435)
	tracef.write(f"2440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2440kbit")
	time.sleep(0.524)
	tracef.write(f"1690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1690kbit")
	time.sleep(0.432)
	tracef.write(f"2356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2356kbit")
	time.sleep(0.462)
	tracef.write(f"1897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1897kbit")
	time.sleep(0.48)
	tracef.write(f"2080 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2080kbit")
	time.sleep(0.512)
	tracef.write(f"1777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1777kbit")
	time.sleep(0.46)
	tracef.write(f"2168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2168kbit")
	time.sleep(0.452)
	tracef.write(f"1611 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1611kbit")
	time.sleep(0.476)
	tracef.write(f"2472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2472kbit")
	time.sleep(0.492)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.492)
	tracef.write(f"1567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1567kbit")
	time.sleep(0.58)
	tracef.write(f"2172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2172kbit")
	time.sleep(0.556)
	tracef.write(f"2108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2108kbit")
	time.sleep(0.423)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.55)
	tracef.write(f"1994 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1994kbit")
	time.sleep(0.517)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.451)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(0.456)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.572)
	tracef.write(f"2445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2445kbit")
	time.sleep(0.523)
	tracef.write(f"2353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2353kbit")
	time.sleep(0.484)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.513)
	tracef.write(f"2569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2569kbit")
	time.sleep(0.556)
	tracef.write(f"2256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2256kbit")
	time.sleep(0.456)
	tracef.write(f"2314 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2314kbit")
	time.sleep(0.512)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.584)
	tracef.write(f"1996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1996kbit")
	time.sleep(0.579)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()