#t:1334-1893 ; rate:1034-1102 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace71.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace71.txt", 'a+')
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1087kbit")
	time.sleep(1.857)
	tracef.write(f"1076 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1076kbit")
	time.sleep(1.524)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(1.839)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(1.89)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(1.885)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(1.397)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(1.68)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(1.535)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(1.89)
	tracef.write(f"1036 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1036kbit")
	time.sleep(1.651)
	tracef.write(f"1100 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1100kbit")
	time.sleep(1.745)
	tracef.write(f"1056 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1056kbit")
	time.sleep(1.888)
	tracef.write(f"1082 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1082kbit")
	time.sleep(1.695)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(1.43)
	tracef.write(f"1047 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1047kbit")
	time.sleep(1.466)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(1.348)
	tracef.write(f"1045 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1045kbit")
	time.sleep(1.622)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(1.693)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(1.569)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(1.884)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(1.61)
	tracef.write(f"1047 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1047kbit")
	time.sleep(1.845)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(1.689)
	tracef.write(f"1091 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1091kbit")
	time.sleep(1.79)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(1.56)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.429)
	tracef.write(f"1049 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1049kbit")
	time.sleep(1.707)
	tracef.write(f"1040 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1040kbit")
	time.sleep(1.495)
	tracef.write(f"1071 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1071kbit")
	time.sleep(1.879)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.499)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(1.731)
	tracef.write(f"1064 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1064kbit")
	time.sleep(1.42)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(1.788)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(1.841)
	tracef.write(f"1039 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1039kbit")
	time.sleep(1.761)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(1.737)
	tracef.write(f"1043 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1043kbit")
	time.sleep(1.757)
	tracef.write(f"1038 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1038kbit")
	time.sleep(1.717)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(1.472)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.795)
	tracef.write(f"1095 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1095kbit")
	time.sleep(1.531)
	tracef.write(f"1050 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1050kbit")
	time.sleep(1.335)
	tracef.write(f"1037 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1037kbit")
	time.sleep(1.486)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(1.832)
	tracef.write(f"1078 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1078kbit")
	time.sleep(1.809)
	tracef.write(f"1096 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1096kbit")
	time.sleep(1.391)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(1.751)
	tracef.write(f"1100 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1100kbit")
	time.sleep(1.64)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(1.785)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(1.359)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(1.364)
	tracef.write(f"1086 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1086kbit")
	time.sleep(1.383)
	tracef.write(f"1096 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1096kbit")
	time.sleep(1.823)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(1.769)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(1.876)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(1.349)
	tracef.write(f"1097 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1097kbit")
	time.sleep(1.622)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(1.867)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(1.867)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()