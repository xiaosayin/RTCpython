#t:2196-2263 ; rate:848-1022 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace173.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace173.txt", 'a+')
	tracef.write(f"1020 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1020kbit")
	time.sleep(2.257)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(2.242)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(2.24)
	tracef.write(f"857 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 857kbit")
	time.sleep(2.241)
	tracef.write(f"1000 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1000kbit")
	time.sleep(2.233)
	tracef.write(f"884 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 884kbit")
	time.sleep(2.232)
	tracef.write(f"894 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 894kbit")
	time.sleep(2.203)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(2.235)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(2.226)
	tracef.write(f"981 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 981kbit")
	time.sleep(2.24)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(2.21)
	tracef.write(f"989 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 989kbit")
	time.sleep(2.217)
	tracef.write(f"879 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 879kbit")
	time.sleep(2.211)
	tracef.write(f"1017 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1017kbit")
	time.sleep(2.197)
	tracef.write(f"999 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 999kbit")
	time.sleep(2.216)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(2.256)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(2.24)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(2.214)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(2.228)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(2.217)
	tracef.write(f"995 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 995kbit")
	time.sleep(2.238)
	tracef.write(f"871 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 871kbit")
	time.sleep(2.199)
	tracef.write(f"977 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 977kbit")
	time.sleep(2.208)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(2.196)
	tracef.write(f"1000 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1000kbit")
	time.sleep(2.228)
	tracef.write(f"885 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 885kbit")
	time.sleep(2.215)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(2.236)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(2.242)
	tracef.write(f"1016 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1016kbit")
	time.sleep(2.237)
	tracef.write(f"875 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 875kbit")
	time.sleep(2.201)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(2.25)
	tracef.write(f"1009 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1009kbit")
	time.sleep(2.239)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(2.255)
	tracef.write(f"963 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 963kbit")
	time.sleep(2.247)
	tracef.write(f"904 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 904kbit")
	time.sleep(2.222)
	tracef.write(f"965 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 965kbit")
	time.sleep(2.251)
	tracef.write(f"928 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 928kbit")
	time.sleep(2.259)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(2.237)
	tracef.write(f"848 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 848kbit")
	time.sleep(2.229)
	tracef.write(f"1007 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1007kbit")
	time.sleep(2.203)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(2.229)
	tracef.write(f"858 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 858kbit")
	time.sleep(2.245)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(2.197)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(2.197)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()