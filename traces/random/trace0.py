#t:156-875 ; rate:2277-2514 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace0.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace0.txt", 'a+')
	tracef.write(f"2409 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2409kbit")
	time.sleep(0.391)
	tracef.write(f"2490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2490kbit")
	time.sleep(0.788)
	tracef.write(f"2337 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2337kbit")
	time.sleep(0.518)
	tracef.write(f"2368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2368kbit")
	time.sleep(0.41)
	tracef.write(f"2310 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2310kbit")
	time.sleep(0.645)
	tracef.write(f"2469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2469kbit")
	time.sleep(0.43)
	tracef.write(f"2372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2372kbit")
	time.sleep(0.502)
	tracef.write(f"2433 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2433kbit")
	time.sleep(0.514)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.401)
	tracef.write(f"2330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2330kbit")
	time.sleep(0.504)
	tracef.write(f"2509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2509kbit")
	time.sleep(0.312)
	tracef.write(f"2452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2452kbit")
	time.sleep(0.319)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.418)
	tracef.write(f"2351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2351kbit")
	time.sleep(0.543)
	tracef.write(f"2281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2281kbit")
	time.sleep(0.832)
	tracef.write(f"2376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2376kbit")
	time.sleep(0.618)
	tracef.write(f"2446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2446kbit")
	time.sleep(0.703)
	tracef.write(f"2394 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2394kbit")
	time.sleep(0.668)
	tracef.write(f"2328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2328kbit")
	time.sleep(0.433)
	tracef.write(f"2444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2444kbit")
	time.sleep(0.416)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.866)
	tracef.write(f"2405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2405kbit")
	time.sleep(0.447)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.693)
	tracef.write(f"2285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2285kbit")
	time.sleep(0.497)
	tracef.write(f"2389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2389kbit")
	time.sleep(0.221)
	tracef.write(f"2474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2474kbit")
	time.sleep(0.315)
	tracef.write(f"2369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2369kbit")
	time.sleep(0.214)
	tracef.write(f"2325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2325kbit")
	time.sleep(0.333)
	tracef.write(f"2283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2283kbit")
	time.sleep(0.856)
	tracef.write(f"2353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2353kbit")
	time.sleep(0.521)
	tracef.write(f"2332 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2332kbit")
	time.sleep(0.242)
	tracef.write(f"2479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2479kbit")
	time.sleep(0.78)
	tracef.write(f"2374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2374kbit")
	time.sleep(0.759)
	tracef.write(f"2463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2463kbit")
	time.sleep(0.774)
	tracef.write(f"2477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2477kbit")
	time.sleep(0.509)
	tracef.write(f"2502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2502kbit")
	time.sleep(0.56)
	tracef.write(f"2335 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2335kbit")
	time.sleep(0.571)
	tracef.write(f"2389 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2389kbit")
	time.sleep(0.755)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.457)
	tracef.write(f"2354 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2354kbit")
	time.sleep(0.535)
	tracef.write(f"2428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2428kbit")
	time.sleep(0.339)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.407)
	tracef.write(f"2321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2321kbit")
	time.sleep(0.685)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.787)
	tracef.write(f"2374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2374kbit")
	time.sleep(0.713)
	tracef.write(f"2385 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2385kbit")
	time.sleep(0.296)
	tracef.write(f"2312 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2312kbit")
	time.sleep(0.549)
	tracef.write(f"2309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2309kbit")
	time.sleep(0.313)
	tracef.write(f"2436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2436kbit")
	time.sleep(0.281)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.873)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.63)
	tracef.write(f"2427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2427kbit")
	time.sleep(0.833)
	tracef.write(f"2391 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2391kbit")
	time.sleep(0.349)
	tracef.write(f"2470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2470kbit")
	time.sleep(0.6)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.62)
	tracef.write(f"2418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2418kbit")
	time.sleep(0.212)
	tracef.write(f"2401 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2401kbit")
	time.sleep(0.685)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.708)
	tracef.write(f"2296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2296kbit")
	time.sleep(0.632)
	tracef.write(f"2315 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2315kbit")
	time.sleep(0.839)
	tracef.write(f"2407 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2407kbit")
	time.sleep(0.85)
	tracef.write(f"2487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2487kbit")
	time.sleep(0.751)
	tracef.write(f"2447 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2447kbit")
	time.sleep(0.61)
	tracef.write(f"2509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2509kbit")
	time.sleep(0.823)
	tracef.write(f"2308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2308kbit")
	time.sleep(0.247)
	tracef.write(f"2425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2425kbit")
	time.sleep(0.206)
	tracef.write(f"2336 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2336kbit")
	time.sleep(0.37)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.802)
	tracef.write(f"2340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2340kbit")
	time.sleep(0.81)
	tracef.write(f"2297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2297kbit")
	time.sleep(0.298)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.746)
	tracef.write(f"2482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2482kbit")
	time.sleep(0.43)
	tracef.write(f"2421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2421kbit")
	time.sleep(0.659)
	tracef.write(f"2370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2370kbit")
	time.sleep(0.622)
	tracef.write(f"2434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2434kbit")
	time.sleep(0.643)
	tracef.write(f"2322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2322kbit")
	time.sleep(0.501)
	tracef.write(f"2482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2482kbit")
	time.sleep(0.347)
	tracef.write(f"2413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2413kbit")
	time.sleep(0.449)
	tracef.write(f"2466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2466kbit")
	time.sleep(0.198)
	tracef.write(f"2324 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2324kbit")
	time.sleep(0.658)
	tracef.write(f"2334 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2334kbit")
	time.sleep(0.601)
	tracef.write(f"2380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2380kbit")
	time.sleep(0.651)
	tracef.write(f"2304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2304kbit")
	time.sleep(0.665)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.438)
	tracef.write(f"2362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2362kbit")
	time.sleep(0.705)
	tracef.write(f"2375 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2375kbit")
	time.sleep(0.215)
	tracef.write(f"2423 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2423kbit")
	time.sleep(0.422)
	tracef.write(f"2499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2499kbit")
	time.sleep(0.699)
	tracef.write(f"2505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2505kbit")
	time.sleep(0.241)
	tracef.write(f"2326 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2326kbit")
	time.sleep(0.468)
	tracef.write(f"2446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2446kbit")
	time.sleep(0.157)
	tracef.write(f"2313 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2313kbit")
	time.sleep(0.7)
	tracef.write(f"2493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2493kbit")
	time.sleep(0.392)
	tracef.write(f"2294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2294kbit")
	time.sleep(0.179)
	tracef.write(f"2473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2473kbit")
	time.sleep(0.184)
	tracef.write(f"2339 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2339kbit")
	time.sleep(0.567)
	tracef.write(f"2297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2297kbit")
	time.sleep(0.281)
	tracef.write(f"2505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2505kbit")
	time.sleep(0.782)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.802)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.329)
	tracef.write(f"2417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2417kbit")
	time.sleep(0.663)
	tracef.write(f"2393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2393kbit")
	time.sleep(0.498)
	tracef.write(f"2313 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2313kbit")
	time.sleep(0.42)
	tracef.write(f"2322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2322kbit")
	time.sleep(0.537)
	tracef.write(f"2371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2371kbit")
	time.sleep(0.571)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.526)
	tracef.write(f"2361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2361kbit")
	time.sleep(0.368)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.31)
	tracef.write(f"2430 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2430kbit")
	time.sleep(0.288)
	tracef.write(f"2415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2415kbit")
	time.sleep(0.294)
	tracef.write(f"2441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2441kbit")
	time.sleep(0.564)
	tracef.write(f"2372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2372kbit")
	time.sleep(0.238)
	tracef.write(f"2321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2321kbit")
	time.sleep(0.673)
	tracef.write(f"2478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2478kbit")
	time.sleep(0.623)
	tracef.write(f"2331 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2331kbit")
	time.sleep(0.305)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.702)
	tracef.write(f"2348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2348kbit")
	time.sleep(0.869)
	tracef.write(f"2476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2476kbit")
	time.sleep(0.554)
	tracef.write(f"2296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2296kbit")
	time.sleep(0.209)
	tracef.write(f"2301 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2301kbit")
	time.sleep(0.607)
	tracef.write(f"2367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2367kbit")
	time.sleep(0.634)
	tracef.write(f"2401 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2401kbit")
	time.sleep(0.403)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.534)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.476)
	tracef.write(f"2368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2368kbit")
	time.sleep(0.797)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.692)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.62)
	tracef.write(f"2342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2342kbit")
	time.sleep(0.508)
	tracef.write(f"2488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2488kbit")
	time.sleep(0.643)
	tracef.write(f"2297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2297kbit")
	time.sleep(0.551)
	tracef.write(f"2497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2497kbit")
	time.sleep(0.304)
	tracef.write(f"2470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2470kbit")
	time.sleep(0.737)
	tracef.write(f"2299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2299kbit")
	time.sleep(0.805)
	tracef.write(f"2491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2491kbit")
	time.sleep(0.561)
	tracef.write(f"2441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2441kbit")
	time.sleep(0.534)
	tracef.write(f"2382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2382kbit")
	time.sleep(0.193)
	tracef.write(f"2277 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2277kbit")
	time.sleep(0.673)
	tracef.write(f"2372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2372kbit")
	time.sleep(0.285)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.561)
	tracef.write(f"2435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2435kbit")
	time.sleep(0.615)
	tracef.write(f"2442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2442kbit")
	time.sleep(0.651)
	tracef.write(f"2307 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2307kbit")
	time.sleep(0.75)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.227)
	tracef.write(f"2468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2468kbit")
	time.sleep(0.664)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.843)
	tracef.write(f"2402 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2402kbit")
	time.sleep(0.44)
	tracef.write(f"2356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2356kbit")
	time.sleep(0.512)
	tracef.write(f"2509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2509kbit")
	time.sleep(0.847)
	tracef.write(f"2325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2325kbit")
	time.sleep(0.806)
	tracef.write(f"2388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2388kbit")
	time.sleep(0.36)
	tracef.write(f"2407 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2407kbit")
	time.sleep(0.787)
	tracef.write(f"2436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2436kbit")
	time.sleep(0.794)
	tracef.write(f"2466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2466kbit")
	time.sleep(0.196)
	tracef.write(f"2445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2445kbit")
	time.sleep(0.87)
	tracef.write(f"2394 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2394kbit")
	time.sleep(0.223)
	tracef.write(f"2421 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2421kbit")
	time.sleep(0.54)
	tracef.write(f"2309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2309kbit")
	time.sleep(0.289)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.408)
	tracef.write(f"2399 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2399kbit")
	time.sleep(0.198)
	tracef.write(f"2296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2296kbit")
	time.sleep(0.156)
	tracef.write(f"2400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2400kbit")
	time.sleep(0.449)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.836)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.407)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.751)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.67)
	tracef.write(f"2469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2469kbit")
	time.sleep(0.723)
	tracef.write(f"2495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2495kbit")
	time.sleep(0.198)
	tracef.write(f"2362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2362kbit")
	time.sleep(0.606)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.651)
	tracef.write(f"2454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2454kbit")
	time.sleep(0.819)
	tracef.write(f"2440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2440kbit")
	time.sleep(0.683)
	tracef.write(f"2463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2463kbit")
	time.sleep(0.563)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.157)
	tracef.write(f"2444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2444kbit")
	time.sleep(0.357)
	tracef.write(f"2480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2480kbit")
	time.sleep(0.666)
	tracef.write(f"2284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2284kbit")
	time.sleep(0.446)
	tracef.write(f"2386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2386kbit")
	time.sleep(0.294)
	tracef.write(f"2281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2281kbit")
	time.sleep(0.359)
	tracef.write(f"2353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2353kbit")
	time.sleep(0.309)
	tracef.write(f"2379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2379kbit")
	time.sleep(0.365)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.76)
	tracef.write(f"2327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2327kbit")
	time.sleep(0.241)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.362)
	tracef.write(f"2465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2465kbit")
	time.sleep(0.608)
	tracef.write(f"2390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2390kbit")
	time.sleep(0.406)
	tracef.write(f"2358 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2358kbit")
	time.sleep(0.713)
	tracef.write(f"2321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2321kbit")
	time.sleep(0.452)
	tracef.write(f"2352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2352kbit")
	time.sleep(0.556)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.428)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.552)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()