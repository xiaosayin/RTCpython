#t:199-679 ; rate:933-957 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace131.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace131.txt", 'a+')
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 950kbit")
	time.sleep(0.243)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.242)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.621)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.403)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.25)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.369)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.424)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.378)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.623)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.537)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.489)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.612)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.505)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.394)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.638)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.658)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.499)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.535)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.434)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.505)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.517)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.551)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.339)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.232)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.608)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.549)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.333)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.484)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.376)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.272)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.342)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.489)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.442)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.575)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.272)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.48)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.408)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.578)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.596)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.531)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.458)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.305)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.624)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.572)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.574)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.547)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.356)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.481)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.34)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.243)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.39)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.459)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.421)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.47)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.244)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.484)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.379)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.465)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.274)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.545)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.647)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.257)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.246)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.596)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.452)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.285)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.531)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.425)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.387)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.449)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.437)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.506)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.661)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.674)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.424)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.373)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.49)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.472)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.564)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.587)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.438)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.347)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.206)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.515)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.458)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.601)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.28)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.215)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.618)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.587)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.37)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.587)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.494)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.379)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.397)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.558)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.335)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.598)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.29)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.417)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.287)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.645)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.363)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.206)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.434)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.632)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.27)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.551)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.649)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.321)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.438)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.555)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.552)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.483)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.311)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.252)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.207)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.321)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.575)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.613)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.458)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.206)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.339)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.577)
	tracef.write(f"946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 946kbit")
	time.sleep(0.435)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.335)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.491)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.631)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.591)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.669)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.618)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.576)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.298)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.31)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.613)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.305)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.391)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.674)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.37)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.227)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.414)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.457)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.21)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.483)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.238)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.486)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.486)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.505)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.461)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.414)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.529)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.508)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.443)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.378)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.271)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.511)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.633)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.202)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.422)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.441)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.269)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.606)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.288)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.406)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.207)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.625)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.371)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.533)
	tracef.write(f"951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 951kbit")
	time.sleep(0.568)
	tracef.write(f"936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 936kbit")
	time.sleep(0.288)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.483)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.504)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.225)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.66)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.475)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.383)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.613)
	tracef.write(f"954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 954kbit")
	time.sleep(0.477)
	tracef.write(f"955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 955kbit")
	time.sleep(0.223)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.613)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.226)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.364)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.318)
	tracef.write(f"939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 939kbit")
	time.sleep(0.64)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.58)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.554)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.3)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.474)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.613)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.335)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.276)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.565)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.21)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.662)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.362)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.401)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.231)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.478)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.387)
	tracef.write(f"933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 933kbit")
	time.sleep(0.395)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.503)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.367)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.625)
	tracef.write(f"952 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 952kbit")
	time.sleep(0.474)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.591)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.498)
	tracef.write(f"953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 953kbit")
	time.sleep(0.252)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.448)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.639)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.37)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.253)
	tracef.write(f"950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 950kbit")
	time.sleep(0.57)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.309)
	tracef.write(f"935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 935kbit")
	time.sleep(0.375)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.496)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(0.414)
	tracef.write(f"944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 944kbit")
	time.sleep(0.535)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(0.387)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.496)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.563)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.327)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.308)
	tracef.write(f"934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 934kbit")
	time.sleep(0.418)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.664)
	tracef.write(f"941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 941kbit")
	time.sleep(0.563)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()