#t:1861-2655 ; rate:821-1330 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace307.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace307.txt", 'a+')
	tracef.write(f"1189 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1189kbit")
	time.sleep(2.616)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(2.002)
	tracef.write(f"980 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 980kbit")
	time.sleep(2.633)
	tracef.write(f"1142 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1142kbit")
	time.sleep(2.053)
	tracef.write(f"1103 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1103kbit")
	time.sleep(2.516)
	tracef.write(f"1120 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1120kbit")
	time.sleep(2.371)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.273)
	tracef.write(f"1135 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1135kbit")
	time.sleep(2.246)
	tracef.write(f"983 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 983kbit")
	time.sleep(2.121)
	tracef.write(f"1226 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1226kbit")
	time.sleep(1.941)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(1.986)
	tracef.write(f"886 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 886kbit")
	time.sleep(1.938)
	tracef.write(f"857 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 857kbit")
	time.sleep(2.495)
	tracef.write(f"821 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 821kbit")
	time.sleep(2.297)
	tracef.write(f"872 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 872kbit")
	time.sleep(2.168)
	tracef.write(f"1041 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1041kbit")
	time.sleep(1.966)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(1.862)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(2.322)
	tracef.write(f"1209 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1209kbit")
	time.sleep(2.382)
	tracef.write(f"1000 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1000kbit")
	time.sleep(2.492)
	tracef.write(f"1260 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1260kbit")
	time.sleep(1.992)
	tracef.write(f"823 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 823kbit")
	time.sleep(1.999)
	tracef.write(f"870 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 870kbit")
	time.sleep(2.43)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.942)
	tracef.write(f"1104 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1104kbit")
	time.sleep(1.892)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(2.342)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(2.176)
	tracef.write(f"1034 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1034kbit")
	time.sleep(2.627)
	tracef.write(f"1213 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1213kbit")
	time.sleep(2.364)
	tracef.write(f"1114 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1114kbit")
	time.sleep(2.53)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(2.435)
	tracef.write(f"1134 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1134kbit")
	time.sleep(2.418)
	tracef.write(f"908 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 908kbit")
	time.sleep(2.268)
	tracef.write(f"1253 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1253kbit")
	time.sleep(2.27)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(1.98)
	tracef.write(f"921 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 921kbit")
	time.sleep(1.879)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(2.188)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(1.996)
	tracef.write(f"914 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 914kbit")
	time.sleep(2.198)
	tracef.write(f"923 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 923kbit")
	time.sleep(2.379)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(1.876)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(2.082)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(2.093)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(2.093)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()