#t:117-982 ; rate:238-2878 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace108.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace108.txt", 'a+')
	tracef.write(f"268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 268kbit")
	time.sleep(0.662)
	tracef.write(f"1832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1832kbit")
	time.sleep(0.524)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(0.636)
	tracef.write(f"325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 325kbit")
	time.sleep(0.143)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.641)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(0.688)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(0.442)
	tracef.write(f"650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 650kbit")
	time.sleep(0.948)
	tracef.write(f"1780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1780kbit")
	time.sleep(0.571)
	tracef.write(f"1123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1123kbit")
	time.sleep(0.682)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.817)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.317)
	tracef.write(f"2341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2341kbit")
	time.sleep(0.699)
	tracef.write(f"760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 760kbit")
	time.sleep(0.406)
	tracef.write(f"2719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2719kbit")
	time.sleep(0.67)
	tracef.write(f"2087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2087kbit")
	time.sleep(0.323)
	tracef.write(f"1781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1781kbit")
	time.sleep(0.381)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(0.652)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.492)
	tracef.write(f"2642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2642kbit")
	time.sleep(0.546)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.267)
	tracef.write(f"305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 305kbit")
	time.sleep(0.283)
	tracef.write(f"2214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2214kbit")
	time.sleep(0.297)
	tracef.write(f"1705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1705kbit")
	time.sleep(0.554)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.745)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(0.693)
	tracef.write(f"1676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1676kbit")
	time.sleep(0.128)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(0.541)
	tracef.write(f"309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 309kbit")
	time.sleep(0.258)
	tracef.write(f"2442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2442kbit")
	time.sleep(0.667)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(0.944)
	tracef.write(f"2726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2726kbit")
	time.sleep(0.148)
	tracef.write(f"2374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2374kbit")
	time.sleep(0.84)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(0.563)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.89)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.877)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.545)
	tracef.write(f"573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 573kbit")
	time.sleep(0.626)
	tracef.write(f"1600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1600kbit")
	time.sleep(0.579)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.777)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.926)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(0.759)
	tracef.write(f"1774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1774kbit")
	time.sleep(0.777)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.595)
	tracef.write(f"2045 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2045kbit")
	time.sleep(0.651)
	tracef.write(f"768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 768kbit")
	time.sleep(0.324)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(0.933)
	tracef.write(f"342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 342kbit")
	time.sleep(0.665)
	tracef.write(f"1168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1168kbit")
	time.sleep(0.958)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(0.477)
	tracef.write(f"2352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2352kbit")
	time.sleep(0.123)
	tracef.write(f"1677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1677kbit")
	time.sleep(0.804)
	tracef.write(f"1973 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1973kbit")
	time.sleep(0.288)
	tracef.write(f"318 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 318kbit")
	time.sleep(0.433)
	tracef.write(f"984 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 984kbit")
	time.sleep(0.523)
	tracef.write(f"2181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2181kbit")
	time.sleep(0.139)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(0.708)
	tracef.write(f"762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 762kbit")
	time.sleep(0.903)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(0.893)
	tracef.write(f"2114 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2114kbit")
	time.sleep(0.643)
	tracef.write(f"2650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2650kbit")
	time.sleep(0.361)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.16)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(0.71)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(0.907)
	tracef.write(f"376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 376kbit")
	time.sleep(0.782)
	tracef.write(f"2318 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2318kbit")
	time.sleep(0.439)
	tracef.write(f"801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 801kbit")
	time.sleep(0.538)
	tracef.write(f"2196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2196kbit")
	time.sleep(0.412)
	tracef.write(f"535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 535kbit")
	time.sleep(0.333)
	tracef.write(f"1336 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1336kbit")
	time.sleep(0.15)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.911)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(0.843)
	tracef.write(f"1483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1483kbit")
	time.sleep(0.332)
	tracef.write(f"701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 701kbit")
	time.sleep(0.356)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(0.682)
	tracef.write(f"1493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1493kbit")
	time.sleep(0.819)
	tracef.write(f"1316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1316kbit")
	time.sleep(0.425)
	tracef.write(f"530 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 530kbit")
	time.sleep(0.819)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.524)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.57)
	tracef.write(f"603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 603kbit")
	time.sleep(0.957)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(0.155)
	tracef.write(f"2873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2873kbit")
	time.sleep(0.283)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(0.274)
	tracef.write(f"1907 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1907kbit")
	time.sleep(0.586)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(0.442)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.685)
	tracef.write(f"773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 773kbit")
	time.sleep(0.385)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(0.442)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.293)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.884)
	tracef.write(f"2025 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2025kbit")
	time.sleep(0.951)
	tracef.write(f"1599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1599kbit")
	time.sleep(0.362)
	tracef.write(f"2794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2794kbit")
	time.sleep(0.477)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.332)
	tracef.write(f"407 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 407kbit")
	time.sleep(0.374)
	tracef.write(f"2290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2290kbit")
	time.sleep(0.394)
	tracef.write(f"830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 830kbit")
	time.sleep(0.245)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(0.475)
	tracef.write(f"1240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1240kbit")
	time.sleep(0.909)
	tracef.write(f"2506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2506kbit")
	time.sleep(0.749)
	tracef.write(f"483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 483kbit")
	time.sleep(0.178)
	tracef.write(f"728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 728kbit")
	time.sleep(0.418)
	tracef.write(f"2377 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2377kbit")
	time.sleep(0.352)
	tracef.write(f"2633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2633kbit")
	time.sleep(0.533)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.772)
	tracef.write(f"594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 594kbit")
	time.sleep(0.435)
	tracef.write(f"1964 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1964kbit")
	time.sleep(0.631)
	tracef.write(f"1322 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1322kbit")
	time.sleep(0.808)
	tracef.write(f"2184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2184kbit")
	time.sleep(0.963)
	tracef.write(f"1941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1941kbit")
	time.sleep(0.469)
	tracef.write(f"1890 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1890kbit")
	time.sleep(0.396)
	tracef.write(f"845 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 845kbit")
	time.sleep(0.201)
	tracef.write(f"1978 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1978kbit")
	time.sleep(0.433)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.429)
	tracef.write(f"2093 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2093kbit")
	time.sleep(0.211)
	tracef.write(f"1115 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1115kbit")
	time.sleep(0.947)
	tracef.write(f"884 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 884kbit")
	time.sleep(0.303)
	tracef.write(f"1052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1052kbit")
	time.sleep(0.403)
	tracef.write(f"857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 857kbit")
	time.sleep(0.289)
	tracef.write(f"2140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2140kbit")
	time.sleep(0.715)
	tracef.write(f"382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 382kbit")
	time.sleep(0.624)
	tracef.write(f"2117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2117kbit")
	time.sleep(0.156)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.403)
	tracef.write(f"1937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1937kbit")
	time.sleep(0.251)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.293)
	tracef.write(f"570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 570kbit")
	time.sleep(0.768)
	tracef.write(f"651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 651kbit")
	time.sleep(0.466)
	tracef.write(f"1492 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1492kbit")
	time.sleep(0.691)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(0.339)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(0.483)
	tracef.write(f"1046 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1046kbit")
	time.sleep(0.473)
	tracef.write(f"1770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1770kbit")
	time.sleep(0.886)
	tracef.write(f"2325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2325kbit")
	time.sleep(0.576)
	tracef.write(f"597 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 597kbit")
	time.sleep(0.768)
	tracef.write(f"2702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2702kbit")
	time.sleep(0.313)
	tracef.write(f"2434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2434kbit")
	time.sleep(0.912)
	tracef.write(f"1125 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1125kbit")
	time.sleep(0.497)
	tracef.write(f"2591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2591kbit")
	time.sleep(0.67)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.512)
	tracef.write(f"897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 897kbit")
	time.sleep(0.749)
	tracef.write(f"1365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1365kbit")
	time.sleep(0.212)
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2381kbit")
	time.sleep(0.224)
	tracef.write(f"2416 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2416kbit")
	time.sleep(0.274)
	tracef.write(f"2614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2614kbit")
	time.sleep(0.256)
	tracef.write(f"2811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2811kbit")
	time.sleep(0.495)
	tracef.write(f"1888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1888kbit")
	time.sleep(0.76)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(0.592)
	tracef.write(f"667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 667kbit")
	time.sleep(0.487)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.485)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.707)
	tracef.write(f"1853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1853kbit")
	time.sleep(0.22)
	tracef.write(f"1861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1861kbit")
	time.sleep(0.965)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(0.582)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.915)
	tracef.write(f"1796 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1796kbit")
	time.sleep(0.229)
	tracef.write(f"446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 446kbit")
	time.sleep(0.258)
	tracef.write(f"1783 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1783kbit")
	time.sleep(0.255)
	tracef.write(f"2257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2257kbit")
	time.sleep(0.123)
	tracef.write(f"1115 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1115kbit")
	time.sleep(0.893)
	tracef.write(f"687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 687kbit")
	time.sleep(0.473)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(0.667)
	tracef.write(f"1040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1040kbit")
	time.sleep(0.82)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(0.324)
	tracef.write(f"1376 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1376kbit")
	time.sleep(0.818)
	tracef.write(f"962 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 962kbit")
	time.sleep(0.798)
	tracef.write(f"1867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1867kbit")
	time.sleep(0.687)
	tracef.write(f"807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 807kbit")
	time.sleep(0.408)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.48)
	tracef.write(f"1944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1944kbit")
	time.sleep(0.853)
	tracef.write(f"2681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2681kbit")
	time.sleep(0.524)
	tracef.write(f"1449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1449kbit")
	time.sleep(0.962)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(0.386)
	tracef.write(f"2202 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2202kbit")
	time.sleep(0.517)
	tracef.write(f"2049 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2049kbit")
	time.sleep(0.65)
	tracef.write(f"2570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2570kbit")
	time.sleep(0.252)
	tracef.write(f"2288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2288kbit")
	time.sleep(0.873)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(0.192)
	tracef.write(f"668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 668kbit")
	time.sleep(0.344)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.205)
	tracef.write(f"1837 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1837kbit")
	time.sleep(0.65)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(0.667)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.205)
	tracef.write(f"1238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1238kbit")
	time.sleep(0.128)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.293)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.416)
	tracef.write(f"2800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2800kbit")
	time.sleep(0.786)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()