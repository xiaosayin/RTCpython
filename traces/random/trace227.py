#t:219-855 ; rate:434-678 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace227.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace227.txt", 'a+')
	tracef.write(f"443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 443kbit")
	time.sleep(0.436)
	tracef.write(f"495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 495kbit")
	time.sleep(0.341)
	tracef.write(f"475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 475kbit")
	time.sleep(0.638)
	tracef.write(f"487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 487kbit")
	time.sleep(0.474)
	tracef.write(f"570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 570kbit")
	time.sleep(0.402)
	tracef.write(f"608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 608kbit")
	time.sleep(0.248)
	tracef.write(f"621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 621kbit")
	time.sleep(0.427)
	tracef.write(f"670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 670kbit")
	time.sleep(0.621)
	tracef.write(f"669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 669kbit")
	time.sleep(0.232)
	tracef.write(f"460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 460kbit")
	time.sleep(0.772)
	tracef.write(f"562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 562kbit")
	time.sleep(0.429)
	tracef.write(f"677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 677kbit")
	time.sleep(0.533)
	tracef.write(f"662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 662kbit")
	time.sleep(0.421)
	tracef.write(f"588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 588kbit")
	time.sleep(0.785)
	tracef.write(f"547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 547kbit")
	time.sleep(0.523)
	tracef.write(f"473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 473kbit")
	time.sleep(0.548)
	tracef.write(f"473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 473kbit")
	time.sleep(0.68)
	tracef.write(f"435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 435kbit")
	time.sleep(0.81)
	tracef.write(f"549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 549kbit")
	time.sleep(0.682)
	tracef.write(f"498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 498kbit")
	time.sleep(0.255)
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 451kbit")
	time.sleep(0.324)
	tracef.write(f"616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 616kbit")
	time.sleep(0.337)
	tracef.write(f"543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 543kbit")
	time.sleep(0.703)
	tracef.write(f"488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 488kbit")
	time.sleep(0.39)
	tracef.write(f"520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 520kbit")
	time.sleep(0.605)
	tracef.write(f"645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 645kbit")
	time.sleep(0.748)
	tracef.write(f"502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 502kbit")
	time.sleep(0.224)
	tracef.write(f"638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 638kbit")
	time.sleep(0.801)
	tracef.write(f"549 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 549kbit")
	time.sleep(0.355)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.304)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.741)
	tracef.write(f"434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 434kbit")
	time.sleep(0.297)
	tracef.write(f"670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 670kbit")
	time.sleep(0.358)
	tracef.write(f"444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 444kbit")
	time.sleep(0.517)
	tracef.write(f"618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 618kbit")
	time.sleep(0.387)
	tracef.write(f"556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 556kbit")
	time.sleep(0.516)
	tracef.write(f"624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 624kbit")
	time.sleep(0.615)
	tracef.write(f"461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 461kbit")
	time.sleep(0.652)
	tracef.write(f"602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 602kbit")
	time.sleep(0.74)
	tracef.write(f"661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 661kbit")
	time.sleep(0.577)
	tracef.write(f"577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 577kbit")
	time.sleep(0.419)
	tracef.write(f"677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 677kbit")
	time.sleep(0.818)
	tracef.write(f"626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 626kbit")
	time.sleep(0.824)
	tracef.write(f"633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 633kbit")
	time.sleep(0.489)
	tracef.write(f"492 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 492kbit")
	time.sleep(0.264)
	tracef.write(f"504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 504kbit")
	time.sleep(0.711)
	tracef.write(f"589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 589kbit")
	time.sleep(0.227)
	tracef.write(f"483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 483kbit")
	time.sleep(0.835)
	tracef.write(f"659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 659kbit")
	time.sleep(0.44)
	tracef.write(f"639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 639kbit")
	time.sleep(0.574)
	tracef.write(f"670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 670kbit")
	time.sleep(0.738)
	tracef.write(f"639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 639kbit")
	time.sleep(0.537)
	tracef.write(f"644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 644kbit")
	time.sleep(0.285)
	tracef.write(f"629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 629kbit")
	time.sleep(0.389)
	tracef.write(f"593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 593kbit")
	time.sleep(0.276)
	tracef.write(f"564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 564kbit")
	time.sleep(0.313)
	tracef.write(f"535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 535kbit")
	time.sleep(0.654)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.342)
	tracef.write(f"515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 515kbit")
	time.sleep(0.597)
	tracef.write(f"563 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 563kbit")
	time.sleep(0.259)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.402)
	tracef.write(f"500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 500kbit")
	time.sleep(0.264)
	tracef.write(f"495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 495kbit")
	time.sleep(0.703)
	tracef.write(f"531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 531kbit")
	time.sleep(0.22)
	tracef.write(f"596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 596kbit")
	time.sleep(0.534)
	tracef.write(f"658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 658kbit")
	time.sleep(0.478)
	tracef.write(f"657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 657kbit")
	time.sleep(0.56)
	tracef.write(f"541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 541kbit")
	time.sleep(0.422)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.288)
	tracef.write(f"560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 560kbit")
	time.sleep(0.443)
	tracef.write(f"677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 677kbit")
	time.sleep(0.697)
	tracef.write(f"499 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 499kbit")
	time.sleep(0.694)
	tracef.write(f"586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 586kbit")
	time.sleep(0.345)
	tracef.write(f"532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 532kbit")
	time.sleep(0.734)
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 451kbit")
	time.sleep(0.448)
	tracef.write(f"479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 479kbit")
	time.sleep(0.7)
	tracef.write(f"526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 526kbit")
	time.sleep(0.78)
	tracef.write(f"548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 548kbit")
	time.sleep(0.702)
	tracef.write(f"443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 443kbit")
	time.sleep(0.667)
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 537kbit")
	time.sleep(0.312)
	tracef.write(f"598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 598kbit")
	time.sleep(0.826)
	tracef.write(f"564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 564kbit")
	time.sleep(0.586)
	tracef.write(f"556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 556kbit")
	time.sleep(0.78)
	tracef.write(f"461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 461kbit")
	time.sleep(0.449)
	tracef.write(f"642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 642kbit")
	time.sleep(0.662)
	tracef.write(f"629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 629kbit")
	time.sleep(0.629)
	tracef.write(f"570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 570kbit")
	time.sleep(0.824)
	tracef.write(f"438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 438kbit")
	time.sleep(0.851)
	tracef.write(f"470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 470kbit")
	time.sleep(0.611)
	tracef.write(f"551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 551kbit")
	time.sleep(0.636)
	tracef.write(f"616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 616kbit")
	time.sleep(0.283)
	tracef.write(f"455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 455kbit")
	time.sleep(0.775)
	tracef.write(f"534 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 534kbit")
	time.sleep(0.533)
	tracef.write(f"670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 670kbit")
	time.sleep(0.472)
	tracef.write(f"672 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 672kbit")
	time.sleep(0.314)
	tracef.write(f"492 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 492kbit")
	time.sleep(0.797)
	tracef.write(f"486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 486kbit")
	time.sleep(0.396)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.768)
	tracef.write(f"448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 448kbit")
	time.sleep(0.241)
	tracef.write(f"599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 599kbit")
	time.sleep(0.366)
	tracef.write(f"528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 528kbit")
	time.sleep(0.574)
	tracef.write(f"593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 593kbit")
	time.sleep(0.447)
	tracef.write(f"482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 482kbit")
	time.sleep(0.825)
	tracef.write(f"651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 651kbit")
	time.sleep(0.477)
	tracef.write(f"442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 442kbit")
	time.sleep(0.742)
	tracef.write(f"495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 495kbit")
	time.sleep(0.836)
	tracef.write(f"669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 669kbit")
	time.sleep(0.829)
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 537kbit")
	time.sleep(0.314)
	tracef.write(f"648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 648kbit")
	time.sleep(0.267)
	tracef.write(f"532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 532kbit")
	time.sleep(0.667)
	tracef.write(f"552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 552kbit")
	time.sleep(0.673)
	tracef.write(f"609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 609kbit")
	time.sleep(0.595)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.346)
	tracef.write(f"536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 536kbit")
	time.sleep(0.714)
	tracef.write(f"590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 590kbit")
	time.sleep(0.45)
	tracef.write(f"545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 545kbit")
	time.sleep(0.464)
	tracef.write(f"596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 596kbit")
	time.sleep(0.556)
	tracef.write(f"450 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 450kbit")
	time.sleep(0.393)
	tracef.write(f"484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 484kbit")
	time.sleep(0.466)
	tracef.write(f"446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 446kbit")
	time.sleep(0.347)
	tracef.write(f"557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 557kbit")
	time.sleep(0.847)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.737)
	tracef.write(f"473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 473kbit")
	time.sleep(0.702)
	tracef.write(f"677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 677kbit")
	time.sleep(0.5)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.586)
	tracef.write(f"456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 456kbit")
	time.sleep(0.405)
	tracef.write(f"532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 532kbit")
	time.sleep(0.518)
	tracef.write(f"637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 637kbit")
	time.sleep(0.827)
	tracef.write(f"456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 456kbit")
	time.sleep(0.334)
	tracef.write(f"625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 625kbit")
	time.sleep(0.73)
	tracef.write(f"468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 468kbit")
	time.sleep(0.685)
	tracef.write(f"560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 560kbit")
	time.sleep(0.734)
	tracef.write(f"466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 466kbit")
	time.sleep(0.277)
	tracef.write(f"520 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 520kbit")
	time.sleep(0.715)
	tracef.write(f"653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 653kbit")
	time.sleep(0.798)
	tracef.write(f"528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 528kbit")
	time.sleep(0.611)
	tracef.write(f"647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 647kbit")
	time.sleep(0.725)
	tracef.write(f"647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 647kbit")
	time.sleep(0.825)
	tracef.write(f"650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 650kbit")
	time.sleep(0.446)
	tracef.write(f"612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 612kbit")
	time.sleep(0.288)
	tracef.write(f"516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 516kbit")
	time.sleep(0.818)
	tracef.write(f"582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 582kbit")
	time.sleep(0.673)
	tracef.write(f"618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 618kbit")
	time.sleep(0.618)
	tracef.write(f"482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 482kbit")
	time.sleep(0.654)
	tracef.write(f"598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 598kbit")
	time.sleep(0.447)
	tracef.write(f"463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 463kbit")
	time.sleep(0.507)
	tracef.write(f"519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 519kbit")
	time.sleep(0.537)
	tracef.write(f"545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 545kbit")
	time.sleep(0.514)
	tracef.write(f"657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 657kbit")
	time.sleep(0.455)
	tracef.write(f"617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 617kbit")
	time.sleep(0.433)
	tracef.write(f"592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 592kbit")
	time.sleep(0.551)
	tracef.write(f"533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 533kbit")
	time.sleep(0.788)
	tracef.write(f"662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 662kbit")
	time.sleep(0.834)
	tracef.write(f"494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 494kbit")
	time.sleep(0.35)
	tracef.write(f"664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 664kbit")
	time.sleep(0.302)
	tracef.write(f"517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 517kbit")
	time.sleep(0.851)
	tracef.write(f"495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 495kbit")
	time.sleep(0.651)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.757)
	tracef.write(f"641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 641kbit")
	time.sleep(0.646)
	tracef.write(f"668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 668kbit")
	time.sleep(0.506)
	tracef.write(f"587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 587kbit")
	time.sleep(0.709)
	tracef.write(f"455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 455kbit")
	time.sleep(0.359)
	tracef.write(f"461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 461kbit")
	time.sleep(0.453)
	tracef.write(f"573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 573kbit")
	time.sleep(0.687)
	tracef.write(f"581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 581kbit")
	time.sleep(0.354)
	tracef.write(f"564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 564kbit")
	time.sleep(0.523)
	tracef.write(f"633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 633kbit")
	time.sleep(0.676)
	tracef.write(f"619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 619kbit")
	time.sleep(0.698)
	tracef.write(f"540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 540kbit")
	time.sleep(0.531)
	tracef.write(f"561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 561kbit")
	time.sleep(0.291)
	tracef.write(f"460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 460kbit")
	time.sleep(0.587)
	tracef.write(f"595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 595kbit")
	time.sleep(0.535)
	tracef.write(f"436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 436kbit")
	time.sleep(0.278)
	tracef.write(f"485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 485kbit")
	time.sleep(0.541)
	tracef.write(f"460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 460kbit")
	time.sleep(0.225)
	tracef.write(f"605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 605kbit")
	time.sleep(0.579)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.618)
	tracef.write(f"625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 625kbit")
	time.sleep(0.452)
	tracef.write(f"636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 636kbit")
	time.sleep(0.573)
	tracef.write(f"634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 634kbit")
	time.sleep(0.338)
	tracef.write(f"607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 607kbit")
	time.sleep(0.496)
	tracef.write(f"449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 449kbit")
	time.sleep(0.429)
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 537kbit")
	time.sleep(0.768)
	tracef.write(f"463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 463kbit")
	time.sleep(0.686)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()