#t:356-793 ; rate:1564-2673 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace84.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace84.txt", 'a+')
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1596kbit")
	time.sleep(0.58)
	tracef.write(f"2213 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2213kbit")
	time.sleep(0.553)
	tracef.write(f"2205 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2205kbit")
	time.sleep(0.664)
	tracef.write(f"2441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2441kbit")
	time.sleep(0.764)
	tracef.write(f"2246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2246kbit")
	time.sleep(0.466)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.722)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.399)
	tracef.write(f"2373 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2373kbit")
	time.sleep(0.53)
	tracef.write(f"2536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2536kbit")
	time.sleep(0.357)
	tracef.write(f"1692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1692kbit")
	time.sleep(0.471)
	tracef.write(f"2201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2201kbit")
	time.sleep(0.623)
	tracef.write(f"1769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1769kbit")
	time.sleep(0.531)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.357)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.438)
	tracef.write(f"2304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2304kbit")
	time.sleep(0.707)
	tracef.write(f"2332 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2332kbit")
	time.sleep(0.662)
	tracef.write(f"1809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1809kbit")
	time.sleep(0.714)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.581)
	tracef.write(f"1788 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1788kbit")
	time.sleep(0.695)
	tracef.write(f"2299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2299kbit")
	time.sleep(0.773)
	tracef.write(f"2454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2454kbit")
	time.sleep(0.76)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.49)
	tracef.write(f"2058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2058kbit")
	time.sleep(0.508)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.468)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.541)
	tracef.write(f"2225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2225kbit")
	time.sleep(0.476)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.523)
	tracef.write(f"2042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2042kbit")
	time.sleep(0.369)
	tracef.write(f"2618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2618kbit")
	time.sleep(0.631)
	tracef.write(f"1662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1662kbit")
	time.sleep(0.771)
	tracef.write(f"2084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2084kbit")
	time.sleep(0.697)
	tracef.write(f"2234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2234kbit")
	time.sleep(0.514)
	tracef.write(f"1875 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1875kbit")
	time.sleep(0.507)
	tracef.write(f"2290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2290kbit")
	time.sleep(0.719)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.665)
	tracef.write(f"2117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2117kbit")
	time.sleep(0.765)
	tracef.write(f"2518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2518kbit")
	time.sleep(0.682)
	tracef.write(f"1731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1731kbit")
	time.sleep(0.485)
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1676kbit")
	time.sleep(0.539)
	tracef.write(f"2201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2201kbit")
	time.sleep(0.471)
	tracef.write(f"2320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2320kbit")
	time.sleep(0.403)
	tracef.write(f"2168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2168kbit")
	time.sleep(0.371)
	tracef.write(f"1820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1820kbit")
	time.sleep(0.41)
	tracef.write(f"2057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2057kbit")
	time.sleep(0.535)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.525)
	tracef.write(f"2254 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2254kbit")
	time.sleep(0.599)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.696)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.775)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.536)
	tracef.write(f"2611 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2611kbit")
	time.sleep(0.625)
	tracef.write(f"2225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2225kbit")
	time.sleep(0.752)
	tracef.write(f"2179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2179kbit")
	time.sleep(0.785)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.487)
	tracef.write(f"1760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1760kbit")
	time.sleep(0.456)
	tracef.write(f"2348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2348kbit")
	time.sleep(0.388)
	tracef.write(f"2573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2573kbit")
	time.sleep(0.589)
	tracef.write(f"2151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2151kbit")
	time.sleep(0.481)
	tracef.write(f"2287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2287kbit")
	time.sleep(0.552)
	tracef.write(f"1995 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1995kbit")
	time.sleep(0.48)
	tracef.write(f"2076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2076kbit")
	time.sleep(0.624)
	tracef.write(f"1778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1778kbit")
	time.sleep(0.433)
	tracef.write(f"2258 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2258kbit")
	time.sleep(0.772)
	tracef.write(f"2270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2270kbit")
	time.sleep(0.401)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.566)
	tracef.write(f"2313 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2313kbit")
	time.sleep(0.58)
	tracef.write(f"1806 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1806kbit")
	time.sleep(0.518)
	tracef.write(f"1815 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1815kbit")
	time.sleep(0.669)
	tracef.write(f"1766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1766kbit")
	time.sleep(0.751)
	tracef.write(f"2131 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2131kbit")
	time.sleep(0.401)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.608)
	tracef.write(f"2383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2383kbit")
	time.sleep(0.518)
	tracef.write(f"2239 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2239kbit")
	time.sleep(0.743)
	tracef.write(f"2045 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2045kbit")
	time.sleep(0.673)
	tracef.write(f"2337 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2337kbit")
	time.sleep(0.372)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.497)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.381)
	tracef.write(f"2617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2617kbit")
	time.sleep(0.62)
	tracef.write(f"2267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2267kbit")
	time.sleep(0.73)
	tracef.write(f"1577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1577kbit")
	time.sleep(0.725)
	tracef.write(f"2295 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2295kbit")
	time.sleep(0.374)
	tracef.write(f"1812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1812kbit")
	time.sleep(0.429)
	tracef.write(f"2340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2340kbit")
	time.sleep(0.502)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.624)
	tracef.write(f"1618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1618kbit")
	time.sleep(0.372)
	tracef.write(f"1991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1991kbit")
	time.sleep(0.368)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.653)
	tracef.write(f"2632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2632kbit")
	time.sleep(0.429)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.735)
	tracef.write(f"2364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2364kbit")
	time.sleep(0.699)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.783)
	tracef.write(f"2551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2551kbit")
	time.sleep(0.543)
	tracef.write(f"2520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2520kbit")
	time.sleep(0.679)
	tracef.write(f"1741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1741kbit")
	time.sleep(0.446)
	tracef.write(f"2591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2591kbit")
	time.sleep(0.376)
	tracef.write(f"2496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2496kbit")
	time.sleep(0.361)
	tracef.write(f"2134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2134kbit")
	time.sleep(0.445)
	tracef.write(f"1939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1939kbit")
	time.sleep(0.579)
	tracef.write(f"2620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2620kbit")
	time.sleep(0.772)
	tracef.write(f"2448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2448kbit")
	time.sleep(0.773)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.762)
	tracef.write(f"1896 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1896kbit")
	time.sleep(0.782)
	tracef.write(f"1782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1782kbit")
	time.sleep(0.698)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.536)
	tracef.write(f"2107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2107kbit")
	time.sleep(0.791)
	tracef.write(f"2431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2431kbit")
	time.sleep(0.421)
	tracef.write(f"2492 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2492kbit")
	time.sleep(0.597)
	tracef.write(f"1731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1731kbit")
	time.sleep(0.542)
	tracef.write(f"2551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2551kbit")
	time.sleep(0.389)
	tracef.write(f"2669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2669kbit")
	time.sleep(0.739)
	tracef.write(f"1635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1635kbit")
	time.sleep(0.483)
	tracef.write(f"2632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2632kbit")
	time.sleep(0.481)
	tracef.write(f"2240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2240kbit")
	time.sleep(0.774)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.726)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.373)
	tracef.write(f"1840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1840kbit")
	time.sleep(0.493)
	tracef.write(f"2378 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2378kbit")
	time.sleep(0.43)
	tracef.write(f"2652 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2652kbit")
	time.sleep(0.76)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.514)
	tracef.write(f"2600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2600kbit")
	time.sleep(0.679)
	tracef.write(f"2056 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2056kbit")
	time.sleep(0.598)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.603)
	tracef.write(f"2507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2507kbit")
	time.sleep(0.518)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.61)
	tracef.write(f"1944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1944kbit")
	time.sleep(0.513)
	tracef.write(f"1735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1735kbit")
	time.sleep(0.603)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.518)
	tracef.write(f"1717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1717kbit")
	time.sleep(0.563)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.551)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.697)
	tracef.write(f"1897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1897kbit")
	time.sleep(0.582)
	tracef.write(f"2319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2319kbit")
	time.sleep(0.378)
	tracef.write(f"1569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1569kbit")
	time.sleep(0.793)
	tracef.write(f"1766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1766kbit")
	time.sleep(0.384)
	tracef.write(f"2514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2514kbit")
	time.sleep(0.542)
	tracef.write(f"2066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2066kbit")
	time.sleep(0.404)
	tracef.write(f"2435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2435kbit")
	time.sleep(0.726)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.432)
	tracef.write(f"2485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2485kbit")
	time.sleep(0.655)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.657)
	tracef.write(f"1792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1792kbit")
	time.sleep(0.473)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.525)
	tracef.write(f"2564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2564kbit")
	time.sleep(0.552)
	tracef.write(f"2392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2392kbit")
	time.sleep(0.601)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.769)
	tracef.write(f"1627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1627kbit")
	time.sleep(0.634)
	tracef.write(f"2647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2647kbit")
	time.sleep(0.373)
	tracef.write(f"1728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1728kbit")
	time.sleep(0.553)
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1676kbit")
	time.sleep(0.407)
	tracef.write(f"2164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2164kbit")
	time.sleep(0.39)
	tracef.write(f"1707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1707kbit")
	time.sleep(0.567)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.532)
	tracef.write(f"2217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2217kbit")
	time.sleep(0.474)
	tracef.write(f"1754 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1754kbit")
	time.sleep(0.538)
	tracef.write(f"1772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1772kbit")
	time.sleep(0.364)
	tracef.write(f"1823 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1823kbit")
	time.sleep(0.689)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.458)
	tracef.write(f"2554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2554kbit")
	time.sleep(0.469)
	tracef.write(f"1915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1915kbit")
	time.sleep(0.703)
	tracef.write(f"1853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1853kbit")
	time.sleep(0.587)
	tracef.write(f"2387 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2387kbit")
	time.sleep(0.719)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.59)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.522)
	tracef.write(f"2621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2621kbit")
	time.sleep(0.726)
	tracef.write(f"1853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1853kbit")
	time.sleep(0.74)
	tracef.write(f"2605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2605kbit")
	time.sleep(0.791)
	tracef.write(f"1649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1649kbit")
	time.sleep(0.746)
	tracef.write(f"1763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1763kbit")
	time.sleep(0.77)
	tracef.write(f"1774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1774kbit")
	time.sleep(0.525)
	tracef.write(f"2408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2408kbit")
	time.sleep(0.726)
	tracef.write(f"2402 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2402kbit")
	time.sleep(0.365)
	tracef.write(f"1920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1920kbit")
	time.sleep(0.656)
	tracef.write(f"2048 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2048kbit")
	time.sleep(0.627)
	tracef.write(f"2434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2434kbit")
	time.sleep(0.782)
	tracef.write(f"2355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2355kbit")
	time.sleep(0.738)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()