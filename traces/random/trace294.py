#t:863-933 ; rate:119-1169 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace294.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace294.txt", 'a+')
	tracef.write(f"1146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1146kbit")
	time.sleep(0.9)
	tracef.write(f"246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 246kbit")
	time.sleep(0.932)
	tracef.write(f"662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 662kbit")
	time.sleep(0.927)
	tracef.write(f"1101 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1101kbit")
	time.sleep(0.904)
	tracef.write(f"418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 418kbit")
	time.sleep(0.93)
	tracef.write(f"1094 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1094kbit")
	time.sleep(0.878)
	tracef.write(f"760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 760kbit")
	time.sleep(0.932)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.871)
	tracef.write(f"1167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1167kbit")
	time.sleep(0.927)
	tracef.write(f"1120 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1120kbit")
	time.sleep(0.876)
	tracef.write(f"862 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 862kbit")
	time.sleep(0.915)
	tracef.write(f"358 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 358kbit")
	time.sleep(0.866)
	tracef.write(f"668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 668kbit")
	time.sleep(0.87)
	tracef.write(f"608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 608kbit")
	time.sleep(0.917)
	tracef.write(f"937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 937kbit")
	time.sleep(0.866)
	tracef.write(f"959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 959kbit")
	time.sleep(0.904)
	tracef.write(f"347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 347kbit")
	time.sleep(0.922)
	tracef.write(f"440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 440kbit")
	time.sleep(0.878)
	tracef.write(f"767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 767kbit")
	time.sleep(0.902)
	tracef.write(f"1164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1164kbit")
	time.sleep(0.91)
	tracef.write(f"656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 656kbit")
	time.sleep(0.901)
	tracef.write(f"482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 482kbit")
	time.sleep(0.922)
	tracef.write(f"1115 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1115kbit")
	time.sleep(0.879)
	tracef.write(f"1148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1148kbit")
	time.sleep(0.893)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.904)
	tracef.write(f"631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 631kbit")
	time.sleep(0.881)
	tracef.write(f"205 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 205kbit")
	time.sleep(0.914)
	tracef.write(f"537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 537kbit")
	time.sleep(0.896)
	tracef.write(f"475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 475kbit")
	time.sleep(0.917)
	tracef.write(f"523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 523kbit")
	time.sleep(0.883)
	tracef.write(f"969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 969kbit")
	time.sleep(0.901)
	tracef.write(f"456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 456kbit")
	time.sleep(0.896)
	tracef.write(f"1048 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1048kbit")
	time.sleep(0.865)
	tracef.write(f"782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 782kbit")
	time.sleep(0.924)
	tracef.write(f"807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 807kbit")
	time.sleep(0.883)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.917)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.883)
	tracef.write(f"521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 521kbit")
	time.sleep(0.872)
	tracef.write(f"781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 781kbit")
	time.sleep(0.901)
	tracef.write(f"755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 755kbit")
	time.sleep(0.876)
	tracef.write(f"1021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1021kbit")
	time.sleep(0.876)
	tracef.write(f"496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 496kbit")
	time.sleep(0.915)
	tracef.write(f"831 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 831kbit")
	time.sleep(0.898)
	tracef.write(f"702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 702kbit")
	time.sleep(0.87)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.882)
	tracef.write(f"262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 262kbit")
	time.sleep(0.927)
	tracef.write(f"206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 206kbit")
	time.sleep(0.863)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.868)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.93)
	tracef.write(f"717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 717kbit")
	time.sleep(0.925)
	tracef.write(f"457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 457kbit")
	time.sleep(0.932)
	tracef.write(f"402 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 402kbit")
	time.sleep(0.922)
	tracef.write(f"1156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1156kbit")
	time.sleep(0.901)
	tracef.write(f"906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 906kbit")
	time.sleep(0.895)
	tracef.write(f"474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 474kbit")
	time.sleep(0.921)
	tracef.write(f"565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 565kbit")
	time.sleep(0.871)
	tracef.write(f"829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 829kbit")
	time.sleep(0.895)
	tracef.write(f"1024 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1024kbit")
	time.sleep(0.884)
	tracef.write(f"555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 555kbit")
	time.sleep(0.874)
	tracef.write(f"713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 713kbit")
	time.sleep(0.929)
	tracef.write(f"252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 252kbit")
	time.sleep(0.9)
	tracef.write(f"674 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 674kbit")
	time.sleep(0.931)
	tracef.write(f"839 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 839kbit")
	time.sleep(0.891)
	tracef.write(f"667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 667kbit")
	time.sleep(0.867)
	tracef.write(f"264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 264kbit")
	time.sleep(0.907)
	tracef.write(f"665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 665kbit")
	time.sleep(0.919)
	tracef.write(f"956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 956kbit")
	time.sleep(0.921)
	tracef.write(f"179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 179kbit")
	time.sleep(0.933)
	tracef.write(f"180 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 180kbit")
	time.sleep(0.878)
	tracef.write(f"662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 662kbit")
	time.sleep(0.875)
	tracef.write(f"1026 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1026kbit")
	time.sleep(0.898)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.89)
	tracef.write(f"507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 507kbit")
	time.sleep(0.872)
	tracef.write(f"142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 142kbit")
	time.sleep(0.886)
	tracef.write(f"835 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 835kbit")
	time.sleep(0.921)
	tracef.write(f"1150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1150kbit")
	time.sleep(0.868)
	tracef.write(f"521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 521kbit")
	time.sleep(0.904)
	tracef.write(f"1135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1135kbit")
	time.sleep(0.89)
	tracef.write(f"230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 230kbit")
	time.sleep(0.925)
	tracef.write(f"319 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 319kbit")
	time.sleep(0.932)
	tracef.write(f"988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 988kbit")
	time.sleep(0.903)
	tracef.write(f"177 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 177kbit")
	time.sleep(0.923)
	tracef.write(f"705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 705kbit")
	time.sleep(0.88)
	tracef.write(f"745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 745kbit")
	time.sleep(0.867)
	tracef.write(f"375 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 375kbit")
	time.sleep(0.88)
	tracef.write(f"320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 320kbit")
	time.sleep(0.865)
	tracef.write(f"707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 707kbit")
	time.sleep(0.87)
	tracef.write(f"215 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 215kbit")
	time.sleep(0.868)
	tracef.write(f"881 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 881kbit")
	time.sleep(0.888)
	tracef.write(f"803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 803kbit")
	time.sleep(0.914)
	tracef.write(f"372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 372kbit")
	time.sleep(0.93)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(0.906)
	tracef.write(f"350 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 350kbit")
	time.sleep(0.88)
	tracef.write(f"863 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 863kbit")
	time.sleep(0.877)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(0.864)
	tracef.write(f"393 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 393kbit")
	time.sleep(0.873)
	tracef.write(f"567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 567kbit")
	time.sleep(0.863)
	tracef.write(f"673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 673kbit")
	time.sleep(0.874)
	tracef.write(f"811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 811kbit")
	time.sleep(0.911)
	tracef.write(f"186 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 186kbit")
	time.sleep(0.897)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.923)
	tracef.write(f"758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 758kbit")
	time.sleep(0.907)
	tracef.write(f"457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 457kbit")
	time.sleep(0.918)
	tracef.write(f"274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 274kbit")
	time.sleep(0.87)
	tracef.write(f"414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 414kbit")
	time.sleep(0.896)
	tracef.write(f"316 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 316kbit")
	time.sleep(0.88)
	tracef.write(f"926 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 926kbit")
	time.sleep(0.863)
	tracef.write(f"1004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1004kbit")
	time.sleep(0.899)
	tracef.write(f"660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 660kbit")
	time.sleep(0.883)
	tracef.write(f"1122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1122kbit")
	time.sleep(0.88)
	tracef.write(f"716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 716kbit")
	time.sleep(0.916)
	tracef.write(f"1093 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1093kbit")
	time.sleep(0.882)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()