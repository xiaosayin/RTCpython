#t:1468-2797 ; rate:834-858 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace95.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace95.txt", 'a+')
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 841kbit")
	time.sleep(2.037)
	tracef.write(f"854 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 854kbit")
	time.sleep(2.634)
	tracef.write(f"847 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 847kbit")
	time.sleep(2.579)
	tracef.write(f"855 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 855kbit")
	time.sleep(2.484)
	tracef.write(f"839 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 839kbit")
	time.sleep(2.46)
	tracef.write(f"842 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 842kbit")
	time.sleep(1.762)
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 841kbit")
	time.sleep(2.744)
	tracef.write(f"845 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 845kbit")
	time.sleep(1.83)
	tracef.write(f"853 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 853kbit")
	time.sleep(1.565)
	tracef.write(f"844 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 844kbit")
	time.sleep(2.368)
	tracef.write(f"839 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 839kbit")
	time.sleep(1.649)
	tracef.write(f"856 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 856kbit")
	time.sleep(1.754)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(2.138)
	tracef.write(f"845 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 845kbit")
	time.sleep(2.473)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(2.44)
	tracef.write(f"834 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 834kbit")
	time.sleep(2.369)
	tracef.write(f"854 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 854kbit")
	time.sleep(2.13)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(1.932)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(1.845)
	tracef.write(f"853 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 853kbit")
	time.sleep(1.906)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(2.69)
	tracef.write(f"842 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 842kbit")
	time.sleep(2.724)
	tracef.write(f"857 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 857kbit")
	time.sleep(2.152)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(2.636)
	tracef.write(f"848 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 848kbit")
	time.sleep(1.546)
	tracef.write(f"855 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 855kbit")
	time.sleep(1.681)
	tracef.write(f"852 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 852kbit")
	time.sleep(1.658)
	tracef.write(f"837 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 837kbit")
	time.sleep(2.149)
	tracef.write(f"849 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 849kbit")
	time.sleep(2.723)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(2.103)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(1.752)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(1.475)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(1.624)
	tracef.write(f"847 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 847kbit")
	time.sleep(2.681)
	tracef.write(f"850 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 850kbit")
	time.sleep(2.482)
	tracef.write(f"850 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 850kbit")
	time.sleep(2.259)
	tracef.write(f"854 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 854kbit")
	time.sleep(2.268)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(1.484)
	tracef.write(f"837 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 837kbit")
	time.sleep(1.559)
	tracef.write(f"842 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 842kbit")
	time.sleep(2.253)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(1.89)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(1.48)
	tracef.write(f"853 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 853kbit")
	time.sleep(2.029)
	tracef.write(f"850 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 850kbit")
	time.sleep(1.616)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(2.629)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(2.273)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(2.273)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()