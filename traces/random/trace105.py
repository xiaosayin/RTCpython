#t:454-776 ; rate:2015-2595 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace105.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace105.txt", 'a+')
	tracef.write(f"2151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2151kbit")
	time.sleep(0.711)
	tracef.write(f"2392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2392kbit")
	time.sleep(0.582)
	tracef.write(f"2310 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2310kbit")
	time.sleep(0.63)
	tracef.write(f"2477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2477kbit")
	time.sleep(0.749)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.584)
	tracef.write(f"2520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2520kbit")
	time.sleep(0.531)
	tracef.write(f"2594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2594kbit")
	time.sleep(0.602)
	tracef.write(f"2445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2445kbit")
	time.sleep(0.676)
	tracef.write(f"2256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2256kbit")
	time.sleep(0.72)
	tracef.write(f"2403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2403kbit")
	time.sleep(0.468)
	tracef.write(f"2233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2233kbit")
	time.sleep(0.696)
	tracef.write(f"2418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2418kbit")
	time.sleep(0.722)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.595)
	tracef.write(f"2074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2074kbit")
	time.sleep(0.735)
	tracef.write(f"2434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2434kbit")
	time.sleep(0.736)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.523)
	tracef.write(f"2135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2135kbit")
	time.sleep(0.534)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.759)
	tracef.write(f"2365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2365kbit")
	time.sleep(0.504)
	tracef.write(f"2190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2190kbit")
	time.sleep(0.621)
	tracef.write(f"2148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2148kbit")
	time.sleep(0.545)
	tracef.write(f"2437 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2437kbit")
	time.sleep(0.641)
	tracef.write(f"2382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2382kbit")
	time.sleep(0.572)
	tracef.write(f"2485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2485kbit")
	time.sleep(0.617)
	tracef.write(f"2147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2147kbit")
	time.sleep(0.702)
	tracef.write(f"2219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2219kbit")
	time.sleep(0.468)
	tracef.write(f"2270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2270kbit")
	time.sleep(0.549)
	tracef.write(f"2121 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2121kbit")
	time.sleep(0.701)
	tracef.write(f"2162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2162kbit")
	time.sleep(0.656)
	tracef.write(f"2289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2289kbit")
	time.sleep(0.593)
	tracef.write(f"2302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2302kbit")
	time.sleep(0.671)
	tracef.write(f"2211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2211kbit")
	time.sleep(0.634)
	tracef.write(f"2142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2142kbit")
	time.sleep(0.727)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.505)
	tracef.write(f"2168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2168kbit")
	time.sleep(0.72)
	tracef.write(f"2126 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2126kbit")
	time.sleep(0.528)
	tracef.write(f"2306 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2306kbit")
	time.sleep(0.559)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.747)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.499)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.573)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.477)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.68)
	tracef.write(f"2279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2279kbit")
	time.sleep(0.749)
	tracef.write(f"2421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2421kbit")
	time.sleep(0.644)
	tracef.write(f"2126 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2126kbit")
	time.sleep(0.756)
	tracef.write(f"2162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2162kbit")
	time.sleep(0.478)
	tracef.write(f"2558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2558kbit")
	time.sleep(0.584)
	tracef.write(f"2349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2349kbit")
	time.sleep(0.56)
	tracef.write(f"2111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2111kbit")
	time.sleep(0.699)
	tracef.write(f"2305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2305kbit")
	time.sleep(0.698)
	tracef.write(f"2438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2438kbit")
	time.sleep(0.508)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.554)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.695)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.637)
	tracef.write(f"2497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2497kbit")
	time.sleep(0.553)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.494)
	tracef.write(f"2590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2590kbit")
	time.sleep(0.727)
	tracef.write(f"2443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2443kbit")
	time.sleep(0.651)
	tracef.write(f"2360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2360kbit")
	time.sleep(0.519)
	tracef.write(f"2321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2321kbit")
	time.sleep(0.67)
	tracef.write(f"2047 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2047kbit")
	time.sleep(0.507)
	tracef.write(f"2491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2491kbit")
	time.sleep(0.634)
	tracef.write(f"2178 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2178kbit")
	time.sleep(0.644)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.533)
	tracef.write(f"2113 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2113kbit")
	time.sleep(0.667)
	tracef.write(f"2375 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2375kbit")
	time.sleep(0.7)
	tracef.write(f"2123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2123kbit")
	time.sleep(0.697)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.74)
	tracef.write(f"2348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2348kbit")
	time.sleep(0.702)
	tracef.write(f"2342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2342kbit")
	time.sleep(0.478)
	tracef.write(f"2183 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2183kbit")
	time.sleep(0.527)
	tracef.write(f"2367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2367kbit")
	time.sleep(0.597)
	tracef.write(f"2023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2023kbit")
	time.sleep(0.754)
	tracef.write(f"2341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2341kbit")
	time.sleep(0.549)
	tracef.write(f"2426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2426kbit")
	time.sleep(0.614)
	tracef.write(f"2428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2428kbit")
	time.sleep(0.531)
	tracef.write(f"2547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2547kbit")
	time.sleep(0.75)
	tracef.write(f"2344 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2344kbit")
	time.sleep(0.74)
	tracef.write(f"2330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2330kbit")
	time.sleep(0.692)
	tracef.write(f"2122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2122kbit")
	time.sleep(0.538)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.765)
	tracef.write(f"2488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2488kbit")
	time.sleep(0.546)
	tracef.write(f"2414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2414kbit")
	time.sleep(0.574)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.763)
	tracef.write(f"2456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2456kbit")
	time.sleep(0.545)
	tracef.write(f"2371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2371kbit")
	time.sleep(0.507)
	tracef.write(f"2128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2128kbit")
	time.sleep(0.73)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.508)
	tracef.write(f"2339 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2339kbit")
	time.sleep(0.672)
	tracef.write(f"2226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2226kbit")
	time.sleep(0.577)
	tracef.write(f"2151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2151kbit")
	time.sleep(0.648)
	tracef.write(f"2136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2136kbit")
	time.sleep(0.676)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.695)
	tracef.write(f"2535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2535kbit")
	time.sleep(0.721)
	tracef.write(f"2205 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2205kbit")
	time.sleep(0.705)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.617)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.488)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.468)
	tracef.write(f"2269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2269kbit")
	time.sleep(0.619)
	tracef.write(f"2177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2177kbit")
	time.sleep(0.679)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.478)
	tracef.write(f"2129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2129kbit")
	time.sleep(0.588)
	tracef.write(f"2449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2449kbit")
	time.sleep(0.709)
	tracef.write(f"2094 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2094kbit")
	time.sleep(0.494)
	tracef.write(f"2417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2417kbit")
	time.sleep(0.465)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.567)
	tracef.write(f"2498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2498kbit")
	time.sleep(0.635)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.63)
	tracef.write(f"2050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2050kbit")
	time.sleep(0.613)
	tracef.write(f"2523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2523kbit")
	time.sleep(0.475)
	tracef.write(f"2196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2196kbit")
	time.sleep(0.561)
	tracef.write(f"2149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2149kbit")
	time.sleep(0.572)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.676)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.659)
	tracef.write(f"2428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2428kbit")
	time.sleep(0.634)
	tracef.write(f"2375 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2375kbit")
	time.sleep(0.533)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.662)
	tracef.write(f"2526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2526kbit")
	time.sleep(0.686)
	tracef.write(f"2315 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2315kbit")
	time.sleep(0.678)
	tracef.write(f"2233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2233kbit")
	time.sleep(0.76)
	tracef.write(f"2576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2576kbit")
	time.sleep(0.638)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.705)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.731)
	tracef.write(f"2172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2172kbit")
	time.sleep(0.737)
	tracef.write(f"2469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2469kbit")
	time.sleep(0.5)
	tracef.write(f"2472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2472kbit")
	time.sleep(0.577)
	tracef.write(f"2342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2342kbit")
	time.sleep(0.657)
	tracef.write(f"2548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2548kbit")
	time.sleep(0.51)
	tracef.write(f"2069 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2069kbit")
	time.sleep(0.455)
	tracef.write(f"2272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2272kbit")
	time.sleep(0.602)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.648)
	tracef.write(f"2123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2123kbit")
	time.sleep(0.513)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.482)
	tracef.write(f"2201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2201kbit")
	time.sleep(0.744)
	tracef.write(f"2298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2298kbit")
	time.sleep(0.607)
	tracef.write(f"2380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2380kbit")
	time.sleep(0.748)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.681)
	tracef.write(f"2546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2546kbit")
	time.sleep(0.745)
	tracef.write(f"2103 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2103kbit")
	time.sleep(0.677)
	tracef.write(f"2226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2226kbit")
	time.sleep(0.705)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.476)
	tracef.write(f"2449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2449kbit")
	time.sleep(0.577)
	tracef.write(f"2092 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2092kbit")
	time.sleep(0.494)
	tracef.write(f"2112 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2112kbit")
	time.sleep(0.61)
	tracef.write(f"2270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2270kbit")
	time.sleep(0.592)
	tracef.write(f"2117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2117kbit")
	time.sleep(0.48)
	tracef.write(f"2396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2396kbit")
	time.sleep(0.503)
	tracef.write(f"2222 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2222kbit")
	time.sleep(0.668)
	tracef.write(f"2568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2568kbit")
	time.sleep(0.637)
	tracef.write(f"2581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2581kbit")
	time.sleep(0.569)
	tracef.write(f"2480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2480kbit")
	time.sleep(0.559)
	tracef.write(f"2241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2241kbit")
	time.sleep(0.464)
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2525kbit")
	time.sleep(0.665)
	tracef.write(f"2466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2466kbit")
	time.sleep(0.711)
	tracef.write(f"2080 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2080kbit")
	time.sleep(0.579)
	tracef.write(f"2082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2082kbit")
	time.sleep(0.585)
	tracef.write(f"2196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2196kbit")
	time.sleep(0.607)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.541)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.612)
	tracef.write(f"2088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2088kbit")
	time.sleep(0.501)
	tracef.write(f"2087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2087kbit")
	time.sleep(0.476)
	tracef.write(f"2469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2469kbit")
	time.sleep(0.576)
	tracef.write(f"2277 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2277kbit")
	time.sleep(0.528)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()