#t:719-869 ; rate:509-1982 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace220.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace220.txt", 'a+')
	tracef.write(f"598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 598kbit")
	time.sleep(0.748)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(0.798)
	tracef.write(f"1534 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1534kbit")
	time.sleep(0.73)
	tracef.write(f"1972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1972kbit")
	time.sleep(0.745)
	tracef.write(f"1334 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1334kbit")
	time.sleep(0.796)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(0.826)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(0.757)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(0.829)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.868)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.764)
	tracef.write(f"1186 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1186kbit")
	time.sleep(0.739)
	tracef.write(f"1820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1820kbit")
	time.sleep(0.813)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.771)
	tracef.write(f"1063 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1063kbit")
	time.sleep(0.822)
	tracef.write(f"873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 873kbit")
	time.sleep(0.865)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(0.793)
	tracef.write(f"574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 574kbit")
	time.sleep(0.809)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(0.74)
	tracef.write(f"1710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1710kbit")
	time.sleep(0.745)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.749)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(0.755)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.72)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(0.764)
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1164kbit")
	time.sleep(0.821)
	tracef.write(f"808 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 808kbit")
	time.sleep(0.842)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.781)
	tracef.write(f"670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 670kbit")
	time.sleep(0.86)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.868)
	tracef.write(f"1713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1713kbit")
	time.sleep(0.77)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.828)
	tracef.write(f"920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 920kbit")
	time.sleep(0.727)
	tracef.write(f"878 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 878kbit")
	time.sleep(0.829)
	tracef.write(f"1400 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1400kbit")
	time.sleep(0.779)
	tracef.write(f"643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 643kbit")
	time.sleep(0.742)
	tracef.write(f"1703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1703kbit")
	time.sleep(0.839)
	tracef.write(f"1554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1554kbit")
	time.sleep(0.785)
	tracef.write(f"582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 582kbit")
	time.sleep(0.779)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.784)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(0.741)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(0.735)
	tracef.write(f"1318 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1318kbit")
	time.sleep(0.841)
	tracef.write(f"1700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1700kbit")
	time.sleep(0.788)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.842)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(0.803)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(0.863)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(0.746)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(0.724)
	tracef.write(f"626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 626kbit")
	time.sleep(0.767)
	tracef.write(f"1732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1732kbit")
	time.sleep(0.742)
	tracef.write(f"758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 758kbit")
	time.sleep(0.729)
	tracef.write(f"612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 612kbit")
	time.sleep(0.738)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.81)
	tracef.write(f"1153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1153kbit")
	time.sleep(0.858)
	tracef.write(f"702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 702kbit")
	time.sleep(0.866)
	tracef.write(f"1359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1359kbit")
	time.sleep(0.811)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.762)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(0.809)
	tracef.write(f"1578 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1578kbit")
	time.sleep(0.786)
	tracef.write(f"803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 803kbit")
	time.sleep(0.782)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(0.862)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.747)
	tracef.write(f"587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 587kbit")
	time.sleep(0.82)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(0.831)
	tracef.write(f"1293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1293kbit")
	time.sleep(0.832)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(0.723)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.862)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.739)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(0.827)
	tracef.write(f"569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 569kbit")
	time.sleep(0.853)
	tracef.write(f"1008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1008kbit")
	time.sleep(0.816)
	tracef.write(f"1830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1830kbit")
	time.sleep(0.816)
	tracef.write(f"1685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1685kbit")
	time.sleep(0.847)
	tracef.write(f"814 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 814kbit")
	time.sleep(0.731)
	tracef.write(f"1854 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1854kbit")
	time.sleep(0.786)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(0.824)
	tracef.write(f"541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 541kbit")
	time.sleep(0.78)
	tracef.write(f"1857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1857kbit")
	time.sleep(0.815)
	tracef.write(f"986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 986kbit")
	time.sleep(0.804)
	tracef.write(f"960 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 960kbit")
	time.sleep(0.768)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.811)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(0.829)
	tracef.write(f"1934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1934kbit")
	time.sleep(0.798)
	tracef.write(f"628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 628kbit")
	time.sleep(0.725)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(0.736)
	tracef.write(f"1152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1152kbit")
	time.sleep(0.835)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(0.767)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(0.794)
	tracef.write(f"566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 566kbit")
	time.sleep(0.847)
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	time.sleep(0.757)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.748)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.727)
	tracef.write(f"781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 781kbit")
	time.sleep(0.789)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(0.856)
	tracef.write(f"710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 710kbit")
	time.sleep(0.734)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.721)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(0.744)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(0.818)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.83)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(0.842)
	tracef.write(f"964 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 964kbit")
	time.sleep(0.816)
	tracef.write(f"527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 527kbit")
	time.sleep(0.817)
	tracef.write(f"1739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1739kbit")
	time.sleep(0.869)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.753)
	tracef.write(f"663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 663kbit")
	time.sleep(0.828)
	tracef.write(f"1843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1843kbit")
	time.sleep(0.78)
	tracef.write(f"1315 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1315kbit")
	time.sleep(0.721)
	tracef.write(f"572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 572kbit")
	time.sleep(0.75)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(0.769)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.847)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(0.745)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.788)
	tracef.write(f"1757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1757kbit")
	time.sleep(0.822)
	tracef.write(f"975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 975kbit")
	time.sleep(0.759)
	tracef.write(f"1383 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1383kbit")
	time.sleep(0.836)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(0.785)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.816)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(0.868)
	tracef.write(f"1119 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1119kbit")
	time.sleep(0.731)
	tracef.write(f"972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 972kbit")
	time.sleep(0.728)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(0.817)
	tracef.write(f"1952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1952kbit")
	time.sleep(0.722)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.847)
	tracef.write(f"1729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1729kbit")
	time.sleep(0.72)
	tracef.write(f"1025 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1025kbit")
	time.sleep(0.813)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(0.819)
	tracef.write(f"1056 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1056kbit")
	time.sleep(0.76)
	tracef.write(f"981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 981kbit")
	time.sleep(0.824)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()