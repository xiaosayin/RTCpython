#t:383-963 ; rate:499-1435 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace243.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace243.txt", 'a+')
	tracef.write(f"529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 529kbit")
	time.sleep(0.953)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(0.873)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.806)
	tracef.write(f"743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 743kbit")
	time.sleep(0.953)
	tracef.write(f"793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 793kbit")
	time.sleep(0.611)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(0.904)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(0.945)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(0.796)
	tracef.write(f"1333 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1333kbit")
	time.sleep(0.679)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(0.705)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(0.432)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.776)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.731)
	tracef.write(f"514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 514kbit")
	time.sleep(0.665)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(0.924)
	tracef.write(f"1117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1117kbit")
	time.sleep(0.683)
	tracef.write(f"977 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 977kbit")
	time.sleep(0.908)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.581)
	tracef.write(f"1073 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1073kbit")
	time.sleep(0.802)
	tracef.write(f"606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 606kbit")
	time.sleep(0.457)
	tracef.write(f"700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 700kbit")
	time.sleep(0.75)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(0.823)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(0.533)
	tracef.write(f"630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 630kbit")
	time.sleep(0.43)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(0.877)
	tracef.write(f"865 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 865kbit")
	time.sleep(0.896)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.794)
	tracef.write(f"631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 631kbit")
	time.sleep(0.407)
	tracef.write(f"676 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 676kbit")
	time.sleep(0.831)
	tracef.write(f"919 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 919kbit")
	time.sleep(0.426)
	tracef.write(f"957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 957kbit")
	time.sleep(0.864)
	tracef.write(f"913 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 913kbit")
	time.sleep(0.498)
	tracef.write(f"770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 770kbit")
	time.sleep(0.756)
	tracef.write(f"643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 643kbit")
	time.sleep(0.61)
	tracef.write(f"664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 664kbit")
	time.sleep(0.448)
	tracef.write(f"512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 512kbit")
	time.sleep(0.583)
	tracef.write(f"1021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1021kbit")
	time.sleep(0.874)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(0.462)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(0.915)
	tracef.write(f"713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 713kbit")
	time.sleep(0.769)
	tracef.write(f"544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 544kbit")
	time.sleep(0.531)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(0.946)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.948)
	tracef.write(f"548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 548kbit")
	time.sleep(0.478)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(0.836)
	tracef.write(f"518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 518kbit")
	time.sleep(0.661)
	tracef.write(f"1233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1233kbit")
	time.sleep(0.756)
	tracef.write(f"803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 803kbit")
	time.sleep(0.834)
	tracef.write(f"888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 888kbit")
	time.sleep(0.694)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(0.462)
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 841kbit")
	time.sleep(0.739)
	tracef.write(f"661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 661kbit")
	time.sleep(0.932)
	tracef.write(f"638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 638kbit")
	time.sleep(0.619)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(0.536)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.829)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(0.639)
	tracef.write(f"709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 709kbit")
	time.sleep(0.843)
	tracef.write(f"1313 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1313kbit")
	time.sleep(0.52)
	tracef.write(f"1227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1227kbit")
	time.sleep(0.447)
	tracef.write(f"902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 902kbit")
	time.sleep(0.501)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(0.47)
	tracef.write(f"1273 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1273kbit")
	time.sleep(0.482)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(0.506)
	tracef.write(f"1386 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1386kbit")
	time.sleep(0.618)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(0.926)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(0.7)
	tracef.write(f"800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 800kbit")
	time.sleep(0.747)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(0.862)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(0.688)
	tracef.write(f"810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 810kbit")
	time.sleep(0.913)
	tracef.write(f"1012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1012kbit")
	time.sleep(0.794)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(0.57)
	tracef.write(f"1129 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1129kbit")
	time.sleep(0.881)
	tracef.write(f"602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 602kbit")
	time.sleep(0.747)
	tracef.write(f"1308 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1308kbit")
	time.sleep(0.48)
	tracef.write(f"957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 957kbit")
	time.sleep(0.526)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(0.626)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.73)
	tracef.write(f"821 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 821kbit")
	time.sleep(0.864)
	tracef.write(f"634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 634kbit")
	time.sleep(0.6)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.744)
	tracef.write(f"874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 874kbit")
	time.sleep(0.388)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(0.674)
	tracef.write(f"675 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 675kbit")
	time.sleep(0.795)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.902)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(0.55)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(0.705)
	tracef.write(f"784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 784kbit")
	time.sleep(0.808)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(0.753)
	tracef.write(f"624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 624kbit")
	time.sleep(0.452)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(0.626)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(0.822)
	tracef.write(f"506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 506kbit")
	time.sleep(0.819)
	tracef.write(f"575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 575kbit")
	time.sleep(0.903)
	tracef.write(f"1362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1362kbit")
	time.sleep(0.52)
	tracef.write(f"1001 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1001kbit")
	time.sleep(0.777)
	tracef.write(f"584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 584kbit")
	time.sleep(0.67)
	tracef.write(f"765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 765kbit")
	time.sleep(0.923)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(0.616)
	tracef.write(f"850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 850kbit")
	time.sleep(0.882)
	tracef.write(f"809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 809kbit")
	time.sleep(0.603)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(0.499)
	tracef.write(f"658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 658kbit")
	time.sleep(0.615)
	tracef.write(f"523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 523kbit")
	time.sleep(0.885)
	tracef.write(f"1339 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1339kbit")
	time.sleep(0.74)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(0.798)
	tracef.write(f"860 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 860kbit")
	time.sleep(0.553)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(0.664)
	tracef.write(f"717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 717kbit")
	time.sleep(0.704)
	tracef.write(f"1220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1220kbit")
	time.sleep(0.493)
	tracef.write(f"746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 746kbit")
	time.sleep(0.619)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(0.921)
	tracef.write(f"1013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1013kbit")
	time.sleep(0.78)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.905)
	tracef.write(f"1054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1054kbit")
	time.sleep(0.879)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(0.775)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.962)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.722)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(0.458)
	tracef.write(f"1096 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1096kbit")
	time.sleep(0.95)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(0.44)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(0.524)
	tracef.write(f"847 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 847kbit")
	time.sleep(0.621)
	tracef.write(f"1018 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1018kbit")
	time.sleep(0.826)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.763)
	tracef.write(f"614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 614kbit")
	time.sleep(0.837)
	tracef.write(f"1116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1116kbit")
	time.sleep(0.504)
	tracef.write(f"598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 598kbit")
	time.sleep(0.618)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(0.775)
	tracef.write(f"1361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1361kbit")
	time.sleep(0.436)
	tracef.write(f"866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 866kbit")
	time.sleep(0.529)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(0.419)
	tracef.write(f"1294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1294kbit")
	time.sleep(0.913)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.63)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.392)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.864)
	tracef.write(f"1020 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1020kbit")
	time.sleep(0.393)
	tracef.write(f"504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 504kbit")
	time.sleep(0.55)
	tracef.write(f"617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 617kbit")
	time.sleep(0.707)
	tracef.write(f"753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 753kbit")
	time.sleep(0.781)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(0.831)
	tracef.write(f"517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 517kbit")
	time.sleep(0.769)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(0.619)
	tracef.write(f"921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 921kbit")
	time.sleep(0.687)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()