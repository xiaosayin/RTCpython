#t:483-828 ; rate:1050-1208 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace39.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace39.txt", 'a+')
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1084kbit")
	time.sleep(0.785)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(0.569)
	tracef.write(f"1131 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1131kbit")
	time.sleep(0.668)
	tracef.write(f"1157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1157kbit")
	time.sleep(0.823)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.811)
	tracef.write(f"1171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1171kbit")
	time.sleep(0.737)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.66)
	tracef.write(f"1121 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1121kbit")
	time.sleep(0.608)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(0.693)
	tracef.write(f"1169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1169kbit")
	time.sleep(0.65)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.78)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.659)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.771)
	tracef.write(f"1081 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1081kbit")
	time.sleep(0.6)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(0.811)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(0.552)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.814)
	tracef.write(f"1193 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1193kbit")
	time.sleep(0.688)
	tracef.write(f"1082 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1082kbit")
	time.sleep(0.537)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(0.81)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(0.601)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(0.548)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(0.717)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(0.648)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(0.687)
	tracef.write(f"1124 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1124kbit")
	time.sleep(0.703)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.718)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(0.724)
	tracef.write(f"1154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1154kbit")
	time.sleep(0.667)
	tracef.write(f"1106 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1106kbit")
	time.sleep(0.492)
	tracef.write(f"1116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1116kbit")
	time.sleep(0.532)
	tracef.write(f"1181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1181kbit")
	time.sleep(0.809)
	tracef.write(f"1177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1177kbit")
	time.sleep(0.789)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.652)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.69)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(0.799)
	tracef.write(f"1099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1099kbit")
	time.sleep(0.814)
	tracef.write(f"1124 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1124kbit")
	time.sleep(0.62)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(0.781)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(0.497)
	tracef.write(f"1068 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1068kbit")
	time.sleep(0.582)
	tracef.write(f"1138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1138kbit")
	time.sleep(0.583)
	tracef.write(f"1125 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1125kbit")
	time.sleep(0.791)
	tracef.write(f"1152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1152kbit")
	time.sleep(0.594)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.763)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.696)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(0.595)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(0.712)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.537)
	tracef.write(f"1157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1157kbit")
	time.sleep(0.586)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.828)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.539)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(0.544)
	tracef.write(f"1116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1116kbit")
	time.sleep(0.75)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.602)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.678)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.523)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(0.801)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.58)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.594)
	tracef.write(f"1117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1117kbit")
	time.sleep(0.777)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(0.755)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.488)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(0.749)
	tracef.write(f"1141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1141kbit")
	time.sleep(0.702)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(0.689)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(0.517)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.673)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(0.767)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(0.663)
	tracef.write(f"1153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1153kbit")
	time.sleep(0.783)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(0.675)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(0.739)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(0.713)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(0.589)
	tracef.write(f"1105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1105kbit")
	time.sleep(0.536)
	tracef.write(f"1132 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1132kbit")
	time.sleep(0.671)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(0.521)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(0.539)
	tracef.write(f"1066 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1066kbit")
	time.sleep(0.485)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(0.615)
	tracef.write(f"1174 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1174kbit")
	time.sleep(0.753)
	tracef.write(f"1173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1173kbit")
	time.sleep(0.756)
	tracef.write(f"1071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1071kbit")
	time.sleep(0.822)
	tracef.write(f"1108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1108kbit")
	time.sleep(0.729)
	tracef.write(f"1153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1153kbit")
	time.sleep(0.632)
	tracef.write(f"1181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1181kbit")
	time.sleep(0.796)
	tracef.write(f"1091 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1091kbit")
	time.sleep(0.583)
	tracef.write(f"1165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1165kbit")
	time.sleep(0.641)
	tracef.write(f"1127 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1127kbit")
	time.sleep(0.799)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(0.729)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(0.647)
	tracef.write(f"1154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1154kbit")
	time.sleep(0.483)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(0.781)
	tracef.write(f"1159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1159kbit")
	time.sleep(0.824)
	tracef.write(f"1119 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1119kbit")
	time.sleep(0.512)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(0.611)
	tracef.write(f"1133 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1133kbit")
	time.sleep(0.694)
	tracef.write(f"1144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1144kbit")
	time.sleep(0.58)
	tracef.write(f"1076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1076kbit")
	time.sleep(0.713)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.527)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(0.532)
	tracef.write(f"1123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1123kbit")
	time.sleep(0.513)
	tracef.write(f"1091 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1091kbit")
	time.sleep(0.527)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(0.719)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(0.512)
	tracef.write(f"1108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1108kbit")
	time.sleep(0.756)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(0.638)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(0.579)
	tracef.write(f"1073 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1073kbit")
	time.sleep(0.768)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(0.712)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(0.656)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(0.629)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(0.71)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(0.649)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(0.586)
	tracef.write(f"1109 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1109kbit")
	time.sleep(0.687)
	tracef.write(f"1135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1135kbit")
	time.sleep(0.757)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(0.818)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(0.6)
	tracef.write(f"1116 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1116kbit")
	time.sleep(0.597)
	tracef.write(f"1123 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1123kbit")
	time.sleep(0.571)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.698)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(0.516)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(0.553)
	tracef.write(f"1076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1076kbit")
	time.sleep(0.487)
	tracef.write(f"1147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1147kbit")
	time.sleep(0.535)
	tracef.write(f"1128 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1128kbit")
	time.sleep(0.791)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.69)
	tracef.write(f"1125 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1125kbit")
	time.sleep(0.71)
	tracef.write(f"1113 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1113kbit")
	time.sleep(0.487)
	tracef.write(f"1204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1204kbit")
	time.sleep(0.615)
	tracef.write(f"1117 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1117kbit")
	time.sleep(0.625)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(0.66)
	tracef.write(f"1100 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1100kbit")
	time.sleep(0.752)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(0.761)
	tracef.write(f"1172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1172kbit")
	time.sleep(0.677)
	tracef.write(f"1146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1146kbit")
	time.sleep(0.773)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(0.659)
	tracef.write(f"1063 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1063kbit")
	time.sleep(0.731)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.548)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.6)
	tracef.write(f"1137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1137kbit")
	time.sleep(0.588)
	tracef.write(f"1144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1144kbit")
	time.sleep(0.589)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(0.603)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(0.574)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(0.656)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.759)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(0.745)
	tracef.write(f"1155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1155kbit")
	time.sleep(0.65)
	tracef.write(f"1146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1146kbit")
	time.sleep(0.758)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(0.818)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()