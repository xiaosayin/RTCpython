#t:766-823 ; rate:711-1600 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace355.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace355.txt", 'a+')
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 876kbit")
	time.sleep(0.767)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(0.812)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.822)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(0.82)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.804)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(0.8)
	tracef.write(f"1068 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1068kbit")
	time.sleep(0.785)
	tracef.write(f"795 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 795kbit")
	time.sleep(0.773)
	tracef.write(f"757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 757kbit")
	time.sleep(0.811)
	tracef.write(f"996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 996kbit")
	time.sleep(0.817)
	tracef.write(f"776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 776kbit")
	time.sleep(0.789)
	tracef.write(f"978 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 978kbit")
	time.sleep(0.816)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.796)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.795)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(0.776)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(0.805)
	tracef.write(f"1345 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1345kbit")
	time.sleep(0.787)
	tracef.write(f"766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 766kbit")
	time.sleep(0.82)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.767)
	tracef.write(f"885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 885kbit")
	time.sleep(0.801)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(0.798)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(0.785)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(0.786)
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1164kbit")
	time.sleep(0.767)
	tracef.write(f"863 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 863kbit")
	time.sleep(0.782)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.782)
	tracef.write(f"899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 899kbit")
	time.sleep(0.821)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.799)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(0.77)
	tracef.write(f"1046 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1046kbit")
	time.sleep(0.787)
	tracef.write(f"1082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1082kbit")
	time.sleep(0.795)
	tracef.write(f"897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 897kbit")
	time.sleep(0.799)
	tracef.write(f"1309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1309kbit")
	time.sleep(0.821)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(0.816)
	tracef.write(f"717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 717kbit")
	time.sleep(0.816)
	tracef.write(f"716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 716kbit")
	time.sleep(0.796)
	tracef.write(f"902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 902kbit")
	time.sleep(0.779)
	tracef.write(f"1022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1022kbit")
	time.sleep(0.817)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(0.794)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(0.774)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.77)
	tracef.write(f"1045 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1045kbit")
	time.sleep(0.799)
	tracef.write(f"1574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1574kbit")
	time.sleep(0.782)
	tracef.write(f"1114 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1114kbit")
	time.sleep(0.82)
	tracef.write(f"1321 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1321kbit")
	time.sleep(0.766)
	tracef.write(f"1219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1219kbit")
	time.sleep(0.783)
	tracef.write(f"921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 921kbit")
	time.sleep(0.769)
	tracef.write(f"975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 975kbit")
	time.sleep(0.771)
	tracef.write(f"999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 999kbit")
	time.sleep(0.795)
	tracef.write(f"1099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1099kbit")
	time.sleep(0.771)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.821)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(0.793)
	tracef.write(f"1081 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1081kbit")
	time.sleep(0.821)
	tracef.write(f"714 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 714kbit")
	time.sleep(0.81)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.814)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.817)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.803)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.789)
	tracef.write(f"1222 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1222kbit")
	time.sleep(0.775)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(0.795)
	tracef.write(f"1551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1551kbit")
	time.sleep(0.78)
	tracef.write(f"1083 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1083kbit")
	time.sleep(0.79)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(0.801)
	tracef.write(f"1177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1177kbit")
	time.sleep(0.816)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(0.777)
	tracef.write(f"1005 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1005kbit")
	time.sleep(0.772)
	tracef.write(f"1565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1565kbit")
	time.sleep(0.793)
	tracef.write(f"746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 746kbit")
	time.sleep(0.787)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(0.822)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(0.781)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(0.803)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.815)
	tracef.write(f"961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 961kbit")
	time.sleep(0.774)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(0.777)
	tracef.write(f"829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 829kbit")
	time.sleep(0.771)
	tracef.write(f"866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 866kbit")
	time.sleep(0.822)
	tracef.write(f"857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 857kbit")
	time.sleep(0.816)
	tracef.write(f"1127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1127kbit")
	time.sleep(0.809)
	tracef.write(f"1360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1360kbit")
	time.sleep(0.767)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.818)
	tracef.write(f"1001 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1001kbit")
	time.sleep(0.774)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(0.777)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.809)
	tracef.write(f"844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 844kbit")
	time.sleep(0.789)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(0.795)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.777)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.807)
	tracef.write(f"968 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 968kbit")
	time.sleep(0.785)
	tracef.write(f"1162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1162kbit")
	time.sleep(0.798)
	tracef.write(f"1312 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1312kbit")
	time.sleep(0.815)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(0.82)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.798)
	tracef.write(f"981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 981kbit")
	time.sleep(0.771)
	tracef.write(f"973 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 973kbit")
	time.sleep(0.807)
	tracef.write(f"1393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1393kbit")
	time.sleep(0.82)
	tracef.write(f"1115 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1115kbit")
	time.sleep(0.773)
	tracef.write(f"721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 721kbit")
	time.sleep(0.781)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(0.783)
	tracef.write(f"716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 716kbit")
	time.sleep(0.808)
	tracef.write(f"765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 765kbit")
	time.sleep(0.804)
	tracef.write(f"794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 794kbit")
	time.sleep(0.794)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.793)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(0.784)
	tracef.write(f"729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 729kbit")
	time.sleep(0.799)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.795)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(0.819)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(0.803)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.785)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.779)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(0.807)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(0.786)
	tracef.write(f"774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 774kbit")
	time.sleep(0.768)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.793)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(0.805)
	tracef.write(f"727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 727kbit")
	time.sleep(0.819)
	tracef.write(f"1117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1117kbit")
	time.sleep(0.782)
	tracef.write(f"760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 760kbit")
	time.sleep(0.801)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(0.785)
	tracef.write(f"732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 732kbit")
	time.sleep(0.776)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.821)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.798)
	tracef.write(f"1578 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1578kbit")
	time.sleep(0.777)
	tracef.write(f"743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 743kbit")
	time.sleep(0.795)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(0.79)
	tracef.write(f"903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 903kbit")
	time.sleep(0.802)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(0.791)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()