#t:1424-1729 ; rate:810-949 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link(sudoPW):
	tracef = open("traces/square/trace56.txt", 'w')
	tracef.close()
	tracef = open("traces/square/trace56.txt", 'a+')
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc add dev lo root netem rate 859kbit")
	time.sleep(1.629)
	tracef.write(f"861 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 861kbit")
	time.sleep(1.549)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(1.523)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(1.689)
	tracef.write(f"869 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 869kbit")
	time.sleep(1.578)
	tracef.write(f"837 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 837kbit")
	time.sleep(1.709)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(1.562)
	tracef.write(f"873 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 873kbit")
	time.sleep(1.669)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(1.543)
	tracef.write(f"868 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 868kbit")
	time.sleep(1.727)
	tracef.write(f"938 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 938kbit")
	time.sleep(1.438)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(1.596)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(1.555)
	tracef.write(f"877 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 877kbit")
	time.sleep(1.514)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(1.697)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(1.702)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(1.588)
	tracef.write(f"813 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 813kbit")
	time.sleep(1.656)
	tracef.write(f"840 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 840kbit")
	time.sleep(1.547)
	tracef.write(f"836 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 836kbit")
	time.sleep(1.51)
	tracef.write(f"832 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 832kbit")
	time.sleep(1.674)
	tracef.write(f"898 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 898kbit")
	time.sleep(1.567)
	tracef.write(f"847 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 847kbit")
	time.sleep(1.506)
	tracef.write(f"822 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 822kbit")
	time.sleep(1.688)
	tracef.write(f"843 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 843kbit")
	time.sleep(1.531)
	tracef.write(f"919 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 919kbit")
	time.sleep(1.633)
	tracef.write(f"823 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 823kbit")
	time.sleep(1.705)
	tracef.write(f"867 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 867kbit")
	time.sleep(1.644)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(1.606)
	tracef.write(f"917 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 917kbit")
	time.sleep(1.631)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(1.535)
	tracef.write(f"913 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 913kbit")
	time.sleep(1.462)
	tracef.write(f"824 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 824kbit")
	time.sleep(1.528)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(1.696)
	tracef.write(f"872 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 872kbit")
	time.sleep(1.625)
	tracef.write(f"863 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 863kbit")
	time.sleep(1.507)
	tracef.write(f"878 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 878kbit")
	time.sleep(1.48)
	tracef.write(f"899 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 899kbit")
	time.sleep(1.686)
	tracef.write(f"825 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 825kbit")
	time.sleep(1.498)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(1.621)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(1.729)
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 841kbit")
	time.sleep(1.553)
	tracef.write(f"922 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 922kbit")
	time.sleep(1.49)
	tracef.write(f"823 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 823kbit")
	time.sleep(1.645)
	tracef.write(f"874 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 874kbit")
	time.sleep(1.446)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(1.582)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(1.467)
	tracef.write(f"925 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 925kbit")
	time.sleep(1.643)
	tracef.write(f"895 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 895kbit")
	time.sleep(1.687)
	tracef.write(f"840 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 840kbit")
	time.sleep(1.557)
	tracef.write(f"825 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 825kbit")
	time.sleep(1.631)
	tracef.write(f"901 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 901kbit")
	time.sleep(1.609)
	tracef.write(f"880 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 880kbit")
	time.sleep(1.523)
	tracef.write(f"947 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 947kbit")
	time.sleep(1.439)
	tracef.write(f"869 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 869kbit")
	time.sleep(1.528)
	tracef.write(f"900 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 900kbit")
	time.sleep(1.528)
	tracef.write(f"839 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 839kbit")
	time.sleep(1.645)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(1.502)
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 841kbit")
	time.sleep(1.461)
	tracef.write(f"884 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 884kbit")
	time.sleep(1.492)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(1.614)
	tracef.write(f"851 ; {round(time.time() * 1000)}\n")
	os.system(f"echo {sudoPW} | sudo -S tc qdisc change dev lo root netem rate 851kbit")
	time.sleep(1.614)
	os.system("echo {sudoPW} | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()