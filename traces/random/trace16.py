#t:301-474 ; rate:134-174 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace16.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace16.txt", 'a+')
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 170kbit")
	time.sleep(0.369)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.462)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.34)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.393)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.413)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.372)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.359)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.454)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.411)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.336)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.402)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.404)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.351)
	tracef.write(f"146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 146kbit")
	time.sleep(0.351)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.455)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.474)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.399)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.309)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.411)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.347)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.462)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.42)
	tracef.write(f"164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 164kbit")
	time.sleep(0.308)
	tracef.write(f"163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 163kbit")
	time.sleep(0.421)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.39)
	tracef.write(f"135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 135kbit")
	time.sleep(0.416)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.398)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.446)
	tracef.write(f"156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 156kbit")
	time.sleep(0.433)
	tracef.write(f"141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 141kbit")
	time.sleep(0.322)
	tracef.write(f"153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 153kbit")
	time.sleep(0.329)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.439)
	tracef.write(f"164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 164kbit")
	time.sleep(0.428)
	tracef.write(f"172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 172kbit")
	time.sleep(0.455)
	tracef.write(f"172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 172kbit")
	time.sleep(0.432)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.442)
	tracef.write(f"165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 165kbit")
	time.sleep(0.326)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.443)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.411)
	tracef.write(f"141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 141kbit")
	time.sleep(0.474)
	tracef.write(f"153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 153kbit")
	time.sleep(0.401)
	tracef.write(f"146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 146kbit")
	time.sleep(0.382)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.398)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.424)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.303)
	tracef.write(f"144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 144kbit")
	time.sleep(0.399)
	tracef.write(f"151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 151kbit")
	time.sleep(0.423)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.405)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.331)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.463)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.422)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.388)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.407)
	tracef.write(f"146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 146kbit")
	time.sleep(0.369)
	tracef.write(f"171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 171kbit")
	time.sleep(0.342)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.377)
	tracef.write(f"164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 164kbit")
	time.sleep(0.35)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.397)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.415)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.372)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.33)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.351)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.361)
	tracef.write(f"156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 156kbit")
	time.sleep(0.451)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.368)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.398)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.418)
	tracef.write(f"142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 142kbit")
	time.sleep(0.441)
	tracef.write(f"165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 165kbit")
	time.sleep(0.457)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.364)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.376)
	tracef.write(f"143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 143kbit")
	time.sleep(0.471)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.385)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.327)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.35)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.372)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.385)
	tracef.write(f"142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 142kbit")
	time.sleep(0.316)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.322)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.443)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.394)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.342)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.365)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.424)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.449)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.439)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.426)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.329)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.374)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.375)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.306)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.382)
	tracef.write(f"141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 141kbit")
	time.sleep(0.446)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.333)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.316)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.328)
	tracef.write(f"135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 135kbit")
	time.sleep(0.381)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.421)
	tracef.write(f"165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 165kbit")
	time.sleep(0.429)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.438)
	tracef.write(f"165 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 165kbit")
	time.sleep(0.336)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.382)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.473)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.432)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.445)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.379)
	tracef.write(f"141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 141kbit")
	time.sleep(0.384)
	tracef.write(f"172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 172kbit")
	time.sleep(0.304)
	tracef.write(f"151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 151kbit")
	time.sleep(0.348)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.404)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.356)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.428)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.391)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.394)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.47)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.464)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.416)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.417)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.322)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.321)
	tracef.write(f"144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 144kbit")
	time.sleep(0.427)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.433)
	tracef.write(f"151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 151kbit")
	time.sleep(0.364)
	tracef.write(f"151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 151kbit")
	time.sleep(0.457)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.387)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.398)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.389)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.421)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.447)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.463)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.351)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.457)
	tracef.write(f"143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 143kbit")
	time.sleep(0.414)
	tracef.write(f"151 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 151kbit")
	time.sleep(0.44)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.451)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.416)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.47)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.344)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.353)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.368)
	tracef.write(f"164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 164kbit")
	time.sleep(0.391)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.407)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.41)
	tracef.write(f"146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 146kbit")
	time.sleep(0.341)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.344)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.339)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.421)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.435)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.324)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.432)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.397)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.457)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.357)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.447)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.316)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.464)
	tracef.write(f"172 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 172kbit")
	time.sleep(0.306)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.352)
	tracef.write(f"144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 144kbit")
	time.sleep(0.409)
	tracef.write(f"135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 135kbit")
	time.sleep(0.435)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.434)
	tracef.write(f"163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 163kbit")
	time.sleep(0.46)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.364)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.336)
	tracef.write(f"173 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 173kbit")
	time.sleep(0.301)
	tracef.write(f"158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 158kbit")
	time.sleep(0.468)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.454)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.389)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.325)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.423)
	tracef.write(f"163 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 163kbit")
	time.sleep(0.416)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.302)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.438)
	tracef.write(f"141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 141kbit")
	time.sleep(0.397)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.384)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.425)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.356)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.357)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.315)
	tracef.write(f"149 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 149kbit")
	time.sleep(0.421)
	tracef.write(f"153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 153kbit")
	time.sleep(0.398)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.332)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.31)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.472)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.426)
	tracef.write(f"160 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 160kbit")
	time.sleep(0.301)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.447)
	tracef.write(f"154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 154kbit")
	time.sleep(0.461)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.45)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.343)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.313)
	tracef.write(f"148 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 148kbit")
	time.sleep(0.382)
	tracef.write(f"144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 144kbit")
	time.sleep(0.365)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.354)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.301)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.383)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.362)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.366)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.374)
	tracef.write(f"144 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 144kbit")
	time.sleep(0.448)
	tracef.write(f"162 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 162kbit")
	time.sleep(0.303)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.439)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.327)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.348)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.421)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.439)
	tracef.write(f"159 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 159kbit")
	time.sleep(0.406)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.446)
	tracef.write(f"153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 153kbit")
	time.sleep(0.409)
	tracef.write(f"143 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 143kbit")
	time.sleep(0.351)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.374)
	tracef.write(f"142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 142kbit")
	time.sleep(0.311)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.417)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.313)
	tracef.write(f"138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 138kbit")
	time.sleep(0.403)
	tracef.write(f"171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 171kbit")
	time.sleep(0.407)
	tracef.write(f"155 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 155kbit")
	time.sleep(0.368)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.316)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.342)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.358)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.355)
	tracef.write(f"153 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 153kbit")
	time.sleep(0.313)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.343)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.403)
	tracef.write(f"164 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 164kbit")
	time.sleep(0.394)
	tracef.write(f"140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 140kbit")
	time.sleep(0.438)
	tracef.write(f"161 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 161kbit")
	time.sleep(0.472)
	tracef.write(f"135 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 135kbit")
	time.sleep(0.32)
	tracef.write(f"152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 152kbit")
	time.sleep(0.349)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.396)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.398)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.45)
	tracef.write(f"145 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 145kbit")
	time.sleep(0.381)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.361)
	tracef.write(f"169 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 169kbit")
	time.sleep(0.39)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.435)
	tracef.write(f"146 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 146kbit")
	time.sleep(0.38)
	tracef.write(f"158 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 158kbit")
	time.sleep(0.34)
	tracef.write(f"167 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 167kbit")
	time.sleep(0.451)
	tracef.write(f"137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 137kbit")
	time.sleep(0.411)
	tracef.write(f"157 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 157kbit")
	time.sleep(0.424)
	tracef.write(f"136 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 136kbit")
	time.sleep(0.326)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.445)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.446)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.335)
	tracef.write(f"170 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 170kbit")
	time.sleep(0.302)
	tracef.write(f"134 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 134kbit")
	time.sleep(0.392)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.341)
	tracef.write(f"139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 139kbit")
	time.sleep(0.374)
	tracef.write(f"152 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 152kbit")
	time.sleep(0.33)
	tracef.write(f"168 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 168kbit")
	time.sleep(0.346)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.417)
	tracef.write(f"150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 150kbit")
	time.sleep(0.457)
	tracef.write(f"142 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 142kbit")
	time.sleep(0.36)
	tracef.write(f"166 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 166kbit")
	time.sleep(0.33)
	tracef.write(f"171 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 171kbit")
	time.sleep(0.425)
	tracef.write(f"147 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 147kbit")
	time.sleep(0.401)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()