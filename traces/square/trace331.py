#t:2344-2921 ; rate:874-1102 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace331.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace331.txt", 'a+')
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 934kbit")
	time.sleep(2.847)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.734)
	tracef.write(f"1005 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1005kbit")
	time.sleep(2.754)
	tracef.write(f"891 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 891kbit")
	time.sleep(2.625)
	tracef.write(f"1067 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1067kbit")
	time.sleep(2.377)
	tracef.write(f"1005 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1005kbit")
	time.sleep(2.505)
	tracef.write(f"879 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 879kbit")
	time.sleep(2.777)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(2.373)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(2.788)
	tracef.write(f"924 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 924kbit")
	time.sleep(2.86)
	tracef.write(f"1054 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1054kbit")
	time.sleep(2.567)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(2.636)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(2.378)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(2.462)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(2.48)
	tracef.write(f"915 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 915kbit")
	time.sleep(2.526)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(2.869)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(2.446)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(2.613)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.543)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(2.872)
	tracef.write(f"1085 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1085kbit")
	time.sleep(2.594)
	tracef.write(f"1027 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1027kbit")
	time.sleep(2.783)
	tracef.write(f"987 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 987kbit")
	time.sleep(2.874)
	tracef.write(f"1040 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1040kbit")
	time.sleep(2.507)
	tracef.write(f"960 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 960kbit")
	time.sleep(2.51)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.764)
	tracef.write(f"960 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 960kbit")
	time.sleep(2.917)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(2.875)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(2.562)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(2.918)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(2.361)
	tracef.write(f"1069 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1069kbit")
	time.sleep(2.813)
	tracef.write(f"911 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 911kbit")
	time.sleep(2.419)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(2.447)
	tracef.write(f"1061 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1061kbit")
	time.sleep(2.546)
	tracef.write(f"1073 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1073kbit")
	time.sleep(2.391)
	tracef.write(f"1073 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1073kbit")
	time.sleep(2.391)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()