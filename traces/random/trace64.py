#t:761-886 ; rate:1181-1376 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace64.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace64.txt", 'a+')
	tracef.write(f"1246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1246kbit")
	time.sleep(0.791)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(0.823)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(0.789)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(0.809)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(0.838)
	tracef.write(f"1289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1289kbit")
	time.sleep(0.789)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.812)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.826)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.789)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.873)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(0.843)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.775)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(0.771)
	tracef.write(f"1356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1356kbit")
	time.sleep(0.844)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(0.801)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.881)
	tracef.write(f"1296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1296kbit")
	time.sleep(0.771)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(0.796)
	tracef.write(f"1339 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1339kbit")
	time.sleep(0.851)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(0.83)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(0.875)
	tracef.write(f"1233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1233kbit")
	time.sleep(0.884)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.838)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(0.792)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(0.821)
	tracef.write(f"1194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1194kbit")
	time.sleep(0.841)
	tracef.write(f"1235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1235kbit")
	time.sleep(0.785)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(0.794)
	tracef.write(f"1331 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1331kbit")
	time.sleep(0.77)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(0.846)
	tracef.write(f"1327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1327kbit")
	time.sleep(0.787)
	tracef.write(f"1356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1356kbit")
	time.sleep(0.88)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(0.793)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.818)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.798)
	tracef.write(f"1224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1224kbit")
	time.sleep(0.763)
	tracef.write(f"1361 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1361kbit")
	time.sleep(0.844)
	tracef.write(f"1299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1299kbit")
	time.sleep(0.878)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(0.823)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(0.805)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(0.834)
	tracef.write(f"1192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1192kbit")
	time.sleep(0.881)
	tracef.write(f"1275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1275kbit")
	time.sleep(0.878)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(0.886)
	tracef.write(f"1207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1207kbit")
	time.sleep(0.829)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(0.781)
	tracef.write(f"1195 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1195kbit")
	time.sleep(0.765)
	tracef.write(f"1298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1298kbit")
	time.sleep(0.778)
	tracef.write(f"1290 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1290kbit")
	time.sleep(0.786)
	tracef.write(f"1351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1351kbit")
	time.sleep(0.791)
	tracef.write(f"1326 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1326kbit")
	time.sleep(0.838)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(0.797)
	tracef.write(f"1359 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1359kbit")
	time.sleep(0.786)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(0.843)
	tracef.write(f"1304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1304kbit")
	time.sleep(0.876)
	tracef.write(f"1342 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1342kbit")
	time.sleep(0.803)
	tracef.write(f"1337 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1337kbit")
	time.sleep(0.855)
	tracef.write(f"1349 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1349kbit")
	time.sleep(0.806)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(0.805)
	tracef.write(f"1362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1362kbit")
	time.sleep(0.797)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.809)
	tracef.write(f"1212 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1212kbit")
	time.sleep(0.884)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(0.81)
	tracef.write(f"1229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1229kbit")
	time.sleep(0.817)
	tracef.write(f"1348 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1348kbit")
	time.sleep(0.786)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(0.771)
	tracef.write(f"1324 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1324kbit")
	time.sleep(0.826)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(0.768)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(0.771)
	tracef.write(f"1357 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1357kbit")
	time.sleep(0.812)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(0.841)
	tracef.write(f"1319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1319kbit")
	time.sleep(0.821)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(0.872)
	tracef.write(f"1365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1365kbit")
	time.sleep(0.81)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(0.835)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(0.857)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(0.811)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(0.818)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(0.87)
	tracef.write(f"1247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1247kbit")
	time.sleep(0.829)
	tracef.write(f"1288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1288kbit")
	time.sleep(0.795)
	tracef.write(f"1278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1278kbit")
	time.sleep(0.869)
	tracef.write(f"1338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1338kbit")
	time.sleep(0.82)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(0.802)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(0.858)
	tracef.write(f"1238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1238kbit")
	time.sleep(0.762)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(0.877)
	tracef.write(f"1240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1240kbit")
	time.sleep(0.841)
	tracef.write(f"1230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1230kbit")
	time.sleep(0.805)
	tracef.write(f"1302 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1302kbit")
	time.sleep(0.814)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(0.83)
	tracef.write(f"1295 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1295kbit")
	time.sleep(0.859)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(0.883)
	tracef.write(f"1355 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1355kbit")
	time.sleep(0.817)
	tracef.write(f"1220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1220kbit")
	time.sleep(0.804)
	tracef.write(f"1314 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1314kbit")
	time.sleep(0.837)
	tracef.write(f"1286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1286kbit")
	time.sleep(0.871)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(0.872)
	tracef.write(f"1237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1237kbit")
	time.sleep(0.805)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(0.772)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.795)
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1217kbit")
	time.sleep(0.764)
	tracef.write(f"1297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1297kbit")
	time.sleep(0.839)
	tracef.write(f"1328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1328kbit")
	time.sleep(0.767)
	tracef.write(f"1198 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1198kbit")
	time.sleep(0.866)
	tracef.write(f"1185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1185kbit")
	time.sleep(0.771)
	tracef.write(f"1272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1272kbit")
	time.sleep(0.78)
	tracef.write(f"1306 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1306kbit")
	time.sleep(0.801)
	tracef.write(f"1347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1347kbit")
	time.sleep(0.775)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(0.766)
	tracef.write(f"1197 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1197kbit")
	time.sleep(0.763)
	tracef.write(f"1205 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1205kbit")
	time.sleep(0.8)
	tracef.write(f"1325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1325kbit")
	time.sleep(0.831)
	tracef.write(f"1291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1291kbit")
	time.sleep(0.859)
	tracef.write(f"1305 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1305kbit")
	time.sleep(0.792)
	tracef.write(f"1344 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1344kbit")
	time.sleep(0.815)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(0.783)
	tracef.write(f"1293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1293kbit")
	time.sleep(0.88)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(0.881)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(0.817)
	tracef.write(f"1341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1341kbit")
	time.sleep(0.774)
	tracef.write(f"1358 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1358kbit")
	time.sleep(0.828)
	tracef.write(f"1365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1365kbit")
	time.sleep(0.87)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()