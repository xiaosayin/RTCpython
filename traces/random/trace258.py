#t:744-877 ; rate:432-548 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace258.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace258.txt", 'a+')
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 537kbit")
	time.sleep(0.784)
	tracef.write(f"478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 478kbit")
	time.sleep(0.754)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.861)
	tracef.write(f"448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 448kbit")
	time.sleep(0.762)
	tracef.write(f"440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 440kbit")
	time.sleep(0.767)
	tracef.write(f"505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 505kbit")
	time.sleep(0.846)
	tracef.write(f"468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 468kbit")
	time.sleep(0.79)
	tracef.write(f"440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 440kbit")
	time.sleep(0.824)
	tracef.write(f"485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 485kbit")
	time.sleep(0.842)
	tracef.write(f"434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 434kbit")
	time.sleep(0.841)
	tracef.write(f"507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 507kbit")
	time.sleep(0.831)
	tracef.write(f"533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 533kbit")
	time.sleep(0.765)
	tracef.write(f"469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 469kbit")
	time.sleep(0.806)
	tracef.write(f"479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 479kbit")
	time.sleep(0.877)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.774)
	tracef.write(f"528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 528kbit")
	time.sleep(0.767)
	tracef.write(f"453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 453kbit")
	time.sleep(0.873)
	tracef.write(f"496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 496kbit")
	time.sleep(0.763)
	tracef.write(f"520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 520kbit")
	time.sleep(0.858)
	tracef.write(f"438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 438kbit")
	time.sleep(0.778)
	tracef.write(f"540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 540kbit")
	time.sleep(0.763)
	tracef.write(f"498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 498kbit")
	time.sleep(0.769)
	tracef.write(f"480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 480kbit")
	time.sleep(0.855)
	tracef.write(f"445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 445kbit")
	time.sleep(0.855)
	tracef.write(f"547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 547kbit")
	time.sleep(0.796)
	tracef.write(f"484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 484kbit")
	time.sleep(0.876)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.86)
	tracef.write(f"521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 521kbit")
	time.sleep(0.796)
	tracef.write(f"464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 464kbit")
	time.sleep(0.81)
	tracef.write(f"508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 508kbit")
	time.sleep(0.794)
	tracef.write(f"457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 457kbit")
	time.sleep(0.842)
	tracef.write(f"445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 445kbit")
	time.sleep(0.79)
	tracef.write(f"521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 521kbit")
	time.sleep(0.744)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.832)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.764)
	tracef.write(f"505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 505kbit")
	time.sleep(0.805)
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 451kbit")
	time.sleep(0.798)
	tracef.write(f"517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 517kbit")
	time.sleep(0.773)
	tracef.write(f"445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 445kbit")
	time.sleep(0.751)
	tracef.write(f"444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 444kbit")
	time.sleep(0.803)
	tracef.write(f"515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 515kbit")
	time.sleep(0.764)
	tracef.write(f"518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 518kbit")
	time.sleep(0.83)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.802)
	tracef.write(f"514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 514kbit")
	time.sleep(0.803)
	tracef.write(f"498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 498kbit")
	time.sleep(0.811)
	tracef.write(f"478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 478kbit")
	time.sleep(0.801)
	tracef.write(f"515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 515kbit")
	time.sleep(0.877)
	tracef.write(f"511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 511kbit")
	time.sleep(0.811)
	tracef.write(f"498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 498kbit")
	time.sleep(0.819)
	tracef.write(f"465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 465kbit")
	time.sleep(0.814)
	tracef.write(f"547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 547kbit")
	time.sleep(0.85)
	tracef.write(f"442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 442kbit")
	time.sleep(0.805)
	tracef.write(f"438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 438kbit")
	time.sleep(0.858)
	tracef.write(f"500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 500kbit")
	time.sleep(0.751)
	tracef.write(f"462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 462kbit")
	time.sleep(0.844)
	tracef.write(f"480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 480kbit")
	time.sleep(0.749)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.762)
	tracef.write(f"493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 493kbit")
	time.sleep(0.753)
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 537kbit")
	time.sleep(0.857)
	tracef.write(f"501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 501kbit")
	time.sleep(0.753)
	tracef.write(f"446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 446kbit")
	time.sleep(0.75)
	tracef.write(f"464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 464kbit")
	time.sleep(0.863)
	tracef.write(f"439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 439kbit")
	time.sleep(0.777)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.798)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.811)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.752)
	tracef.write(f"490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 490kbit")
	time.sleep(0.86)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.874)
	tracef.write(f"483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 483kbit")
	time.sleep(0.815)
	tracef.write(f"546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 546kbit")
	time.sleep(0.756)
	tracef.write(f"471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 471kbit")
	time.sleep(0.756)
	tracef.write(f"541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 541kbit")
	time.sleep(0.765)
	tracef.write(f"457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 457kbit")
	time.sleep(0.75)
	tracef.write(f"461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 461kbit")
	time.sleep(0.86)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.785)
	tracef.write(f"525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 525kbit")
	time.sleep(0.864)
	tracef.write(f"527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 527kbit")
	time.sleep(0.788)
	tracef.write(f"532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 532kbit")
	time.sleep(0.867)
	tracef.write(f"450 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 450kbit")
	time.sleep(0.835)
	tracef.write(f"506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 506kbit")
	time.sleep(0.789)
	tracef.write(f"458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 458kbit")
	time.sleep(0.877)
	tracef.write(f"547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 547kbit")
	time.sleep(0.774)
	tracef.write(f"453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 453kbit")
	time.sleep(0.865)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.873)
	tracef.write(f"533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 533kbit")
	time.sleep(0.782)
	tracef.write(f"504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 504kbit")
	time.sleep(0.813)
	tracef.write(f"538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 538kbit")
	time.sleep(0.826)
	tracef.write(f"433 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 433kbit")
	time.sleep(0.861)
	tracef.write(f"452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 452kbit")
	time.sleep(0.771)
	tracef.write(f"452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 452kbit")
	time.sleep(0.858)
	tracef.write(f"524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 524kbit")
	time.sleep(0.767)
	tracef.write(f"547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 547kbit")
	time.sleep(0.867)
	tracef.write(f"473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 473kbit")
	time.sleep(0.779)
	tracef.write(f"521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 521kbit")
	time.sleep(0.845)
	tracef.write(f"443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 443kbit")
	time.sleep(0.749)
	tracef.write(f"464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 464kbit")
	time.sleep(0.813)
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 451kbit")
	time.sleep(0.796)
	tracef.write(f"527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 527kbit")
	time.sleep(0.806)
	tracef.write(f"436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 436kbit")
	time.sleep(0.825)
	tracef.write(f"505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 505kbit")
	time.sleep(0.876)
	tracef.write(f"461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 461kbit")
	time.sleep(0.811)
	tracef.write(f"479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 479kbit")
	time.sleep(0.789)
	tracef.write(f"443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 443kbit")
	time.sleep(0.847)
	tracef.write(f"433 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 433kbit")
	time.sleep(0.783)
	tracef.write(f"535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 535kbit")
	time.sleep(0.771)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.797)
	tracef.write(f"456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 456kbit")
	time.sleep(0.816)
	tracef.write(f"449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 449kbit")
	time.sleep(0.844)
	tracef.write(f"524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 524kbit")
	time.sleep(0.839)
	tracef.write(f"435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 435kbit")
	time.sleep(0.846)
	tracef.write(f"506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 506kbit")
	time.sleep(0.806)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.847)
	tracef.write(f"507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 507kbit")
	time.sleep(0.808)
	tracef.write(f"512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 512kbit")
	time.sleep(0.78)
	tracef.write(f"510 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 510kbit")
	time.sleep(0.811)
	tracef.write(f"484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 484kbit")
	time.sleep(0.871)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.758)
	tracef.write(f"527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 527kbit")
	time.sleep(0.864)
	tracef.write(f"471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 471kbit")
	time.sleep(0.817)
	tracef.write(f"437 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 437kbit")
	time.sleep(0.767)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.865)
	tracef.write(f"499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 499kbit")
	time.sleep(0.776)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.753)
	tracef.write(f"441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 441kbit")
	time.sleep(0.761)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()