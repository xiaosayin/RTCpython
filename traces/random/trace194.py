#t:373-580 ; rate:1303-2570 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace194.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace194.txt", 'a+')
	tracef.write(f"1842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1842kbit")
	time.sleep(0.498)
	tracef.write(f"2285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2285kbit")
	time.sleep(0.499)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.414)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.517)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(0.527)
	tracef.write(f"2125 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2125kbit")
	time.sleep(0.524)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.416)
	tracef.write(f"1346 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1346kbit")
	time.sleep(0.413)
	tracef.write(f"2173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2173kbit")
	time.sleep(0.567)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.413)
	tracef.write(f"2511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2511kbit")
	time.sleep(0.535)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.448)
	tracef.write(f"1829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1829kbit")
	time.sleep(0.38)
	tracef.write(f"2160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2160kbit")
	time.sleep(0.453)
	tracef.write(f"2252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2252kbit")
	time.sleep(0.485)
	tracef.write(f"1336 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1336kbit")
	time.sleep(0.555)
	tracef.write(f"2405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2405kbit")
	time.sleep(0.481)
	tracef.write(f"1807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1807kbit")
	time.sleep(0.558)
	tracef.write(f"1702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1702kbit")
	time.sleep(0.428)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(0.417)
	tracef.write(f"2203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2203kbit")
	time.sleep(0.374)
	tracef.write(f"2109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2109kbit")
	time.sleep(0.423)
	tracef.write(f"2429 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2429kbit")
	time.sleep(0.432)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(0.515)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.481)
	tracef.write(f"2233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2233kbit")
	time.sleep(0.546)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.479)
	tracef.write(f"2565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2565kbit")
	time.sleep(0.476)
	tracef.write(f"2130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2130kbit")
	time.sleep(0.4)
	tracef.write(f"2368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2368kbit")
	time.sleep(0.415)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.396)
	tracef.write(f"2120 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2120kbit")
	time.sleep(0.574)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(0.437)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.446)
	tracef.write(f"2379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2379kbit")
	time.sleep(0.523)
	tracef.write(f"1921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1921kbit")
	time.sleep(0.553)
	tracef.write(f"1738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1738kbit")
	time.sleep(0.56)
	tracef.write(f"1673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1673kbit")
	time.sleep(0.523)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(0.528)
	tracef.write(f"1780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1780kbit")
	time.sleep(0.554)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.386)
	tracef.write(f"2002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2002kbit")
	time.sleep(0.509)
	tracef.write(f"1966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1966kbit")
	time.sleep(0.455)
	tracef.write(f"2130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2130kbit")
	time.sleep(0.516)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.559)
	tracef.write(f"1769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1769kbit")
	time.sleep(0.544)
	tracef.write(f"2282 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2282kbit")
	time.sleep(0.516)
	tracef.write(f"1334 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1334kbit")
	time.sleep(0.508)
	tracef.write(f"1904 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1904kbit")
	time.sleep(0.497)
	tracef.write(f"1793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1793kbit")
	time.sleep(0.505)
	tracef.write(f"1524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1524kbit")
	time.sleep(0.542)
	tracef.write(f"1795 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1795kbit")
	time.sleep(0.384)
	tracef.write(f"2144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2144kbit")
	time.sleep(0.5)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.428)
	tracef.write(f"1821 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1821kbit")
	time.sleep(0.544)
	tracef.write(f"2416 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2416kbit")
	time.sleep(0.459)
	tracef.write(f"2498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2498kbit")
	time.sleep(0.468)
	tracef.write(f"2357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2357kbit")
	time.sleep(0.429)
	tracef.write(f"1772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1772kbit")
	time.sleep(0.542)
	tracef.write(f"2032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2032kbit")
	time.sleep(0.394)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.55)
	tracef.write(f"1842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1842kbit")
	time.sleep(0.522)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.382)
	tracef.write(f"1365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1365kbit")
	time.sleep(0.529)
	tracef.write(f"1657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1657kbit")
	time.sleep(0.542)
	tracef.write(f"2016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2016kbit")
	time.sleep(0.471)
	tracef.write(f"2558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2558kbit")
	time.sleep(0.488)
	tracef.write(f"2259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2259kbit")
	time.sleep(0.502)
	tracef.write(f"1735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1735kbit")
	time.sleep(0.497)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.553)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(0.505)
	tracef.write(f"1657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1657kbit")
	time.sleep(0.487)
	tracef.write(f"2127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2127kbit")
	time.sleep(0.573)
	tracef.write(f"1764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1764kbit")
	time.sleep(0.424)
	tracef.write(f"2107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2107kbit")
	time.sleep(0.46)
	tracef.write(f"2281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2281kbit")
	time.sleep(0.507)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(0.373)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.475)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.511)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.516)
	tracef.write(f"2120 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2120kbit")
	time.sleep(0.465)
	tracef.write(f"2548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2548kbit")
	time.sleep(0.437)
	tracef.write(f"2227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2227kbit")
	time.sleep(0.39)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.533)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.474)
	tracef.write(f"2090 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2090kbit")
	time.sleep(0.491)
	tracef.write(f"2102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2102kbit")
	time.sleep(0.484)
	tracef.write(f"2163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2163kbit")
	time.sleep(0.397)
	tracef.write(f"2382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2382kbit")
	time.sleep(0.437)
	tracef.write(f"2467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2467kbit")
	time.sleep(0.433)
	tracef.write(f"2114 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2114kbit")
	time.sleep(0.52)
	tracef.write(f"1712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1712kbit")
	time.sleep(0.502)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.418)
	tracef.write(f"1804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1804kbit")
	time.sleep(0.471)
	tracef.write(f"1343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1343kbit")
	time.sleep(0.38)
	tracef.write(f"2037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2037kbit")
	time.sleep(0.488)
	tracef.write(f"2482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2482kbit")
	time.sleep(0.541)
	tracef.write(f"2216 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2216kbit")
	time.sleep(0.469)
	tracef.write(f"2335 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2335kbit")
	time.sleep(0.524)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.441)
	tracef.write(f"2415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2415kbit")
	time.sleep(0.381)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.394)
	tracef.write(f"2102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2102kbit")
	time.sleep(0.509)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.568)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(0.434)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.52)
	tracef.write(f"2545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2545kbit")
	time.sleep(0.52)
	tracef.write(f"1867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1867kbit")
	time.sleep(0.541)
	tracef.write(f"1934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1934kbit")
	time.sleep(0.377)
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2381kbit")
	time.sleep(0.458)
	tracef.write(f"1866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1866kbit")
	time.sleep(0.579)
	tracef.write(f"1880 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1880kbit")
	time.sleep(0.373)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.482)
	tracef.write(f"1554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1554kbit")
	time.sleep(0.425)
	tracef.write(f"2492 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2492kbit")
	time.sleep(0.499)
	tracef.write(f"1791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1791kbit")
	time.sleep(0.512)
	tracef.write(f"2481 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2481kbit")
	time.sleep(0.561)
	tracef.write(f"2253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2253kbit")
	time.sleep(0.403)
	tracef.write(f"2431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2431kbit")
	time.sleep(0.472)
	tracef.write(f"1945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1945kbit")
	time.sleep(0.393)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.572)
	tracef.write(f"1763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1763kbit")
	time.sleep(0.558)
	tracef.write(f"1975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1975kbit")
	time.sleep(0.515)
	tracef.write(f"2371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2371kbit")
	time.sleep(0.383)
	tracef.write(f"2380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2380kbit")
	time.sleep(0.447)
	tracef.write(f"2452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2452kbit")
	time.sleep(0.559)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.449)
	tracef.write(f"2099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2099kbit")
	time.sleep(0.44)
	tracef.write(f"2209 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2209kbit")
	time.sleep(0.516)
	tracef.write(f"2426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2426kbit")
	time.sleep(0.496)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.56)
	tracef.write(f"1953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1953kbit")
	time.sleep(0.5)
	tracef.write(f"1836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1836kbit")
	time.sleep(0.456)
	tracef.write(f"2341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2341kbit")
	time.sleep(0.454)
	tracef.write(f"1816 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1816kbit")
	time.sleep(0.387)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.494)
	tracef.write(f"1958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1958kbit")
	time.sleep(0.558)
	tracef.write(f"1878 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1878kbit")
	time.sleep(0.419)
	tracef.write(f"2084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2084kbit")
	time.sleep(0.521)
	tracef.write(f"1716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1716kbit")
	time.sleep(0.442)
	tracef.write(f"1772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1772kbit")
	time.sleep(0.577)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(0.519)
	tracef.write(f"1788 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1788kbit")
	time.sleep(0.401)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(0.51)
	tracef.write(f"1933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1933kbit")
	time.sleep(0.466)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.471)
	tracef.write(f"1884 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1884kbit")
	time.sleep(0.394)
	tracef.write(f"2193 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2193kbit")
	time.sleep(0.529)
	tracef.write(f"1977 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1977kbit")
	time.sleep(0.567)
	tracef.write(f"2529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2529kbit")
	time.sleep(0.402)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.543)
	tracef.write(f"2503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2503kbit")
	time.sleep(0.409)
	tracef.write(f"1608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1608kbit")
	time.sleep(0.533)
	tracef.write(f"2420 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2420kbit")
	time.sleep(0.399)
	tracef.write(f"2401 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2401kbit")
	time.sleep(0.576)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.496)
	tracef.write(f"1979 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1979kbit")
	time.sleep(0.44)
	tracef.write(f"2229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2229kbit")
	time.sleep(0.569)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(0.448)
	tracef.write(f"2242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2242kbit")
	time.sleep(0.52)
	tracef.write(f"1716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1716kbit")
	time.sleep(0.568)
	tracef.write(f"2427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2427kbit")
	time.sleep(0.565)
	tracef.write(f"2416 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2416kbit")
	time.sleep(0.564)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.472)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.487)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.391)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(0.573)
	tracef.write(f"1499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1499kbit")
	time.sleep(0.403)
	tracef.write(f"2484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2484kbit")
	time.sleep(0.384)
	tracef.write(f"1837 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1837kbit")
	time.sleep(0.556)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.447)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.457)
	tracef.write(f"1379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1379kbit")
	time.sleep(0.442)
	tracef.write(f"1791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1791kbit")
	time.sleep(0.384)
	tracef.write(f"1737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1737kbit")
	time.sleep(0.464)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(0.379)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.385)
	tracef.write(f"2046 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2046kbit")
	time.sleep(0.485)
	tracef.write(f"2321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2321kbit")
	time.sleep(0.417)
	tracef.write(f"1777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1777kbit")
	time.sleep(0.483)
	tracef.write(f"2355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2355kbit")
	time.sleep(0.479)
	tracef.write(f"2161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2161kbit")
	time.sleep(0.47)
	tracef.write(f"2535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2535kbit")
	time.sleep(0.397)
	tracef.write(f"1846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1846kbit")
	time.sleep(0.576)
	tracef.write(f"1690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1690kbit")
	time.sleep(0.491)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.58)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.566)
	tracef.write(f"1867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1867kbit")
	time.sleep(0.471)
	tracef.write(f"2404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2404kbit")
	time.sleep(0.575)
	tracef.write(f"1950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1950kbit")
	time.sleep(0.429)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.516)
	tracef.write(f"1994 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1994kbit")
	time.sleep(0.537)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.456)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.554)
	tracef.write(f"1561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1561kbit")
	time.sleep(0.496)
	tracef.write(f"1695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1695kbit")
	time.sleep(0.466)
	tracef.write(f"2502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2502kbit")
	time.sleep(0.467)
	tracef.write(f"2148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2148kbit")
	time.sleep(0.376)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.528)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.383)
	tracef.write(f"1907 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1907kbit")
	time.sleep(0.435)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(0.439)
	tracef.write(f"2018 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2018kbit")
	time.sleep(0.52)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.458)
	tracef.write(f"1498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1498kbit")
	time.sleep(0.557)
	tracef.write(f"1333 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1333kbit")
	time.sleep(0.548)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.481)
	tracef.write(f"2230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2230kbit")
	time.sleep(0.455)
	tracef.write(f"2176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2176kbit")
	time.sleep(0.393)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()