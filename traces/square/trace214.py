#t:1338-1509 ; rate:1013-1339 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace214.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace214.txt", 'a+')
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1225kbit")
	time.sleep(1.469)
	tracef.write(f"1300 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1300kbit")
	time.sleep(1.432)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(1.478)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(1.372)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(1.429)
	tracef.write(f"1216 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1216kbit")
	time.sleep(1.39)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(1.374)
	tracef.write(f"1052 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1052kbit")
	time.sleep(1.346)
	tracef.write(f"1166 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1166kbit")
	time.sleep(1.414)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(1.438)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(1.411)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(1.412)
	tracef.write(f"1279 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1279kbit")
	time.sleep(1.365)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(1.378)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(1.364)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(1.486)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(1.425)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(1.469)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(1.498)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.349)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(1.396)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(1.367)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(1.491)
	tracef.write(f"1141 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1141kbit")
	time.sleep(1.363)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(1.45)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(1.45)
	tracef.write(f"1127 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1127kbit")
	time.sleep(1.434)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(1.362)
	tracef.write(f"1162 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1162kbit")
	time.sleep(1.391)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(1.382)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(1.398)
	tracef.write(f"1075 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1075kbit")
	time.sleep(1.383)
	tracef.write(f"1182 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1182kbit")
	time.sleep(1.493)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(1.508)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(1.476)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(1.416)
	tracef.write(f"1195 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1195kbit")
	time.sleep(1.364)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(1.437)
	tracef.write(f"1284 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1284kbit")
	time.sleep(1.341)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(1.466)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(1.421)
	tracef.write(f"1265 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1265kbit")
	time.sleep(1.35)
	tracef.write(f"1049 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1049kbit")
	time.sleep(1.471)
	tracef.write(f"1079 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1079kbit")
	time.sleep(1.346)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(1.497)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(1.346)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(1.496)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(1.448)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(1.454)
	tracef.write(f"1131 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1131kbit")
	time.sleep(1.49)
	tracef.write(f"1144 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1144kbit")
	time.sleep(1.395)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(1.492)
	tracef.write(f"1129 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1129kbit")
	time.sleep(1.384)
	tracef.write(f"1186 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1186kbit")
	time.sleep(1.372)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(1.393)
	tracef.write(f"1018 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1018kbit")
	time.sleep(1.353)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(1.425)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(1.37)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(1.342)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(1.351)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(1.424)
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1246kbit")
	time.sleep(1.507)
	tracef.write(f"1145 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1145kbit")
	time.sleep(1.399)
	tracef.write(f"1114 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1114kbit")
	time.sleep(1.483)
	tracef.write(f"1174 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1174kbit")
	time.sleep(1.501)
	tracef.write(f"1102 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1102kbit")
	time.sleep(1.377)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(1.364)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(1.508)
	tracef.write(f"1285 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1285kbit")
	time.sleep(1.508)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()