#t:802-990 ; rate:854-2646 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace169.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace169.txt", 'a+')
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1613kbit")
	time.sleep(0.897)
	tracef.write(f"1825 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1825kbit")
	time.sleep(0.903)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.953)
	tracef.write(f"1138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1138kbit")
	time.sleep(0.888)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(0.814)
	tracef.write(f"1515 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1515kbit")
	time.sleep(0.862)
	tracef.write(f"999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 999kbit")
	time.sleep(0.802)
	tracef.write(f"2081 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2081kbit")
	time.sleep(0.974)
	tracef.write(f"1411 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1411kbit")
	time.sleep(0.806)
	tracef.write(f"2094 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2094kbit")
	time.sleep(0.923)
	tracef.write(f"1335 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1335kbit")
	time.sleep(0.864)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.93)
	tracef.write(f"1697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1697kbit")
	time.sleep(0.957)
	tracef.write(f"2275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2275kbit")
	time.sleep(0.968)
	tracef.write(f"2256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2256kbit")
	time.sleep(0.805)
	tracef.write(f"1262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1262kbit")
	time.sleep(0.88)
	tracef.write(f"1015 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1015kbit")
	time.sleep(0.935)
	tracef.write(f"1730 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1730kbit")
	time.sleep(0.916)
	tracef.write(f"1264 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1264kbit")
	time.sleep(0.889)
	tracef.write(f"2323 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2323kbit")
	time.sleep(0.843)
	tracef.write(f"1194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1194kbit")
	time.sleep(0.99)
	tracef.write(f"867 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 867kbit")
	time.sleep(0.942)
	tracef.write(f"1663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1663kbit")
	time.sleep(0.972)
	tracef.write(f"2243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2243kbit")
	time.sleep(0.886)
	tracef.write(f"2293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2293kbit")
	time.sleep(0.867)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(0.938)
	tracef.write(f"1847 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1847kbit")
	time.sleep(0.936)
	tracef.write(f"889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 889kbit")
	time.sleep(0.849)
	tracef.write(f"2061 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2061kbit")
	time.sleep(0.806)
	tracef.write(f"1864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1864kbit")
	time.sleep(0.823)
	tracef.write(f"1782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1782kbit")
	time.sleep(0.834)
	tracef.write(f"1959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1959kbit")
	time.sleep(0.882)
	tracef.write(f"2150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2150kbit")
	time.sleep(0.895)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(0.932)
	tracef.write(f"2595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2595kbit")
	time.sleep(0.973)
	tracef.write(f"1604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1604kbit")
	time.sleep(0.955)
	tracef.write(f"2474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2474kbit")
	time.sleep(0.809)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.9)
	tracef.write(f"2192 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2192kbit")
	time.sleep(0.929)
	tracef.write(f"2318 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2318kbit")
	time.sleep(0.833)
	tracef.write(f"2413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2413kbit")
	time.sleep(0.806)
	tracef.write(f"1688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1688kbit")
	time.sleep(0.843)
	tracef.write(f"2240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2240kbit")
	time.sleep(0.808)
	tracef.write(f"1866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1866kbit")
	time.sleep(0.913)
	tracef.write(f"1160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1160kbit")
	time.sleep(0.937)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.86)
	tracef.write(f"1765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1765kbit")
	time.sleep(0.856)
	tracef.write(f"1283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1283kbit")
	time.sleep(0.871)
	tracef.write(f"1065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1065kbit")
	time.sleep(0.818)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(0.805)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.885)
	tracef.write(f"2079 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2079kbit")
	time.sleep(0.933)
	tracef.write(f"2567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2567kbit")
	time.sleep(0.981)
	tracef.write(f"1833 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1833kbit")
	time.sleep(0.803)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.975)
	tracef.write(f"1353 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1353kbit")
	time.sleep(0.931)
	tracef.write(f"1902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1902kbit")
	time.sleep(0.832)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.917)
	tracef.write(f"2346 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2346kbit")
	time.sleep(0.806)
	tracef.write(f"1030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1030kbit")
	time.sleep(0.935)
	tracef.write(f"2229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2229kbit")
	time.sleep(0.825)
	tracef.write(f"993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 993kbit")
	time.sleep(0.859)
	tracef.write(f"2303 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2303kbit")
	time.sleep(0.859)
	tracef.write(f"2344 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2344kbit")
	time.sleep(0.837)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.89)
	tracef.write(f"2453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2453kbit")
	time.sleep(0.894)
	tracef.write(f"1666 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1666kbit")
	time.sleep(0.966)
	tracef.write(f"2542 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2542kbit")
	time.sleep(0.908)
	tracef.write(f"1822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1822kbit")
	time.sleep(0.949)
	tracef.write(f"2004 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2004kbit")
	time.sleep(0.925)
	tracef.write(f"1661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1661kbit")
	time.sleep(0.948)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(0.869)
	tracef.write(f"908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 908kbit")
	time.sleep(0.836)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.92)
	tracef.write(f"1107 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1107kbit")
	time.sleep(0.972)
	tracef.write(f"2181 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2181kbit")
	time.sleep(0.829)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.804)
	tracef.write(f"1866 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1866kbit")
	time.sleep(0.812)
	tracef.write(f"1330 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1330kbit")
	time.sleep(0.969)
	tracef.write(f"2189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2189kbit")
	time.sleep(0.844)
	tracef.write(f"945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 945kbit")
	time.sleep(0.902)
	tracef.write(f"2351 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2351kbit")
	time.sleep(0.904)
	tracef.write(f"2185 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2185kbit")
	time.sleep(0.807)
	tracef.write(f"2057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2057kbit")
	time.sleep(0.961)
	tracef.write(f"2110 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2110kbit")
	time.sleep(0.986)
	tracef.write(f"1101 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1101kbit")
	time.sleep(0.963)
	tracef.write(f"2592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2592kbit")
	time.sleep(0.856)
	tracef.write(f"2204 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2204kbit")
	time.sleep(0.88)
	tracef.write(f"1196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1196kbit")
	time.sleep(0.934)
	tracef.write(f"894 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 894kbit")
	time.sleep(0.913)
	tracef.write(f"2143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2143kbit")
	time.sleep(0.811)
	tracef.write(f"2627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2627kbit")
	time.sleep(0.971)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.85)
	tracef.write(f"948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 948kbit")
	time.sleep(0.877)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.957)
	tracef.write(f"1380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1380kbit")
	time.sleep(0.85)
	tracef.write(f"1248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1248kbit")
	time.sleep(0.844)
	tracef.write(f"1480 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1480kbit")
	time.sleep(0.817)
	tracef.write(f"1902 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1902kbit")
	time.sleep(0.964)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.99)
	tracef.write(f"2222 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2222kbit")
	time.sleep(0.941)
	tracef.write(f"1081 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1081kbit")
	time.sleep(0.988)
	tracef.write(f"2586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2586kbit")
	time.sleep(0.846)
	tracef.write(f"1712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1712kbit")
	time.sleep(0.91)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.863)
	tracef.write(f"1136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1136kbit")
	time.sleep(0.803)
	tracef.write(f"2250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2250kbit")
	time.sleep(0.883)
	tracef.write(f"2436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2436kbit")
	time.sleep(0.925)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.821)
	tracef.write(f"1141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1141kbit")
	time.sleep(0.943)
	tracef.write(f"991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 991kbit")
	time.sleep(0.948)
	tracef.write(f"1080 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1080kbit")
	time.sleep(0.888)
	tracef.write(f"1317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1317kbit")
	time.sleep(0.877)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()