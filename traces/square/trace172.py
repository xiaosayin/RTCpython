#t:2114-2812 ; rate:875-942 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace172.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace172.txt", 'a+')
	tracef.write(f"902 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 902kbit")
	time.sleep(2.393)
	tracef.write(f"882 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 882kbit")
	time.sleep(2.609)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(2.773)
	tracef.write(f"903 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 903kbit")
	time.sleep(2.127)
	tracef.write(f"895 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 895kbit")
	time.sleep(2.125)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(2.629)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(2.731)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(2.209)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(2.691)
	tracef.write(f"904 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 904kbit")
	time.sleep(2.168)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(2.218)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(2.135)
	tracef.write(f"913 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 913kbit")
	time.sleep(2.157)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(2.156)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(2.369)
	tracef.write(f"876 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 876kbit")
	time.sleep(2.793)
	tracef.write(f"888 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 888kbit")
	time.sleep(2.602)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(2.811)
	tracef.write(f"879 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 879kbit")
	time.sleep(2.463)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(2.439)
	tracef.write(f"903 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 903kbit")
	time.sleep(2.21)
	tracef.write(f"914 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 914kbit")
	time.sleep(2.453)
	tracef.write(f"910 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 910kbit")
	time.sleep(2.572)
	tracef.write(f"903 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 903kbit")
	time.sleep(2.339)
	tracef.write(f"910 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 910kbit")
	time.sleep(2.337)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(2.202)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(2.447)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(2.635)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(2.727)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(2.651)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(2.349)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(2.259)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(2.428)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(2.496)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(2.582)
	tracef.write(f"887 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 887kbit")
	time.sleep(2.279)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(2.652)
	tracef.write(f"886 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 886kbit")
	time.sleep(2.279)
	tracef.write(f"878 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 878kbit")
	time.sleep(2.357)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(2.646)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(2.646)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()