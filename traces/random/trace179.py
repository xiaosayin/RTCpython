#t:777-788 ; rate:1479-2722 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace179.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace179.txt", 'a+')
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2059kbit")
	time.sleep(0.777)
	tracef.write(f"2391 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2391kbit")
	time.sleep(0.784)
	tracef.write(f"2709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2709kbit")
	time.sleep(0.786)
	tracef.write(f"2581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2581kbit")
	time.sleep(0.781)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.788)
	tracef.write(f"2511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2511kbit")
	time.sleep(0.783)
	tracef.write(f"1859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1859kbit")
	time.sleep(0.784)
	tracef.write(f"2442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2442kbit")
	time.sleep(0.786)
	tracef.write(f"2219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2219kbit")
	time.sleep(0.783)
	tracef.write(f"1519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1519kbit")
	time.sleep(0.782)
	tracef.write(f"1818 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1818kbit")
	time.sleep(0.781)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.788)
	tracef.write(f"1686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1686kbit")
	time.sleep(0.779)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.788)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.78)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.781)
	tracef.write(f"2464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2464kbit")
	time.sleep(0.784)
	tracef.write(f"2432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2432kbit")
	time.sleep(0.779)
	tracef.write(f"2588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2588kbit")
	time.sleep(0.778)
	tracef.write(f"2595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2595kbit")
	time.sleep(0.788)
	tracef.write(f"2680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2680kbit")
	time.sleep(0.783)
	tracef.write(f"2577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2577kbit")
	time.sleep(0.788)
	tracef.write(f"1801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1801kbit")
	time.sleep(0.783)
	tracef.write(f"2227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2227kbit")
	time.sleep(0.788)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.787)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.787)
	tracef.write(f"1578 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1578kbit")
	time.sleep(0.784)
	tracef.write(f"2030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2030kbit")
	time.sleep(0.778)
	tracef.write(f"2561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2561kbit")
	time.sleep(0.786)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.785)
	tracef.write(f"2536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2536kbit")
	time.sleep(0.783)
	tracef.write(f"2198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2198kbit")
	time.sleep(0.78)
	tracef.write(f"1817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1817kbit")
	time.sleep(0.783)
	tracef.write(f"1974 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1974kbit")
	time.sleep(0.785)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.786)
	tracef.write(f"2487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2487kbit")
	time.sleep(0.788)
	tracef.write(f"1765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1765kbit")
	time.sleep(0.786)
	tracef.write(f"1986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1986kbit")
	time.sleep(0.786)
	tracef.write(f"1579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1579kbit")
	time.sleep(0.782)
	tracef.write(f"2372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2372kbit")
	time.sleep(0.786)
	tracef.write(f"2244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2244kbit")
	time.sleep(0.781)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.781)
	tracef.write(f"2115 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2115kbit")
	time.sleep(0.785)
	tracef.write(f"2179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2179kbit")
	time.sleep(0.777)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.778)
	tracef.write(f"2639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2639kbit")
	time.sleep(0.777)
	tracef.write(f"2319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2319kbit")
	time.sleep(0.784)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.786)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.778)
	tracef.write(f"2223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2223kbit")
	time.sleep(0.786)
	tracef.write(f"2177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2177kbit")
	time.sleep(0.782)
	tracef.write(f"1654 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1654kbit")
	time.sleep(0.782)
	tracef.write(f"2557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2557kbit")
	time.sleep(0.781)
	tracef.write(f"1687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1687kbit")
	time.sleep(0.779)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.778)
	tracef.write(f"2417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2417kbit")
	time.sleep(0.779)
	tracef.write(f"2310 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2310kbit")
	time.sleep(0.786)
	tracef.write(f"2583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2583kbit")
	time.sleep(0.784)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.777)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.781)
	tracef.write(f"1770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1770kbit")
	time.sleep(0.78)
	tracef.write(f"1557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1557kbit")
	time.sleep(0.785)
	tracef.write(f"2305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2305kbit")
	time.sleep(0.781)
	tracef.write(f"2220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2220kbit")
	time.sleep(0.785)
	tracef.write(f"2629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2629kbit")
	time.sleep(0.777)
	tracef.write(f"2310 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2310kbit")
	time.sleep(0.788)
	tracef.write(f"1859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1859kbit")
	time.sleep(0.781)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.784)
	tracef.write(f"2638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2638kbit")
	time.sleep(0.788)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.783)
	tracef.write(f"1793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1793kbit")
	time.sleep(0.778)
	tracef.write(f"2432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2432kbit")
	time.sleep(0.782)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.783)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.779)
	tracef.write(f"2547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2547kbit")
	time.sleep(0.778)
	tracef.write(f"1826 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1826kbit")
	time.sleep(0.784)
	tracef.write(f"2358 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2358kbit")
	time.sleep(0.788)
	tracef.write(f"2426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2426kbit")
	time.sleep(0.779)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.787)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.778)
	tracef.write(f"1763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1763kbit")
	time.sleep(0.779)
	tracef.write(f"2426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2426kbit")
	time.sleep(0.785)
	tracef.write(f"1844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1844kbit")
	time.sleep(0.783)
	tracef.write(f"1667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1667kbit")
	time.sleep(0.783)
	tracef.write(f"2031 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2031kbit")
	time.sleep(0.784)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.787)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.778)
	tracef.write(f"1609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1609kbit")
	time.sleep(0.786)
	tracef.write(f"1574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1574kbit")
	time.sleep(0.778)
	tracef.write(f"1653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1653kbit")
	time.sleep(0.782)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.783)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.788)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.78)
	tracef.write(f"2418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2418kbit")
	time.sleep(0.781)
	tracef.write(f"2308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2308kbit")
	time.sleep(0.784)
	tracef.write(f"2349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2349kbit")
	time.sleep(0.778)
	tracef.write(f"1900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1900kbit")
	time.sleep(0.779)
	tracef.write(f"1848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1848kbit")
	time.sleep(0.786)
	tracef.write(f"2106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2106kbit")
	time.sleep(0.786)
	tracef.write(f"1950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1950kbit")
	time.sleep(0.78)
	tracef.write(f"1672 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1672kbit")
	time.sleep(0.781)
	tracef.write(f"1568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1568kbit")
	time.sleep(0.777)
	tracef.write(f"1816 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1816kbit")
	time.sleep(0.782)
	tracef.write(f"1579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1579kbit")
	time.sleep(0.781)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.78)
	tracef.write(f"2270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2270kbit")
	time.sleep(0.78)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.786)
	tracef.write(f"2346 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2346kbit")
	time.sleep(0.781)
	tracef.write(f"2304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2304kbit")
	time.sleep(0.785)
	tracef.write(f"2400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2400kbit")
	time.sleep(0.779)
	tracef.write(f"2448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2448kbit")
	time.sleep(0.777)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.783)
	tracef.write(f"2716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2716kbit")
	time.sleep(0.785)
	tracef.write(f"2575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2575kbit")
	time.sleep(0.788)
	tracef.write(f"2511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2511kbit")
	time.sleep(0.779)
	tracef.write(f"2486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2486kbit")
	time.sleep(0.778)
	tracef.write(f"1691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1691kbit")
	time.sleep(0.781)
	tracef.write(f"2332 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2332kbit")
	time.sleep(0.778)
	tracef.write(f"2198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2198kbit")
	time.sleep(0.788)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.784)
	tracef.write(f"2211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2211kbit")
	time.sleep(0.78)
	tracef.write(f"1875 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1875kbit")
	time.sleep(0.784)
	tracef.write(f"2108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2108kbit")
	time.sleep(0.787)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.781)
	tracef.write(f"1965 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1965kbit")
	time.sleep(0.784)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.782)
	tracef.write(f"2272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2272kbit")
	time.sleep(0.783)
	tracef.write(f"2207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2207kbit")
	time.sleep(0.782)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()