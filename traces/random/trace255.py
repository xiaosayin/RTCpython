#t:680-804 ; rate:396-1929 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace255.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace255.txt", 'a+')
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 451kbit")
	time.sleep(0.69)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(0.755)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.684)
	tracef.write(f"606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 606kbit")
	time.sleep(0.741)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(0.79)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.744)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(0.765)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.726)
	tracef.write(f"674 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 674kbit")
	time.sleep(0.716)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.759)
	tracef.write(f"1844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1844kbit")
	time.sleep(0.724)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(0.68)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.79)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(0.684)
	tracef.write(f"426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 426kbit")
	time.sleep(0.752)
	tracef.write(f"566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 566kbit")
	time.sleep(0.804)
	tracef.write(f"466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 466kbit")
	time.sleep(0.761)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(0.744)
	tracef.write(f"451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 451kbit")
	time.sleep(0.786)
	tracef.write(f"404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 404kbit")
	time.sleep(0.69)
	tracef.write(f"1725 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1725kbit")
	time.sleep(0.692)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(0.758)
	tracef.write(f"989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 989kbit")
	time.sleep(0.727)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(0.743)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(0.741)
	tracef.write(f"1670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1670kbit")
	time.sleep(0.785)
	tracef.write(f"1411 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1411kbit")
	time.sleep(0.783)
	tracef.write(f"875 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 875kbit")
	time.sleep(0.749)
	tracef.write(f"434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 434kbit")
	time.sleep(0.697)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(0.746)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.797)
	tracef.write(f"632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 632kbit")
	time.sleep(0.746)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(0.79)
	tracef.write(f"738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 738kbit")
	time.sleep(0.715)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.797)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(0.804)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(0.783)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.779)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.709)
	tracef.write(f"817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 817kbit")
	time.sleep(0.683)
	tracef.write(f"1713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1713kbit")
	time.sleep(0.783)
	tracef.write(f"911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 911kbit")
	time.sleep(0.768)
	tracef.write(f"1022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1022kbit")
	time.sleep(0.778)
	tracef.write(f"691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 691kbit")
	time.sleep(0.732)
	tracef.write(f"1846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1846kbit")
	time.sleep(0.699)
	tracef.write(f"787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 787kbit")
	time.sleep(0.784)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(0.685)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(0.735)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(0.797)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.772)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(0.681)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.755)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(0.734)
	tracef.write(f"1220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1220kbit")
	time.sleep(0.765)
	tracef.write(f"428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 428kbit")
	time.sleep(0.709)
	tracef.write(f"1766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1766kbit")
	time.sleep(0.724)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(0.713)
	tracef.write(f"1132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1132kbit")
	time.sleep(0.769)
	tracef.write(f"729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 729kbit")
	time.sleep(0.737)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.689)
	tracef.write(f"973 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 973kbit")
	time.sleep(0.804)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(0.724)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(0.791)
	tracef.write(f"877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 877kbit")
	time.sleep(0.729)
	tracef.write(f"912 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 912kbit")
	time.sleep(0.717)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(0.751)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.74)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.8)
	tracef.write(f"680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 680kbit")
	time.sleep(0.767)
	tracef.write(f"1759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1759kbit")
	time.sleep(0.682)
	tracef.write(f"1883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1883kbit")
	time.sleep(0.74)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(0.781)
	tracef.write(f"1135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1135kbit")
	time.sleep(0.71)
	tracef.write(f"609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 609kbit")
	time.sleep(0.712)
	tracef.write(f"490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 490kbit")
	time.sleep(0.724)
	tracef.write(f"1426 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1426kbit")
	time.sleep(0.725)
	tracef.write(f"701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 701kbit")
	time.sleep(0.704)
	tracef.write(f"442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 442kbit")
	time.sleep(0.692)
	tracef.write(f"1169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1169kbit")
	time.sleep(0.733)
	tracef.write(f"996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 996kbit")
	time.sleep(0.688)
	tracef.write(f"1245 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1245kbit")
	time.sleep(0.724)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.789)
	tracef.write(f"1873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1873kbit")
	time.sleep(0.726)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(0.78)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.791)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.762)
	tracef.write(f"411 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 411kbit")
	time.sleep(0.8)
	tracef.write(f"1659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1659kbit")
	time.sleep(0.713)
	tracef.write(f"1707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1707kbit")
	time.sleep(0.763)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(0.756)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.705)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.73)
	tracef.write(f"1258 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1258kbit")
	time.sleep(0.753)
	tracef.write(f"1840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1840kbit")
	time.sleep(0.686)
	tracef.write(f"1425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1425kbit")
	time.sleep(0.779)
	tracef.write(f"445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 445kbit")
	time.sleep(0.728)
	tracef.write(f"1292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1292kbit")
	time.sleep(0.76)
	tracef.write(f"749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 749kbit")
	time.sleep(0.716)
	tracef.write(f"960 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 960kbit")
	time.sleep(0.7)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(0.75)
	tracef.write(f"1354 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1354kbit")
	time.sleep(0.705)
	tracef.write(f"810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 810kbit")
	time.sleep(0.758)
	tracef.write(f"702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 702kbit")
	time.sleep(0.725)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(0.793)
	tracef.write(f"782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 782kbit")
	time.sleep(0.694)
	tracef.write(f"587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 587kbit")
	time.sleep(0.683)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(0.693)
	tracef.write(f"1682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1682kbit")
	time.sleep(0.731)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.722)
	tracef.write(f"1867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1867kbit")
	time.sleep(0.728)
	tracef.write(f"1405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1405kbit")
	time.sleep(0.774)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(0.686)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(0.786)
	tracef.write(f"1714 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1714kbit")
	time.sleep(0.695)
	tracef.write(f"783 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 783kbit")
	time.sleep(0.68)
	tracef.write(f"514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 514kbit")
	time.sleep(0.749)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.767)
	tracef.write(f"615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 615kbit")
	time.sleep(0.683)
	tracef.write(f"1146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1146kbit")
	time.sleep(0.733)
	tracef.write(f"1654 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1654kbit")
	time.sleep(0.781)
	tracef.write(f"1095 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1095kbit")
	time.sleep(0.759)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.785)
	tracef.write(f"1802 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1802kbit")
	time.sleep(0.762)
	tracef.write(f"1617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1617kbit")
	time.sleep(0.753)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(0.773)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(0.803)
	tracef.write(f"1016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1016kbit")
	time.sleep(0.79)
	tracef.write(f"1714 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1714kbit")
	time.sleep(0.784)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(0.789)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.748)
	tracef.write(f"460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 460kbit")
	time.sleep(0.742)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.798)
	tracef.write(f"1085 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1085kbit")
	time.sleep(0.692)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(0.692)
	tracef.write(f"788 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 788kbit")
	time.sleep(0.734)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()