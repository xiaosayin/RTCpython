#t:832-878 ; rate:1869-2606 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace168.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace168.txt", 'a+')
	tracef.write(f"1968 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1968kbit")
	time.sleep(0.856)
	tracef.write(f"2204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2204kbit")
	time.sleep(0.842)
	tracef.write(f"2139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2139kbit")
	time.sleep(0.878)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.842)
	tracef.write(f"2591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2591kbit")
	time.sleep(0.85)
	tracef.write(f"2191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2191kbit")
	time.sleep(0.849)
	tracef.write(f"2495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2495kbit")
	time.sleep(0.878)
	tracef.write(f"1888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1888kbit")
	time.sleep(0.855)
	tracef.write(f"2309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2309kbit")
	time.sleep(0.836)
	tracef.write(f"2356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2356kbit")
	time.sleep(0.851)
	tracef.write(f"1941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1941kbit")
	time.sleep(0.841)
	tracef.write(f"2359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2359kbit")
	time.sleep(0.845)
	tracef.write(f"2365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2365kbit")
	time.sleep(0.854)
	tracef.write(f"2185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2185kbit")
	time.sleep(0.875)
	tracef.write(f"2198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2198kbit")
	time.sleep(0.864)
	tracef.write(f"2207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2207kbit")
	time.sleep(0.874)
	tracef.write(f"2127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2127kbit")
	time.sleep(0.856)
	tracef.write(f"2128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2128kbit")
	time.sleep(0.864)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.837)
	tracef.write(f"2436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2436kbit")
	time.sleep(0.864)
	tracef.write(f"2307 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2307kbit")
	time.sleep(0.847)
	tracef.write(f"2262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2262kbit")
	time.sleep(0.869)
	tracef.write(f"2466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2466kbit")
	time.sleep(0.872)
	tracef.write(f"2358 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2358kbit")
	time.sleep(0.869)
	tracef.write(f"2469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2469kbit")
	time.sleep(0.859)
	tracef.write(f"2384 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2384kbit")
	time.sleep(0.876)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.866)
	tracef.write(f"2456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2456kbit")
	time.sleep(0.872)
	tracef.write(f"2140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2140kbit")
	time.sleep(0.846)
	tracef.write(f"2592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2592kbit")
	time.sleep(0.875)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.833)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.832)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.843)
	tracef.write(f"2228 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2228kbit")
	time.sleep(0.859)
	tracef.write(f"2040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2040kbit")
	time.sleep(0.836)
	tracef.write(f"2048 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2048kbit")
	time.sleep(0.861)
	tracef.write(f"2582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2582kbit")
	time.sleep(0.849)
	tracef.write(f"2374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2374kbit")
	time.sleep(0.846)
	tracef.write(f"2259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2259kbit")
	time.sleep(0.874)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.86)
	tracef.write(f"2291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2291kbit")
	time.sleep(0.852)
	tracef.write(f"2022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2022kbit")
	time.sleep(0.835)
	tracef.write(f"2575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2575kbit")
	time.sleep(0.868)
	tracef.write(f"2023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2023kbit")
	time.sleep(0.832)
	tracef.write(f"2393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2393kbit")
	time.sleep(0.856)
	tracef.write(f"2426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2426kbit")
	time.sleep(0.848)
	tracef.write(f"2403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2403kbit")
	time.sleep(0.872)
	tracef.write(f"2596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2596kbit")
	time.sleep(0.858)
	tracef.write(f"2142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2142kbit")
	time.sleep(0.836)
	tracef.write(f"1994 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1994kbit")
	time.sleep(0.854)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.865)
	tracef.write(f"2589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2589kbit")
	time.sleep(0.871)
	tracef.write(f"2501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2501kbit")
	time.sleep(0.848)
	tracef.write(f"2185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2185kbit")
	time.sleep(0.876)
	tracef.write(f"2083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2083kbit")
	time.sleep(0.864)
	tracef.write(f"2584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2584kbit")
	time.sleep(0.871)
	tracef.write(f"2185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2185kbit")
	time.sleep(0.876)
	tracef.write(f"2586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2586kbit")
	time.sleep(0.863)
	tracef.write(f"2395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2395kbit")
	time.sleep(0.86)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.836)
	tracef.write(f"1885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1885kbit")
	time.sleep(0.845)
	tracef.write(f"2370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2370kbit")
	time.sleep(0.844)
	tracef.write(f"2187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2187kbit")
	time.sleep(0.848)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.842)
	tracef.write(f"1984 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1984kbit")
	time.sleep(0.832)
	tracef.write(f"2431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2431kbit")
	time.sleep(0.849)
	tracef.write(f"2524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2524kbit")
	time.sleep(0.869)
	tracef.write(f"2020 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2020kbit")
	time.sleep(0.862)
	tracef.write(f"2256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2256kbit")
	time.sleep(0.843)
	tracef.write(f"2271 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2271kbit")
	time.sleep(0.872)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.844)
	tracef.write(f"2376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2376kbit")
	time.sleep(0.844)
	tracef.write(f"2188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2188kbit")
	time.sleep(0.835)
	tracef.write(f"2429 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2429kbit")
	time.sleep(0.849)
	tracef.write(f"2184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2184kbit")
	time.sleep(0.863)
	tracef.write(f"2545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2545kbit")
	time.sleep(0.841)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.833)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.857)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.853)
	tracef.write(f"1948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1948kbit")
	time.sleep(0.834)
	tracef.write(f"2148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2148kbit")
	time.sleep(0.876)
	tracef.write(f"2352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2352kbit")
	time.sleep(0.837)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.859)
	tracef.write(f"2391 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2391kbit")
	time.sleep(0.851)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.858)
	tracef.write(f"2424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2424kbit")
	time.sleep(0.873)
	tracef.write(f"2424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2424kbit")
	time.sleep(0.841)
	tracef.write(f"2359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2359kbit")
	time.sleep(0.862)
	tracef.write(f"2384 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2384kbit")
	time.sleep(0.871)
	tracef.write(f"2480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2480kbit")
	time.sleep(0.869)
	tracef.write(f"2287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2287kbit")
	time.sleep(0.86)
	tracef.write(f"2015 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2015kbit")
	time.sleep(0.867)
	tracef.write(f"2464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2464kbit")
	time.sleep(0.859)
	tracef.write(f"2110 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2110kbit")
	time.sleep(0.841)
	tracef.write(f"2010 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2010kbit")
	time.sleep(0.838)
	tracef.write(f"2454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2454kbit")
	time.sleep(0.875)
	tracef.write(f"2203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2203kbit")
	time.sleep(0.854)
	tracef.write(f"2237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2237kbit")
	time.sleep(0.866)
	tracef.write(f"2037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2037kbit")
	time.sleep(0.835)
	tracef.write(f"2213 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2213kbit")
	time.sleep(0.869)
	tracef.write(f"2359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2359kbit")
	time.sleep(0.866)
	tracef.write(f"1899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1899kbit")
	time.sleep(0.84)
	tracef.write(f"1924 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1924kbit")
	time.sleep(0.87)
	tracef.write(f"2064 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2064kbit")
	time.sleep(0.87)
	tracef.write(f"2305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2305kbit")
	time.sleep(0.871)
	tracef.write(f"2370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2370kbit")
	time.sleep(0.841)
	tracef.write(f"2128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2128kbit")
	time.sleep(0.857)
	tracef.write(f"2000 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2000kbit")
	time.sleep(0.87)
	tracef.write(f"2503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2503kbit")
	time.sleep(0.867)
	tracef.write(f"2049 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2049kbit")
	time.sleep(0.84)
	tracef.write(f"2595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2595kbit")
	time.sleep(0.853)
	tracef.write(f"2049 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2049kbit")
	time.sleep(0.833)
	tracef.write(f"2129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2129kbit")
	time.sleep(0.847)
	tracef.write(f"2427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2427kbit")
	time.sleep(0.838)
	tracef.write(f"2432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2432kbit")
	time.sleep(0.877)
	tracef.write(f"2139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2139kbit")
	time.sleep(0.876)
	tracef.write(f"2057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2057kbit")
	time.sleep(0.873)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()