#t:2420-2814 ; rate:831-1011 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace50.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace50.txt", 'a+')
	tracef.write(f"906 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 906kbit")
	time.sleep(2.808)
	tracef.write(f"885 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 885kbit")
	time.sleep(2.774)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(2.749)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(2.453)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(2.769)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(2.621)
	tracef.write(f"897 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 897kbit")
	time.sleep(2.713)
	tracef.write(f"910 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 910kbit")
	time.sleep(2.603)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(2.605)
	tracef.write(f"872 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 872kbit")
	time.sleep(2.452)
	tracef.write(f"989 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 989kbit")
	time.sleep(2.592)
	tracef.write(f"996 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 996kbit")
	time.sleep(2.671)
	tracef.write(f"858 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 858kbit")
	time.sleep(2.64)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(2.661)
	tracef.write(f"976 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 976kbit")
	time.sleep(2.511)
	tracef.write(f"872 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 872kbit")
	time.sleep(2.752)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(2.574)
	tracef.write(f"1009 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1009kbit")
	time.sleep(2.547)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(2.612)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(2.556)
	tracef.write(f"874 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 874kbit")
	time.sleep(2.553)
	tracef.write(f"906 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 906kbit")
	time.sleep(2.682)
	tracef.write(f"1009 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1009kbit")
	time.sleep(2.673)
	tracef.write(f"849 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 849kbit")
	time.sleep(2.769)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(2.643)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(2.543)
	tracef.write(f"886 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 886kbit")
	time.sleep(2.694)
	tracef.write(f"906 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 906kbit")
	time.sleep(2.599)
	tracef.write(f"958 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 958kbit")
	time.sleep(2.507)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(2.742)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(2.599)
	tracef.write(f"874 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 874kbit")
	time.sleep(2.426)
	tracef.write(f"995 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 995kbit")
	time.sleep(2.782)
	tracef.write(f"840 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 840kbit")
	time.sleep(2.448)
	tracef.write(f"968 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 968kbit")
	time.sleep(2.55)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(2.73)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(2.546)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(2.546)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()