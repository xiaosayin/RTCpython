#t:1402-2830 ; rate:876-1279 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace116.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace116.txt", 'a+')
	tracef.write(f"1031 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 1031kbit")
	time.sleep(1.436)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(1.479)
	tracef.write(f"1058 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1058kbit")
	time.sleep(1.785)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(1.696)
	tracef.write(f"964 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 964kbit")
	time.sleep(2.648)
	tracef.write(f"1014 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1014kbit")
	time.sleep(2.075)
	tracef.write(f"1188 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1188kbit")
	time.sleep(1.733)
	tracef.write(f"1199 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1199kbit")
	time.sleep(2.567)
	tracef.write(f"1049 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1049kbit")
	time.sleep(2.024)
	tracef.write(f"1118 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1118kbit")
	time.sleep(2.776)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(2.83)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(1.448)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(1.491)
	tracef.write(f"1210 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1210kbit")
	time.sleep(2.347)
	tracef.write(f"1243 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1243kbit")
	time.sleep(1.562)
	tracef.write(f"1254 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1254kbit")
	time.sleep(2.614)
	tracef.write(f"887 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 887kbit")
	time.sleep(2.493)
	tracef.write(f"1088 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1088kbit")
	time.sleep(1.646)
	tracef.write(f"892 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 892kbit")
	time.sleep(2.232)
	tracef.write(f"1151 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1151kbit")
	time.sleep(2.61)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(2.192)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(2.617)
	tracef.write(f"1023 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1023kbit")
	time.sleep(1.95)
	tracef.write(f"891 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 891kbit")
	time.sleep(2.341)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(1.415)
	tracef.write(f"1126 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1126kbit")
	time.sleep(2.059)
	tracef.write(f"1231 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1231kbit")
	time.sleep(2.618)
	tracef.write(f"1062 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1062kbit")
	time.sleep(1.692)
	tracef.write(f"894 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 894kbit")
	time.sleep(1.933)
	tracef.write(f"1019 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1019kbit")
	time.sleep(1.927)
	tracef.write(f"1003 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1003kbit")
	time.sleep(2.568)
	tracef.write(f"1154 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1154kbit")
	time.sleep(2.525)
	tracef.write(f"1002 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1002kbit")
	time.sleep(1.783)
	tracef.write(f"1236 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1236kbit")
	time.sleep(2.656)
	tracef.write(f"1006 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1006kbit")
	time.sleep(2.337)
	tracef.write(f"982 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 982kbit")
	time.sleep(2.336)
	tracef.write(f"992 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 992kbit")
	time.sleep(1.99)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(1.698)
	tracef.write(f"1098 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1098kbit")
	time.sleep(2.512)
	tracef.write(f"995 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 995kbit")
	time.sleep(1.94)
	tracef.write(f"1049 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1049kbit")
	time.sleep(1.724)
	tracef.write(f"877 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 877kbit")
	time.sleep(2.077)
	tracef.write(f"1271 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1271kbit")
	time.sleep(1.428)
	tracef.write(f"970 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 970kbit")
	time.sleep(2.37)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(2.268)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(2.062)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(2.062)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()