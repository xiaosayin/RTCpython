#t:1161-1628 ; rate:878-1105 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace76.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace76.txt", 'a+')
	tracef.write(f"932 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 932kbit")
	time.sleep(1.161)
	tracef.write(f"904 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 904kbit")
	time.sleep(1.289)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(1.408)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(1.529)
	tracef.write(f"919 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 919kbit")
	time.sleep(1.575)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(1.337)
	tracef.write(f"1069 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1069kbit")
	time.sleep(1.618)
	tracef.write(f"1003 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1003kbit")
	time.sleep(1.444)
	tracef.write(f"1084 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1084kbit")
	time.sleep(1.603)
	tracef.write(f"929 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 929kbit")
	time.sleep(1.262)
	tracef.write(f"1089 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1089kbit")
	time.sleep(1.378)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(1.411)
	tracef.write(f"884 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 884kbit")
	time.sleep(1.586)
	tracef.write(f"906 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 906kbit")
	time.sleep(1.491)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(1.424)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(1.487)
	tracef.write(f"962 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 962kbit")
	time.sleep(1.393)
	tracef.write(f"993 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 993kbit")
	time.sleep(1.616)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(1.437)
	tracef.write(f"1051 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1051kbit")
	time.sleep(1.366)
	tracef.write(f"1072 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1072kbit")
	time.sleep(1.544)
	tracef.write(f"1016 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1016kbit")
	time.sleep(1.198)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(1.427)
	tracef.write(f"992 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 992kbit")
	time.sleep(1.527)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(1.164)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(1.246)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(1.283)
	tracef.write(f"895 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 895kbit")
	time.sleep(1.531)
	tracef.write(f"890 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 890kbit")
	time.sleep(1.352)
	tracef.write(f"1035 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1035kbit")
	time.sleep(1.523)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(1.518)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(1.61)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(1.188)
	tracef.write(f"912 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 912kbit")
	time.sleep(1.484)
	tracef.write(f"989 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 989kbit")
	time.sleep(1.279)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(1.543)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(1.542)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(1.367)
	tracef.write(f"1074 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1074kbit")
	time.sleep(1.45)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(1.271)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(1.401)
	tracef.write(f"920 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 920kbit")
	time.sleep(1.324)
	tracef.write(f"991 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 991kbit")
	time.sleep(1.62)
	tracef.write(f"890 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 890kbit")
	time.sleep(1.196)
	tracef.write(f"1060 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1060kbit")
	time.sleep(1.591)
	tracef.write(f"1066 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1066kbit")
	time.sleep(1.627)
	tracef.write(f"974 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 974kbit")
	time.sleep(1.346)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(1.287)
	tracef.write(f"1025 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1025kbit")
	time.sleep(1.444)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(1.52)
	tracef.write(f"992 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 992kbit")
	time.sleep(1.392)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(1.592)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(1.216)
	tracef.write(f"974 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 974kbit")
	time.sleep(1.297)
	tracef.write(f"899 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 899kbit")
	time.sleep(1.49)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(1.257)
	tracef.write(f"1059 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1059kbit")
	time.sleep(1.283)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(1.622)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(1.374)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(1.535)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(1.54)
	tracef.write(f"888 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 888kbit")
	time.sleep(1.627)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(1.165)
	tracef.write(f"1070 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1070kbit")
	time.sleep(1.4)
	tracef.write(f"1077 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1077kbit")
	time.sleep(1.347)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(1.58)
	tracef.write(f"890 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 890kbit")
	time.sleep(1.246)
	tracef.write(f"890 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 890kbit")
	time.sleep(1.246)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()