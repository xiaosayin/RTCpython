#t:72-691 ; rate:211-2575 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace284.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace284.txt", 'a+')
	tracef.write(f"1095 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1095kbit")
	time.sleep(0.425)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(0.579)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(0.173)
	tracef.write(f"1701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1701kbit")
	time.sleep(0.652)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(0.502)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(0.301)
	tracef.write(f"370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 370kbit")
	time.sleep(0.468)
	tracef.write(f"2005 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2005kbit")
	time.sleep(0.669)
	tracef.write(f"650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 650kbit")
	time.sleep(0.686)
	tracef.write(f"1836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1836kbit")
	time.sleep(0.575)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(0.536)
	tracef.write(f"2132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2132kbit")
	time.sleep(0.683)
	tracef.write(f"1807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1807kbit")
	time.sleep(0.46)
	tracef.write(f"2005 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2005kbit")
	time.sleep(0.617)
	tracef.write(f"1657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1657kbit")
	time.sleep(0.151)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.64)
	tracef.write(f"1067 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1067kbit")
	time.sleep(0.613)
	tracef.write(f"643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 643kbit")
	time.sleep(0.585)
	tracef.write(f"768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 768kbit")
	time.sleep(0.484)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(0.367)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.59)
	tracef.write(f"1011 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1011kbit")
	time.sleep(0.635)
	tracef.write(f"1889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1889kbit")
	time.sleep(0.095)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(0.395)
	tracef.write(f"1577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1577kbit")
	time.sleep(0.369)
	tracef.write(f"575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 575kbit")
	time.sleep(0.147)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(0.535)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.15)
	tracef.write(f"1744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1744kbit")
	time.sleep(0.512)
	tracef.write(f"1857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1857kbit")
	time.sleep(0.658)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(0.416)
	tracef.write(f"1268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1268kbit")
	time.sleep(0.622)
	tracef.write(f"725 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 725kbit")
	time.sleep(0.357)
	tracef.write(f"1001 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1001kbit")
	time.sleep(0.682)
	tracef.write(f"2145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2145kbit")
	time.sleep(0.669)
	tracef.write(f"2521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2521kbit")
	time.sleep(0.664)
	tracef.write(f"1792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1792kbit")
	time.sleep(0.15)
	tracef.write(f"412 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 412kbit")
	time.sleep(0.263)
	tracef.write(f"2543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2543kbit")
	time.sleep(0.346)
	tracef.write(f"1841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1841kbit")
	time.sleep(0.656)
	tracef.write(f"463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 463kbit")
	time.sleep(0.127)
	tracef.write(f"2186 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2186kbit")
	time.sleep(0.333)
	tracef.write(f"523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 523kbit")
	time.sleep(0.348)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.432)
	tracef.write(f"1506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1506kbit")
	time.sleep(0.542)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(0.232)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.513)
	tracef.write(f"1698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1698kbit")
	time.sleep(0.412)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.627)
	tracef.write(f"1806 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1806kbit")
	time.sleep(0.655)
	tracef.write(f"485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 485kbit")
	time.sleep(0.448)
	tracef.write(f"1158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1158kbit")
	time.sleep(0.534)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.525)
	tracef.write(f"848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 848kbit")
	time.sleep(0.277)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.267)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(0.41)
	tracef.write(f"979 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 979kbit")
	time.sleep(0.42)
	tracef.write(f"1512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1512kbit")
	time.sleep(0.214)
	tracef.write(f"1080 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1080kbit")
	time.sleep(0.332)
	tracef.write(f"2416 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2416kbit")
	time.sleep(0.526)
	tracef.write(f"1832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1832kbit")
	time.sleep(0.405)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.117)
	tracef.write(f"2392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2392kbit")
	time.sleep(0.388)
	tracef.write(f"620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 620kbit")
	time.sleep(0.66)
	tracef.write(f"676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 676kbit")
	time.sleep(0.325)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(0.444)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(0.109)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.215)
	tracef.write(f"829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 829kbit")
	time.sleep(0.213)
	tracef.write(f"600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 600kbit")
	time.sleep(0.537)
	tracef.write(f"2346 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2346kbit")
	time.sleep(0.258)
	tracef.write(f"2449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2449kbit")
	time.sleep(0.27)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.288)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(0.484)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(0.558)
	tracef.write(f"1366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1366kbit")
	time.sleep(0.171)
	tracef.write(f"633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 633kbit")
	time.sleep(0.24)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(0.328)
	tracef.write(f"926 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 926kbit")
	time.sleep(0.653)
	tracef.write(f"2200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2200kbit")
	time.sleep(0.512)
	tracef.write(f"1724 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1724kbit")
	time.sleep(0.31)
	tracef.write(f"1813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1813kbit")
	time.sleep(0.425)
	tracef.write(f"2158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2158kbit")
	time.sleep(0.577)
	tracef.write(f"2573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2573kbit")
	time.sleep(0.57)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.125)
	tracef.write(f"453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 453kbit")
	time.sleep(0.56)
	tracef.write(f"2263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2263kbit")
	time.sleep(0.481)
	tracef.write(f"557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 557kbit")
	time.sleep(0.637)
	tracef.write(f"2250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2250kbit")
	time.sleep(0.674)
	tracef.write(f"1551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1551kbit")
	time.sleep(0.496)
	tracef.write(f"669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 669kbit")
	time.sleep(0.424)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(0.262)
	tracef.write(f"1071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1071kbit")
	time.sleep(0.672)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(0.576)
	tracef.write(f"2361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2361kbit")
	time.sleep(0.154)
	tracef.write(f"1734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1734kbit")
	time.sleep(0.259)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(0.541)
	tracef.write(f"2019 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2019kbit")
	time.sleep(0.68)
	tracef.write(f"1704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1704kbit")
	time.sleep(0.155)
	tracef.write(f"1228 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1228kbit")
	time.sleep(0.452)
	tracef.write(f"882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 882kbit")
	time.sleep(0.511)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.627)
	tracef.write(f"1401 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1401kbit")
	time.sleep(0.541)
	tracef.write(f"1223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1223kbit")
	time.sleep(0.663)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(0.368)
	tracef.write(f"337 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 337kbit")
	time.sleep(0.119)
	tracef.write(f"596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 596kbit")
	time.sleep(0.248)
	tracef.write(f"1667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1667kbit")
	time.sleep(0.495)
	tracef.write(f"633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 633kbit")
	time.sleep(0.583)
	tracef.write(f"1788 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1788kbit")
	time.sleep(0.641)
	tracef.write(f"1378 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1378kbit")
	time.sleep(0.601)
	tracef.write(f"1772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1772kbit")
	time.sleep(0.53)
	tracef.write(f"625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 625kbit")
	time.sleep(0.526)
	tracef.write(f"2402 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2402kbit")
	time.sleep(0.458)
	tracef.write(f"842 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 842kbit")
	time.sleep(0.641)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.114)
	tracef.write(f"1851 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1851kbit")
	time.sleep(0.282)
	tracef.write(f"787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 787kbit")
	time.sleep(0.131)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(0.191)
	tracef.write(f"2457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2457kbit")
	time.sleep(0.529)
	tracef.write(f"908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 908kbit")
	time.sleep(0.401)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.641)
	tracef.write(f"2486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2486kbit")
	time.sleep(0.538)
	tracef.write(f"1786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1786kbit")
	time.sleep(0.345)
	tracef.write(f"2468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2468kbit")
	time.sleep(0.215)
	tracef.write(f"819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 819kbit")
	time.sleep(0.267)
	tracef.write(f"2563 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2563kbit")
	time.sleep(0.517)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.384)
	tracef.write(f"732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 732kbit")
	time.sleep(0.539)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(0.192)
	tracef.write(f"512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 512kbit")
	time.sleep(0.205)
	tracef.write(f"1860 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1860kbit")
	time.sleep(0.57)
	tracef.write(f"716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 716kbit")
	time.sleep(0.293)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(0.337)
	tracef.write(f"1127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1127kbit")
	time.sleep(0.287)
	tracef.write(f"581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 581kbit")
	time.sleep(0.605)
	tracef.write(f"596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 596kbit")
	time.sleep(0.283)
	tracef.write(f"1722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1722kbit")
	time.sleep(0.257)
	tracef.write(f"961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 961kbit")
	time.sleep(0.3)
	tracef.write(f"560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 560kbit")
	time.sleep(0.669)
	tracef.write(f"609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 609kbit")
	time.sleep(0.234)
	tracef.write(f"2201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2201kbit")
	time.sleep(0.138)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(0.274)
	tracef.write(f"796 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 796kbit")
	time.sleep(0.271)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(0.363)
	tracef.write(f"496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 496kbit")
	time.sleep(0.643)
	tracef.write(f"1403 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1403kbit")
	time.sleep(0.573)
	tracef.write(f"1310 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1310kbit")
	time.sleep(0.463)
	tracef.write(f"858 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 858kbit")
	time.sleep(0.391)
	tracef.write(f"1699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1699kbit")
	time.sleep(0.181)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(0.257)
	tracef.write(f"379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 379kbit")
	time.sleep(0.265)
	tracef.write(f"2307 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2307kbit")
	time.sleep(0.629)
	tracef.write(f"415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 415kbit")
	time.sleep(0.38)
	tracef.write(f"730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 730kbit")
	time.sleep(0.254)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.17)
	tracef.write(f"314 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 314kbit")
	time.sleep(0.384)
	tracef.write(f"794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 794kbit")
	time.sleep(0.614)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(0.179)
	tracef.write(f"755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 755kbit")
	time.sleep(0.617)
	tracef.write(f"2566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2566kbit")
	time.sleep(0.566)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.645)
	tracef.write(f"870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 870kbit")
	time.sleep(0.368)
	tracef.write(f"524 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 524kbit")
	time.sleep(0.307)
	tracef.write(f"1958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1958kbit")
	time.sleep(0.181)
	tracef.write(f"380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 380kbit")
	time.sleep(0.46)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.496)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(0.372)
	tracef.write(f"1885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1885kbit")
	time.sleep(0.49)
	tracef.write(f"333 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 333kbit")
	time.sleep(0.591)
	tracef.write(f"2203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2203kbit")
	time.sleep(0.512)
	tracef.write(f"2370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2370kbit")
	time.sleep(0.432)
	tracef.write(f"1718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1718kbit")
	time.sleep(0.279)
	tracef.write(f"878 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 878kbit")
	time.sleep(0.622)
	tracef.write(f"2121 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2121kbit")
	time.sleep(0.415)
	tracef.write(f"755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 755kbit")
	time.sleep(0.534)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.133)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(0.548)
	tracef.write(f"2220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2220kbit")
	time.sleep(0.403)
	tracef.write(f"601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 601kbit")
	time.sleep(0.303)
	tracef.write(f"1329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1329kbit")
	time.sleep(0.54)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.28)
	tracef.write(f"2190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2190kbit")
	time.sleep(0.455)
	tracef.write(f"2461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2461kbit")
	time.sleep(0.356)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.397)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.515)
	tracef.write(f"432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 432kbit")
	time.sleep(0.448)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(0.335)
	tracef.write(f"1884 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1884kbit")
	time.sleep(0.4)
	tracef.write(f"1988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1988kbit")
	time.sleep(0.158)
	tracef.write(f"227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 227kbit")
	time.sleep(0.324)
	tracef.write(f"2564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2564kbit")
	time.sleep(0.266)
	tracef.write(f"454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 454kbit")
	time.sleep(0.552)
	tracef.write(f"560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 560kbit")
	time.sleep(0.147)
	tracef.write(f"476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 476kbit")
	time.sleep(0.527)
	tracef.write(f"1552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1552kbit")
	time.sleep(0.287)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.243)
	tracef.write(f"472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 472kbit")
	time.sleep(0.645)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(0.396)
	tracef.write(f"656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 656kbit")
	time.sleep(0.201)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(0.384)
	tracef.write(f"530 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 530kbit")
	time.sleep(0.288)
	tracef.write(f"2116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2116kbit")
	time.sleep(0.135)
	tracef.write(f"1165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1165kbit")
	time.sleep(0.206)
	tracef.write(f"2526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2526kbit")
	time.sleep(0.562)
	tracef.write(f"2504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2504kbit")
	time.sleep(0.16)
	tracef.write(f"2509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2509kbit")
	time.sleep(0.257)
	tracef.write(f"2214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2214kbit")
	time.sleep(0.382)
	tracef.write(f"1301 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1301kbit")
	time.sleep(0.643)
	tracef.write(f"699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 699kbit")
	time.sleep(0.486)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.448)
	tracef.write(f"1506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1506kbit")
	time.sleep(0.404)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(0.238)
	tracef.write(f"2040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2040kbit")
	time.sleep(0.381)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(0.68)
	tracef.write(f"2368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2368kbit")
	time.sleep(0.301)
	tracef.write(f"2330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2330kbit")
	time.sleep(0.441)
	tracef.write(f"2251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2251kbit")
	time.sleep(0.579)
	tracef.write(f"1151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1151kbit")
	time.sleep(0.383)
	tracef.write(f"2379 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2379kbit")
	time.sleep(0.625)
	tracef.write(f"1965 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1965kbit")
	time.sleep(0.268)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(0.683)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.511)
	tracef.write(f"1861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1861kbit")
	time.sleep(0.192)
	tracef.write(f"2256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2256kbit")
	time.sleep(0.299)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(0.187)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.434)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.352)
	tracef.write(f"658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 658kbit")
	time.sleep(0.422)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.513)
	tracef.write(f"2388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2388kbit")
	time.sleep(0.634)
	tracef.write(f"436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 436kbit")
	time.sleep(0.494)
	tracef.write(f"1579 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1579kbit")
	time.sleep(0.519)
	tracef.write(f"1597 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1597kbit")
	time.sleep(0.554)
	tracef.write(f"695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 695kbit")
	time.sleep(0.565)
	tracef.write(f"972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 972kbit")
	time.sleep(0.093)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(0.249)
	tracef.write(f"780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 780kbit")
	time.sleep(0.361)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.563)
	tracef.write(f"1262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1262kbit")
	time.sleep(0.112)
	tracef.write(f"1405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1405kbit")
	time.sleep(0.335)
	tracef.write(f"458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 458kbit")
	time.sleep(0.248)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()