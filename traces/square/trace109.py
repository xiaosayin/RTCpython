#t:2216-2695 ; rate:1178-1277 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace109.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace109.txt", 'a+')
	tracef.write(f"1217 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1217kbit")
	time.sleep(2.622)
	tracef.write(f"1273 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1273kbit")
	time.sleep(2.48)
	tracef.write(f"1208 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1208kbit")
	time.sleep(2.666)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(2.517)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(2.239)
	tracef.write(f"1203 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1203kbit")
	time.sleep(2.598)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(2.606)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(2.548)
	tracef.write(f"1276 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1276kbit")
	time.sleep(2.221)
	tracef.write(f"1252 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1252kbit")
	time.sleep(2.674)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.483)
	tracef.write(f"1255 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1255kbit")
	time.sleep(2.486)
	tracef.write(f"1180 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1180kbit")
	time.sleep(2.233)
	tracef.write(f"1240 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1240kbit")
	time.sleep(2.4)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(2.426)
	tracef.write(f"1200 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1200kbit")
	time.sleep(2.509)
	tracef.write(f"1211 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1211kbit")
	time.sleep(2.359)
	tracef.write(f"1256 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1256kbit")
	time.sleep(2.41)
	tracef.write(f"1244 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1244kbit")
	time.sleep(2.335)
	tracef.write(f"1232 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1232kbit")
	time.sleep(2.446)
	tracef.write(f"1184 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1184kbit")
	time.sleep(2.383)
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1189kbit")
	time.sleep(2.543)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.312)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(2.445)
	tracef.write(f"1241 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1241kbit")
	time.sleep(2.512)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(2.281)
	tracef.write(f"1255 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1255kbit")
	time.sleep(2.417)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(2.514)
	tracef.write(f"1270 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1270kbit")
	time.sleep(2.374)
	tracef.write(f"1225 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1225kbit")
	time.sleep(2.673)
	tracef.write(f"1191 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1191kbit")
	time.sleep(2.354)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(2.316)
	tracef.write(f"1222 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1222kbit")
	time.sleep(2.292)
	tracef.write(f"1274 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1274kbit")
	time.sleep(2.263)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(2.34)
	tracef.write(f"1221 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1221kbit")
	time.sleep(2.482)
	tracef.write(f"1183 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1183kbit")
	time.sleep(2.336)
	tracef.write(f"1249 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1249kbit")
	time.sleep(2.471)
	tracef.write(f"1257 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1257kbit")
	time.sleep(2.339)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(2.292)
	tracef.write(f"1250 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1250kbit")
	time.sleep(2.292)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()