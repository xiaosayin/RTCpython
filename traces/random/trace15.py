#t:236-922 ; rate:805-1423 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace15.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace15.txt", 'a+')
	tracef.write(f"985 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 985kbit")
	time.sleep(0.596)
	tracef.write(f"1025 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1025kbit")
	time.sleep(0.41)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(0.336)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(0.324)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(0.887)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.551)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(0.704)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(0.683)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.656)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(0.308)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.459)
	tracef.write(f"1103 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1103kbit")
	time.sleep(0.495)
	tracef.write(f"1090 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1090kbit")
	time.sleep(0.696)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(0.8)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.854)
	tracef.write(f"1334 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1334kbit")
	time.sleep(0.438)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(0.416)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(0.678)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(0.273)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(0.291)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(0.517)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(0.702)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(0.492)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(0.654)
	tracef.write(f"899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 899kbit")
	time.sleep(0.616)
	tracef.write(f"1152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1152kbit")
	time.sleep(0.919)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.748)
	tracef.write(f"1002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1002kbit")
	time.sleep(0.755)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(0.784)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.698)
	tracef.write(f"893 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 893kbit")
	time.sleep(0.783)
	tracef.write(f"886 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 886kbit")
	time.sleep(0.355)
	tracef.write(f"987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 987kbit")
	time.sleep(0.774)
	tracef.write(f"820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 820kbit")
	time.sleep(0.61)
	tracef.write(f"844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 844kbit")
	time.sleep(0.491)
	tracef.write(f"1152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1152kbit")
	time.sleep(0.667)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(0.87)
	tracef.write(f"1000 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1000kbit")
	time.sleep(0.572)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.656)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(0.91)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(0.596)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(0.473)
	tracef.write(f"823 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 823kbit")
	time.sleep(0.776)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(0.434)
	tracef.write(f"929 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 929kbit")
	time.sleep(0.41)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.479)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.387)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(0.866)
	tracef.write(f"1194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1194kbit")
	time.sleep(0.423)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(0.699)
	tracef.write(f"855 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 855kbit")
	time.sleep(0.82)
	tracef.write(f"1002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1002kbit")
	time.sleep(0.785)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(0.304)
	tracef.write(f"1141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1141kbit")
	time.sleep(0.309)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(0.534)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.375)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.385)
	tracef.write(f"1405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1405kbit")
	time.sleep(0.415)
	tracef.write(f"1067 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1067kbit")
	time.sleep(0.746)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(0.726)
	tracef.write(f"1179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1179kbit")
	time.sleep(0.637)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(0.439)
	tracef.write(f"1000 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1000kbit")
	time.sleep(0.784)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(0.488)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(0.337)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(0.85)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(0.534)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(0.773)
	tracef.write(f"848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 848kbit")
	time.sleep(0.392)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.834)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(0.778)
	tracef.write(f"986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 986kbit")
	time.sleep(0.663)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.562)
	tracef.write(f"914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 914kbit")
	time.sleep(0.608)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.787)
	tracef.write(f"1135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1135kbit")
	time.sleep(0.656)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(0.551)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(0.755)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(0.596)
	tracef.write(f"1387 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1387kbit")
	time.sleep(0.385)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.558)
	tracef.write(f"1080 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1080kbit")
	time.sleep(0.368)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(0.876)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(0.531)
	tracef.write(f"1152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1152kbit")
	time.sleep(0.652)
	tracef.write(f"1169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1169kbit")
	time.sleep(0.754)
	tracef.write(f"993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 993kbit")
	time.sleep(0.478)
	tracef.write(f"1040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1040kbit")
	time.sleep(0.785)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.456)
	tracef.write(f"813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 813kbit")
	time.sleep(0.872)
	tracef.write(f"1301 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1301kbit")
	time.sleep(0.589)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(0.604)
	tracef.write(f"1145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1145kbit")
	time.sleep(0.692)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(0.854)
	tracef.write(f"990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 990kbit")
	time.sleep(0.875)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.534)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(0.272)
	tracef.write(f"1054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1054kbit")
	time.sleep(0.6)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.374)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(0.813)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.383)
	tracef.write(f"1177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1177kbit")
	time.sleep(0.42)
	tracef.write(f"1163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1163kbit")
	time.sleep(0.401)
	tracef.write(f"817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 817kbit")
	time.sleep(0.343)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.715)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(0.265)
	tracef.write(f"861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 861kbit")
	time.sleep(0.879)
	tracef.write(f"1267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1267kbit")
	time.sleep(0.49)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(0.762)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(0.847)
	tracef.write(f"882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 882kbit")
	time.sleep(0.552)
	tracef.write(f"914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 914kbit")
	time.sleep(0.633)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(0.853)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(0.525)
	tracef.write(f"848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 848kbit")
	time.sleep(0.753)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(0.528)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.279)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(0.731)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.411)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(0.595)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(0.818)
	tracef.write(f"1175 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1175kbit")
	time.sleep(0.672)
	tracef.write(f"815 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 815kbit")
	time.sleep(0.508)
	tracef.write(f"1375 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1375kbit")
	time.sleep(0.269)
	tracef.write(f"1026 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1026kbit")
	time.sleep(0.404)
	tracef.write(f"844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 844kbit")
	time.sleep(0.311)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.881)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(0.71)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(0.32)
	tracef.write(f"1010 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1010kbit")
	time.sleep(0.483)
	tracef.write(f"861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 861kbit")
	time.sleep(0.286)
	tracef.write(f"1406 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1406kbit")
	time.sleep(0.416)
	tracef.write(f"973 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 973kbit")
	time.sleep(0.706)
	tracef.write(f"1174 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1174kbit")
	time.sleep(0.646)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(0.328)
	tracef.write(f"847 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 847kbit")
	time.sleep(0.649)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(0.683)
	tracef.write(f"1237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1237kbit")
	time.sleep(0.694)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.488)
	tracef.write(f"1293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1293kbit")
	time.sleep(0.836)
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1164kbit")
	time.sleep(0.304)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.438)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.276)
	tracef.write(f"1309 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1309kbit")
	time.sleep(0.294)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(0.728)
	tracef.write(f"1153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1153kbit")
	time.sleep(0.36)
	tracef.write(f"962 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 962kbit")
	time.sleep(0.799)
	tracef.write(f"1371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1371kbit")
	time.sleep(0.92)
	tracef.write(f"1018 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1018kbit")
	time.sleep(0.766)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.467)
	tracef.write(f"810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 810kbit")
	time.sleep(0.605)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.506)
	tracef.write(f"1031 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1031kbit")
	time.sleep(0.279)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(0.296)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(0.57)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.347)
	tracef.write(f"866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 866kbit")
	time.sleep(0.721)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.502)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(0.858)
	tracef.write(f"1382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1382kbit")
	time.sleep(0.244)
	tracef.write(f"885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 885kbit")
	time.sleep(0.416)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.314)
	tracef.write(f"902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 902kbit")
	time.sleep(0.778)
	tracef.write(f"899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 899kbit")
	time.sleep(0.866)
	tracef.write(f"1040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1040kbit")
	time.sleep(0.508)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.35)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(0.818)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.613)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(0.662)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(0.502)
	tracef.write(f"1275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1275kbit")
	time.sleep(0.92)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(0.497)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()