#t:213-969 ; rate:183-2054 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace263.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace263.txt", 'a+')
	tracef.write(f"810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 810kbit")
	time.sleep(0.583)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.544)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(0.824)
	tracef.write(f"462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 462kbit")
	time.sleep(0.907)
	tracef.write(f"1652 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1652kbit")
	time.sleep(0.394)
	tracef.write(f"243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 243kbit")
	time.sleep(0.706)
	tracef.write(f"729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 729kbit")
	time.sleep(0.718)
	tracef.write(f"1727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1727kbit")
	time.sleep(0.26)
	tracef.write(f"1173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1173kbit")
	time.sleep(0.721)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(0.911)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(0.632)
	tracef.write(f"1120 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1120kbit")
	time.sleep(0.228)
	tracef.write(f"682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 682kbit")
	time.sleep(0.502)
	tracef.write(f"2038 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2038kbit")
	time.sleep(0.302)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.564)
	tracef.write(f"428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 428kbit")
	time.sleep(0.728)
	tracef.write(f"1455 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1455kbit")
	time.sleep(0.485)
	tracef.write(f"491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 491kbit")
	time.sleep(0.451)
	tracef.write(f"855 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 855kbit")
	time.sleep(0.49)
	tracef.write(f"1311 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1311kbit")
	time.sleep(0.29)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(0.243)
	tracef.write(f"824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 824kbit")
	time.sleep(0.535)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.783)
	tracef.write(f"1769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1769kbit")
	time.sleep(0.463)
	tracef.write(f"1545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1545kbit")
	time.sleep(0.727)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.493)
	tracef.write(f"735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 735kbit")
	time.sleep(0.55)
	tracef.write(f"449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 449kbit")
	time.sleep(0.401)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.559)
	tracef.write(f"721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 721kbit")
	time.sleep(0.407)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(0.63)
	tracef.write(f"1948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1948kbit")
	time.sleep(0.397)
	tracef.write(f"813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 813kbit")
	time.sleep(0.345)
	tracef.write(f"1517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1517kbit")
	time.sleep(0.795)
	tracef.write(f"1761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1761kbit")
	time.sleep(0.257)
	tracef.write(f"656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 656kbit")
	time.sleep(0.281)
	tracef.write(f"1730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1730kbit")
	time.sleep(0.843)
	tracef.write(f"1694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1694kbit")
	time.sleep(0.7)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.722)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(0.609)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(0.329)
	tracef.write(f"1944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1944kbit")
	time.sleep(0.41)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(0.744)
	tracef.write(f"1194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1194kbit")
	time.sleep(0.769)
	tracef.write(f"321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 321kbit")
	time.sleep(0.246)
	tracef.write(f"773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 773kbit")
	time.sleep(0.738)
	tracef.write(f"204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 204kbit")
	time.sleep(0.595)
	tracef.write(f"883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 883kbit")
	time.sleep(0.408)
	tracef.write(f"1493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1493kbit")
	time.sleep(0.355)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.761)
	tracef.write(f"290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 290kbit")
	time.sleep(0.959)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(0.42)
	tracef.write(f"578 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 578kbit")
	time.sleep(0.418)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(0.656)
	tracef.write(f"697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 697kbit")
	time.sleep(0.875)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(0.733)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(0.232)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.409)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.656)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(0.662)
	tracef.write(f"1435 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1435kbit")
	time.sleep(0.93)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.53)
	tracef.write(f"1335 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1335kbit")
	time.sleep(0.282)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.717)
	tracef.write(f"1354 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1354kbit")
	time.sleep(0.651)
	tracef.write(f"1129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1129kbit")
	time.sleep(0.816)
	tracef.write(f"1009 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1009kbit")
	time.sleep(0.358)
	tracef.write(f"997 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 997kbit")
	time.sleep(0.856)
	tracef.write(f"559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 559kbit")
	time.sleep(0.862)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(0.705)
	tracef.write(f"1787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1787kbit")
	time.sleep(0.859)
	tracef.write(f"486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 486kbit")
	time.sleep(0.759)
	tracef.write(f"1838 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1838kbit")
	time.sleep(0.944)
	tracef.write(f"330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 330kbit")
	time.sleep(0.381)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.682)
	tracef.write(f"206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 206kbit")
	time.sleep(0.744)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.575)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(0.492)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(0.253)
	tracef.write(f"1784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1784kbit")
	time.sleep(0.637)
	tracef.write(f"1981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1981kbit")
	time.sleep(0.968)
	tracef.write(f"1710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1710kbit")
	time.sleep(0.278)
	tracef.write(f"1025 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1025kbit")
	time.sleep(0.478)
	tracef.write(f"671 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 671kbit")
	time.sleep(0.291)
	tracef.write(f"1022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1022kbit")
	time.sleep(0.875)
	tracef.write(f"1378 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1378kbit")
	time.sleep(0.269)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(0.739)
	tracef.write(f"698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 698kbit")
	time.sleep(0.938)
	tracef.write(f"247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 247kbit")
	time.sleep(0.799)
	tracef.write(f"712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 712kbit")
	time.sleep(0.36)
	tracef.write(f"709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 709kbit")
	time.sleep(0.939)
	tracef.write(f"747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 747kbit")
	time.sleep(0.964)
	tracef.write(f"1185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1185kbit")
	time.sleep(0.917)
	tracef.write(f"2046 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2046kbit")
	time.sleep(0.361)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.505)
	tracef.write(f"1422 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1422kbit")
	time.sleep(0.435)
	tracef.write(f"690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 690kbit")
	time.sleep(0.872)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.748)
	tracef.write(f"341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 341kbit")
	time.sleep(0.304)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(0.375)
	tracef.write(f"1823 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1823kbit")
	time.sleep(0.844)
	tracef.write(f"1617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1617kbit")
	time.sleep(0.353)
	tracef.write(f"718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 718kbit")
	time.sleep(0.791)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.594)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.72)
	tracef.write(f"1411 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1411kbit")
	time.sleep(0.616)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(0.335)
	tracef.write(f"890 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 890kbit")
	time.sleep(0.785)
	tracef.write(f"1857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1857kbit")
	time.sleep(0.616)
	tracef.write(f"360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 360kbit")
	time.sleep(0.511)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(0.721)
	tracef.write(f"998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 998kbit")
	time.sleep(0.838)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.619)
	tracef.write(f"1741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1741kbit")
	time.sleep(0.513)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.604)
	tracef.write(f"666 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 666kbit")
	time.sleep(0.587)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(0.678)
	tracef.write(f"487 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 487kbit")
	time.sleep(0.733)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(0.562)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.606)
	tracef.write(f"242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 242kbit")
	time.sleep(0.439)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(0.558)
	tracef.write(f"626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 626kbit")
	time.sleep(0.666)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(0.505)
	tracef.write(f"1665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1665kbit")
	time.sleep(0.689)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.464)
	tracef.write(f"1717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1717kbit")
	time.sleep(0.386)
	tracef.write(f"540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 540kbit")
	time.sleep(0.232)
	tracef.write(f"1661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1661kbit")
	time.sleep(0.805)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.566)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(0.584)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(0.413)
	tracef.write(f"448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 448kbit")
	time.sleep(0.419)
	tracef.write(f"279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 279kbit")
	time.sleep(0.876)
	tracef.write(f"427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 427kbit")
	time.sleep(0.385)
	tracef.write(f"928 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 928kbit")
	time.sleep(0.721)
	tracef.write(f"272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 272kbit")
	time.sleep(0.687)
	tracef.write(f"246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 246kbit")
	time.sleep(0.299)
	tracef.write(f"1620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1620kbit")
	time.sleep(0.796)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.626)
	tracef.write(f"1495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1495kbit")
	time.sleep(0.911)
	tracef.write(f"1157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1157kbit")
	time.sleep(0.549)
	tracef.write(f"1967 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1967kbit")
	time.sleep(0.34)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(0.922)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.82)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(0.96)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(0.272)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(0.529)
	tracef.write(f"1551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1551kbit")
	time.sleep(0.295)
	tracef.write(f"1892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1892kbit")
	time.sleep(0.518)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(0.411)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(0.294)
	tracef.write(f"1654 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1654kbit")
	time.sleep(0.435)
	tracef.write(f"264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 264kbit")
	time.sleep(0.725)
	tracef.write(f"796 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 796kbit")
	time.sleep(0.265)
	tracef.write(f"1983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1983kbit")
	time.sleep(0.663)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.28)
	tracef.write(f"224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 224kbit")
	time.sleep(0.622)
	tracef.write(f"478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 478kbit")
	time.sleep(0.224)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(0.289)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.907)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.96)
	tracef.write(f"767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 767kbit")
	time.sleep(0.963)
	tracef.write(f"808 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 808kbit")
	time.sleep(0.787)
	tracef.write(f"1688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1688kbit")
	time.sleep(0.259)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.852)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(0.3)
	tracef.write(f"669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 669kbit")
	time.sleep(0.484)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(0.837)
	tracef.write(f"752 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 752kbit")
	time.sleep(0.359)
	tracef.write(f"507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 507kbit")
	time.sleep(0.939)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()