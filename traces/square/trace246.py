#t:1807-1878 ; rate:903-1298 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace246.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace246.txt", 'a+')
	tracef.write(f"963 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 963kbit")
	time.sleep(1.857)
	tracef.write(f"1181 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1181kbit")
	time.sleep(1.834)
	tracef.write(f"1187 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1187kbit")
	time.sleep(1.874)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(1.852)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(1.823)
	tracef.write(f"1292 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1292kbit")
	time.sleep(1.812)
	tracef.write(f"1120 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1120kbit")
	time.sleep(1.838)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(1.877)
	tracef.write(f"1203 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1203kbit")
	time.sleep(1.863)
	tracef.write(f"1287 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1287kbit")
	time.sleep(1.842)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(1.812)
	tracef.write(f"1251 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1251kbit")
	time.sleep(1.815)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(1.817)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(1.841)
	tracef.write(f"1263 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1263kbit")
	time.sleep(1.809)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(1.857)
	tracef.write(f"1166 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1166kbit")
	time.sleep(1.845)
	tracef.write(f"1130 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1130kbit")
	time.sleep(1.851)
	tracef.write(f"1218 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1218kbit")
	time.sleep(1.867)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(1.851)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(1.818)
	tracef.write(f"1075 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1075kbit")
	time.sleep(1.859)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(1.807)
	tracef.write(f"1161 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1161kbit")
	time.sleep(1.829)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(1.836)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(1.81)
	tracef.write(f"1266 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1266kbit")
	time.sleep(1.861)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(1.859)
	tracef.write(f"999 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 999kbit")
	time.sleep(1.838)
	tracef.write(f"1282 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1282kbit")
	time.sleep(1.811)
	tracef.write(f"1242 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1242kbit")
	time.sleep(1.814)
	tracef.write(f"1170 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1170kbit")
	time.sleep(1.863)
	tracef.write(f"1261 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1261kbit")
	time.sleep(1.856)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.825)
	tracef.write(f"971 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 971kbit")
	time.sleep(1.825)
	tracef.write(f"1259 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1259kbit")
	time.sleep(1.851)
	tracef.write(f"992 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 992kbit")
	time.sleep(1.863)
	tracef.write(f"1202 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1202kbit")
	time.sleep(1.866)
	tracef.write(f"1044 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1044kbit")
	time.sleep(1.836)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(1.86)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(1.848)
	tracef.write(f"1114 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1114kbit")
	time.sleep(1.819)
	tracef.write(f"1033 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1033kbit")
	time.sleep(1.86)
	tracef.write(f"992 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 992kbit")
	time.sleep(1.832)
	tracef.write(f"965 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 965kbit")
	time.sleep(1.838)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(1.878)
	tracef.write(f"962 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 962kbit")
	time.sleep(1.84)
	tracef.write(f"1090 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1090kbit")
	time.sleep(1.838)
	tracef.write(f"1207 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1207kbit")
	time.sleep(1.849)
	tracef.write(f"1053 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1053kbit")
	time.sleep(1.841)
	tracef.write(f"1240 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1240kbit")
	time.sleep(1.859)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(1.869)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(1.869)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()