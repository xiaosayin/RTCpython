#t:202-982 ; rate:305-2607 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace99.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace99.txt", 'a+')
	tracef.write(f"2477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2477kbit")
	time.sleep(0.844)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(0.509)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(0.694)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.327)
	tracef.write(f"488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 488kbit")
	time.sleep(0.62)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(0.843)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(0.215)
	tracef.write(f"414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 414kbit")
	time.sleep(0.532)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(0.253)
	tracef.write(f"564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 564kbit")
	time.sleep(0.532)
	tracef.write(f"646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 646kbit")
	time.sleep(0.666)
	tracef.write(f"1523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1523kbit")
	time.sleep(0.967)
	tracef.write(f"1350 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1350kbit")
	time.sleep(0.636)
	tracef.write(f"601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 601kbit")
	time.sleep(0.37)
	tracef.write(f"1705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1705kbit")
	time.sleep(0.406)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(0.882)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(0.915)
	tracef.write(f"1794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1794kbit")
	time.sleep(0.937)
	tracef.write(f"1020 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1020kbit")
	time.sleep(0.236)
	tracef.write(f"642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 642kbit")
	time.sleep(0.522)
	tracef.write(f"664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 664kbit")
	time.sleep(0.909)
	tracef.write(f"2302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2302kbit")
	time.sleep(0.676)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.95)
	tracef.write(f"2554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2554kbit")
	time.sleep(0.51)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(0.661)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.654)
	tracef.write(f"2144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2144kbit")
	time.sleep(0.494)
	tracef.write(f"1810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1810kbit")
	time.sleep(0.675)
	tracef.write(f"2371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2371kbit")
	time.sleep(0.576)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(0.689)
	tracef.write(f"2340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2340kbit")
	time.sleep(0.738)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.364)
	tracef.write(f"1687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1687kbit")
	time.sleep(0.334)
	tracef.write(f"853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 853kbit")
	time.sleep(0.364)
	tracef.write(f"1865 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1865kbit")
	time.sleep(0.397)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(0.606)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.969)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(0.664)
	tracef.write(f"2022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2022kbit")
	time.sleep(0.892)
	tracef.write(f"2170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2170kbit")
	time.sleep(0.528)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.427)
	tracef.write(f"2185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2185kbit")
	time.sleep(0.486)
	tracef.write(f"1681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1681kbit")
	time.sleep(0.9)
	tracef.write(f"395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 395kbit")
	time.sleep(0.663)
	tracef.write(f"1742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1742kbit")
	time.sleep(0.403)
	tracef.write(f"737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 737kbit")
	time.sleep(0.212)
	tracef.write(f"834 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 834kbit")
	time.sleep(0.619)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.62)
	tracef.write(f"2214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2214kbit")
	time.sleep(0.233)
	tracef.write(f"1674 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1674kbit")
	time.sleep(0.646)
	tracef.write(f"2579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2579kbit")
	time.sleep(0.685)
	tracef.write(f"2260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2260kbit")
	time.sleep(0.463)
	tracef.write(f"480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 480kbit")
	time.sleep(0.923)
	tracef.write(f"2095 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2095kbit")
	time.sleep(0.764)
	tracef.write(f"572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 572kbit")
	time.sleep(0.262)
	tracef.write(f"1389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1389kbit")
	time.sleep(0.53)
	tracef.write(f"1694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1694kbit")
	time.sleep(0.706)
	tracef.write(f"1741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1741kbit")
	time.sleep(0.258)
	tracef.write(f"1778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1778kbit")
	time.sleep(0.83)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(0.365)
	tracef.write(f"1549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1549kbit")
	time.sleep(0.361)
	tracef.write(f"1975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1975kbit")
	time.sleep(0.329)
	tracef.write(f"709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 709kbit")
	time.sleep(0.885)
	tracef.write(f"2448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2448kbit")
	time.sleep(0.284)
	tracef.write(f"2252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2252kbit")
	time.sleep(0.783)
	tracef.write(f"1335 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1335kbit")
	time.sleep(0.727)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.461)
	tracef.write(f"483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 483kbit")
	time.sleep(0.82)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(0.918)
	tracef.write(f"1815 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1815kbit")
	time.sleep(0.862)
	tracef.write(f"601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 601kbit")
	time.sleep(0.28)
	tracef.write(f"2243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2243kbit")
	time.sleep(0.801)
	tracef.write(f"605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 605kbit")
	time.sleep(0.238)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(0.582)
	tracef.write(f"1759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1759kbit")
	time.sleep(0.659)
	tracef.write(f"628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 628kbit")
	time.sleep(0.411)
	tracef.write(f"803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 803kbit")
	time.sleep(0.904)
	tracef.write(f"1009 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1009kbit")
	time.sleep(0.517)
	tracef.write(f"979 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 979kbit")
	time.sleep(0.779)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.203)
	tracef.write(f"858 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 858kbit")
	time.sleep(0.254)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.341)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(0.551)
	tracef.write(f"799 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 799kbit")
	time.sleep(0.518)
	tracef.write(f"832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 832kbit")
	time.sleep(0.461)
	tracef.write(f"668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 668kbit")
	time.sleep(0.78)
	tracef.write(f"1433 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1433kbit")
	time.sleep(0.321)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.515)
	tracef.write(f"1812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1812kbit")
	time.sleep(0.649)
	tracef.write(f"2207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2207kbit")
	time.sleep(0.649)
	tracef.write(f"2196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2196kbit")
	time.sleep(0.752)
	tracef.write(f"672 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 672kbit")
	time.sleep(0.841)
	tracef.write(f"1825 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1825kbit")
	time.sleep(0.436)
	tracef.write(f"2338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2338kbit")
	time.sleep(0.302)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.394)
	tracef.write(f"2485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2485kbit")
	time.sleep(0.732)
	tracef.write(f"2533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2533kbit")
	time.sleep(0.553)
	tracef.write(f"2378 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2378kbit")
	time.sleep(0.654)
	tracef.write(f"377 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 377kbit")
	time.sleep(0.276)
	tracef.write(f"425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 425kbit")
	time.sleep(0.654)
	tracef.write(f"767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 767kbit")
	time.sleep(0.524)
	tracef.write(f"1858 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1858kbit")
	time.sleep(0.766)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(0.558)
	tracef.write(f"2078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2078kbit")
	time.sleep(0.886)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.48)
	tracef.write(f"840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 840kbit")
	time.sleep(0.233)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(0.57)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.358)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(0.417)
	tracef.write(f"1568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1568kbit")
	time.sleep(0.36)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.254)
	tracef.write(f"408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 408kbit")
	time.sleep(0.516)
	tracef.write(f"988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 988kbit")
	time.sleep(0.325)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.372)
	tracef.write(f"1141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1141kbit")
	time.sleep(0.329)
	tracef.write(f"715 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 715kbit")
	time.sleep(0.971)
	tracef.write(f"614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 614kbit")
	time.sleep(0.499)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.598)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(0.871)
	tracef.write(f"2042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2042kbit")
	time.sleep(0.404)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.366)
	tracef.write(f"411 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 411kbit")
	time.sleep(0.925)
	tracef.write(f"2156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2156kbit")
	time.sleep(0.317)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.737)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.615)
	tracef.write(f"751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 751kbit")
	time.sleep(0.426)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(0.263)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.571)
	tracef.write(f"2604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2604kbit")
	time.sleep(0.479)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.912)
	tracef.write(f"695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 695kbit")
	time.sleep(0.38)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.385)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(0.345)
	tracef.write(f"1869 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1869kbit")
	time.sleep(0.244)
	tracef.write(f"1968 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1968kbit")
	time.sleep(0.974)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.337)
	tracef.write(f"963 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 963kbit")
	time.sleep(0.841)
	tracef.write(f"1677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1677kbit")
	time.sleep(0.239)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(0.958)
	tracef.write(f"1933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1933kbit")
	time.sleep(0.786)
	tracef.write(f"658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 658kbit")
	time.sleep(0.609)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(0.798)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.926)
	tracef.write(f"1861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1861kbit")
	time.sleep(0.866)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.859)
	tracef.write(f"2102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2102kbit")
	time.sleep(0.878)
	tracef.write(f"774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 774kbit")
	time.sleep(0.701)
	tracef.write(f"1082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1082kbit")
	time.sleep(0.716)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.409)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.718)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.661)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(0.27)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.405)
	tracef.write(f"2486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2486kbit")
	time.sleep(0.842)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.822)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(0.647)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.54)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(0.655)
	tracef.write(f"441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 441kbit")
	time.sleep(0.616)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.586)
	tracef.write(f"696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 696kbit")
	time.sleep(0.371)
	tracef.write(f"2513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2513kbit")
	time.sleep(0.627)
	tracef.write(f"1660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1660kbit")
	time.sleep(0.532)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.899)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(0.601)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.347)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.798)
	tracef.write(f"378 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 378kbit")
	time.sleep(0.818)
	tracef.write(f"419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 419kbit")
	time.sleep(0.558)
	tracef.write(f"635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 635kbit")
	time.sleep(0.953)
	tracef.write(f"1385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1385kbit")
	time.sleep(0.722)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()