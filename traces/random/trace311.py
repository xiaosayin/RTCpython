#t:118-954 ; rate:2453-2569 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace311.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace311.txt", 'a+')
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2525kbit")
	time.sleep(0.421)
	tracef.write(f"2552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2552kbit")
	time.sleep(0.702)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.663)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.784)
	tracef.write(f"2503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2503kbit")
	time.sleep(0.83)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.342)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.824)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.142)
	tracef.write(f"2556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2556kbit")
	time.sleep(0.459)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.425)
	tracef.write(f"2484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2484kbit")
	time.sleep(0.853)
	tracef.write(f"2502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2502kbit")
	time.sleep(0.329)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.839)
	tracef.write(f"2470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2470kbit")
	time.sleep(0.592)
	tracef.write(f"2537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2537kbit")
	time.sleep(0.403)
	tracef.write(f"2499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2499kbit")
	time.sleep(0.498)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.887)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.157)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.903)
	tracef.write(f"2538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2538kbit")
	time.sleep(0.823)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.608)
	tracef.write(f"2521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2521kbit")
	time.sleep(0.75)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.923)
	tracef.write(f"2541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2541kbit")
	time.sleep(0.249)
	tracef.write(f"2480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2480kbit")
	time.sleep(0.84)
	tracef.write(f"2488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2488kbit")
	time.sleep(0.866)
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2525kbit")
	time.sleep(0.217)
	tracef.write(f"2458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2458kbit")
	time.sleep(0.929)
	tracef.write(f"2511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2511kbit")
	time.sleep(0.916)
	tracef.write(f"2462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2462kbit")
	time.sleep(0.126)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.549)
	tracef.write(f"2544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2544kbit")
	time.sleep(0.606)
	tracef.write(f"2465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2465kbit")
	time.sleep(0.67)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.191)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.752)
	tracef.write(f"2513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2513kbit")
	time.sleep(0.376)
	tracef.write(f"2526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2526kbit")
	time.sleep(0.385)
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2525kbit")
	time.sleep(0.81)
	tracef.write(f"2509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2509kbit")
	time.sleep(0.726)
	tracef.write(f"2556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2556kbit")
	time.sleep(0.808)
	tracef.write(f"2474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2474kbit")
	time.sleep(0.913)
	tracef.write(f"2474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2474kbit")
	time.sleep(0.74)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.628)
	tracef.write(f"2533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2533kbit")
	time.sleep(0.794)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.409)
	tracef.write(f"2468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2468kbit")
	time.sleep(0.136)
	tracef.write(f"2518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2518kbit")
	time.sleep(0.391)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.932)
	tracef.write(f"2531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2531kbit")
	time.sleep(0.144)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.186)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.675)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.315)
	tracef.write(f"2473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2473kbit")
	time.sleep(0.439)
	tracef.write(f"2465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2465kbit")
	time.sleep(0.934)
	tracef.write(f"2454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2454kbit")
	time.sleep(0.676)
	tracef.write(f"2481 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2481kbit")
	time.sleep(0.129)
	tracef.write(f"2468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2468kbit")
	time.sleep(0.198)
	tracef.write(f"2508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2508kbit")
	time.sleep(0.405)
	tracef.write(f"2529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2529kbit")
	time.sleep(0.728)
	tracef.write(f"2555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2555kbit")
	time.sleep(0.259)
	tracef.write(f"2501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2501kbit")
	time.sleep(0.654)
	tracef.write(f"2487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2487kbit")
	time.sleep(0.331)
	tracef.write(f"2532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2532kbit")
	time.sleep(0.178)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.855)
	tracef.write(f"2503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2503kbit")
	time.sleep(0.458)
	tracef.write(f"2546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2546kbit")
	time.sleep(0.777)
	tracef.write(f"2471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2471kbit")
	time.sleep(0.841)
	tracef.write(f"2477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2477kbit")
	time.sleep(0.18)
	tracef.write(f"2473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2473kbit")
	time.sleep(0.486)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.788)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.615)
	tracef.write(f"2478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2478kbit")
	time.sleep(0.811)
	tracef.write(f"2548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2548kbit")
	time.sleep(0.294)
	tracef.write(f"2454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2454kbit")
	time.sleep(0.741)
	tracef.write(f"2494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2494kbit")
	time.sleep(0.476)
	tracef.write(f"2460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2460kbit")
	time.sleep(0.926)
	tracef.write(f"2534 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2534kbit")
	time.sleep(0.2)
	tracef.write(f"2544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2544kbit")
	time.sleep(0.647)
	tracef.write(f"2540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2540kbit")
	time.sleep(0.44)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.839)
	tracef.write(f"2557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2557kbit")
	time.sleep(0.234)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.495)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.166)
	tracef.write(f"2460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2460kbit")
	time.sleep(0.943)
	tracef.write(f"2474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2474kbit")
	time.sleep(0.208)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.32)
	tracef.write(f"2476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2476kbit")
	time.sleep(0.402)
	tracef.write(f"2518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2518kbit")
	time.sleep(0.469)
	tracef.write(f"2462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2462kbit")
	time.sleep(0.61)
	tracef.write(f"2550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2550kbit")
	time.sleep(0.211)
	tracef.write(f"2486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2486kbit")
	time.sleep(0.371)
	tracef.write(f"2519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2519kbit")
	time.sleep(0.243)
	tracef.write(f"2502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2502kbit")
	time.sleep(0.604)
	tracef.write(f"2541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2541kbit")
	time.sleep(0.91)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.611)
	tracef.write(f"2567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2567kbit")
	time.sleep(0.185)
	tracef.write(f"2554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2554kbit")
	time.sleep(0.15)
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2525kbit")
	time.sleep(0.789)
	tracef.write(f"2514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2514kbit")
	time.sleep(0.672)
	tracef.write(f"2507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2507kbit")
	time.sleep(0.859)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.869)
	tracef.write(f"2501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2501kbit")
	time.sleep(0.289)
	tracef.write(f"2500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2500kbit")
	time.sleep(0.648)
	tracef.write(f"2472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2472kbit")
	time.sleep(0.274)
	tracef.write(f"2473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2473kbit")
	time.sleep(0.14)
	tracef.write(f"2548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2548kbit")
	time.sleep(0.952)
	tracef.write(f"2544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2544kbit")
	time.sleep(0.822)
	tracef.write(f"2480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2480kbit")
	time.sleep(0.713)
	tracef.write(f"2512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2512kbit")
	time.sleep(0.524)
	tracef.write(f"2560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2560kbit")
	time.sleep(0.315)
	tracef.write(f"2548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2548kbit")
	time.sleep(0.362)
	tracef.write(f"2557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2557kbit")
	time.sleep(0.91)
	tracef.write(f"2507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2507kbit")
	time.sleep(0.138)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.88)
	tracef.write(f"2463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2463kbit")
	time.sleep(0.688)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.24)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.644)
	tracef.write(f"2471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2471kbit")
	time.sleep(0.23)
	tracef.write(f"2483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2483kbit")
	time.sleep(0.577)
	tracef.write(f"2481 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2481kbit")
	time.sleep(0.459)
	tracef.write(f"2547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2547kbit")
	time.sleep(0.612)
	tracef.write(f"2525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2525kbit")
	time.sleep(0.63)
	tracef.write(f"2479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2479kbit")
	time.sleep(0.911)
	tracef.write(f"2476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2476kbit")
	time.sleep(0.819)
	tracef.write(f"2524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2524kbit")
	time.sleep(0.401)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.589)
	tracef.write(f"2545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2545kbit")
	time.sleep(0.143)
	tracef.write(f"2495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2495kbit")
	time.sleep(0.305)
	tracef.write(f"2558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2558kbit")
	time.sleep(0.666)
	tracef.write(f"2520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2520kbit")
	time.sleep(0.438)
	tracef.write(f"2475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2475kbit")
	time.sleep(0.664)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.578)
	tracef.write(f"2555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2555kbit")
	time.sleep(0.426)
	tracef.write(f"2540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2540kbit")
	time.sleep(0.51)
	tracef.write(f"2497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2497kbit")
	time.sleep(0.459)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.455)
	tracef.write(f"2566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2566kbit")
	time.sleep(0.909)
	tracef.write(f"2486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2486kbit")
	time.sleep(0.641)
	tracef.write(f"2522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2522kbit")
	time.sleep(0.85)
	tracef.write(f"2567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2567kbit")
	time.sleep(0.369)
	tracef.write(f"2522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2522kbit")
	time.sleep(0.311)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.246)
	tracef.write(f"2476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2476kbit")
	time.sleep(0.923)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.23)
	tracef.write(f"2490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2490kbit")
	time.sleep(0.769)
	tracef.write(f"2538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2538kbit")
	time.sleep(0.398)
	tracef.write(f"2488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2488kbit")
	time.sleep(0.609)
	tracef.write(f"2489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2489kbit")
	time.sleep(0.936)
	tracef.write(f"2523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2523kbit")
	time.sleep(0.351)
	tracef.write(f"2477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2477kbit")
	time.sleep(0.459)
	tracef.write(f"2465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2465kbit")
	time.sleep(0.911)
	tracef.write(f"2460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2460kbit")
	time.sleep(0.797)
	tracef.write(f"2491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2491kbit")
	time.sleep(0.286)
	tracef.write(f"2496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2496kbit")
	time.sleep(0.77)
	tracef.write(f"2487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2487kbit")
	time.sleep(0.54)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.256)
	tracef.write(f"2455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2455kbit")
	time.sleep(0.229)
	tracef.write(f"2487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2487kbit")
	time.sleep(0.175)
	tracef.write(f"2515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2515kbit")
	time.sleep(0.204)
	tracef.write(f"2498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2498kbit")
	time.sleep(0.795)
	tracef.write(f"2498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2498kbit")
	time.sleep(0.153)
	tracef.write(f"2463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2463kbit")
	time.sleep(0.136)
	tracef.write(f"2491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2491kbit")
	time.sleep(0.249)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.39)
	tracef.write(f"2531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2531kbit")
	time.sleep(0.822)
	tracef.write(f"2540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2540kbit")
	time.sleep(0.5)
	tracef.write(f"2517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2517kbit")
	time.sleep(0.515)
	tracef.write(f"2505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2505kbit")
	time.sleep(0.721)
	tracef.write(f"2503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2503kbit")
	time.sleep(0.725)
	tracef.write(f"2496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2496kbit")
	time.sleep(0.871)
	tracef.write(f"2559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2559kbit")
	time.sleep(0.16)
	tracef.write(f"2479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2479kbit")
	time.sleep(0.626)
	tracef.write(f"2527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2527kbit")
	time.sleep(0.809)
	tracef.write(f"2541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2541kbit")
	time.sleep(0.951)
	tracef.write(f"2459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2459kbit")
	time.sleep(0.314)
	tracef.write(f"2466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2466kbit")
	time.sleep(0.477)
	tracef.write(f"2522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2522kbit")
	time.sleep(0.515)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.538)
	tracef.write(f"2558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2558kbit")
	time.sleep(0.826)
	tracef.write(f"2549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2549kbit")
	time.sleep(0.602)
	tracef.write(f"2521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2521kbit")
	time.sleep(0.596)
	tracef.write(f"2526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2526kbit")
	time.sleep(0.556)
	tracef.write(f"2533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2533kbit")
	time.sleep(0.299)
	tracef.write(f"2520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2520kbit")
	time.sleep(0.355)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()