#t:68-856 ; rate:217-301 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace69.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace69.txt", 'a+')
	tracef.write(f"252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 252kbit")
	time.sleep(0.396)
	tracef.write(f"218 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 218kbit")
	time.sleep(0.343)
	tracef.write(f"286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 286kbit")
	time.sleep(0.348)
	tracef.write(f"259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 259kbit")
	time.sleep(0.278)
	tracef.write(f"243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 243kbit")
	time.sleep(0.33)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.395)
	tracef.write(f"240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 240kbit")
	time.sleep(0.27)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.64)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.742)
	tracef.write(f"238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 238kbit")
	time.sleep(0.337)
	tracef.write(f"247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 247kbit")
	time.sleep(0.286)
	tracef.write(f"285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 285kbit")
	time.sleep(0.414)
	tracef.write(f"288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 288kbit")
	time.sleep(0.262)
	tracef.write(f"232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 232kbit")
	time.sleep(0.787)
	tracef.write(f"219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 219kbit")
	time.sleep(0.694)
	tracef.write(f"293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 293kbit")
	time.sleep(0.837)
	tracef.write(f"248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 248kbit")
	time.sleep(0.243)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.276)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.406)
	tracef.write(f"287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 287kbit")
	time.sleep(0.661)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.25)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.264)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.786)
	tracef.write(f"221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 221kbit")
	time.sleep(0.449)
	tracef.write(f"300 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 300kbit")
	time.sleep(0.822)
	tracef.write(f"239 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 239kbit")
	time.sleep(0.769)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.148)
	tracef.write(f"253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 253kbit")
	time.sleep(0.261)
	tracef.write(f"250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 250kbit")
	time.sleep(0.244)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.584)
	tracef.write(f"261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 261kbit")
	time.sleep(0.569)
	tracef.write(f"223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 223kbit")
	time.sleep(0.794)
	tracef.write(f"283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 283kbit")
	time.sleep(0.667)
	tracef.write(f"267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 267kbit")
	time.sleep(0.109)
	tracef.write(f"296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 296kbit")
	time.sleep(0.178)
	tracef.write(f"248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 248kbit")
	time.sleep(0.438)
	tracef.write(f"251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 251kbit")
	time.sleep(0.434)
	tracef.write(f"269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 269kbit")
	time.sleep(0.142)
	tracef.write(f"266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 266kbit")
	time.sleep(0.496)
	tracef.write(f"225 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 225kbit")
	time.sleep(0.522)
	tracef.write(f"245 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 245kbit")
	time.sleep(0.553)
	tracef.write(f"266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 266kbit")
	time.sleep(0.171)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.399)
	tracef.write(f"247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 247kbit")
	time.sleep(0.532)
	tracef.write(f"221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 221kbit")
	time.sleep(0.602)
	tracef.write(f"268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 268kbit")
	time.sleep(0.647)
	tracef.write(f"267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 267kbit")
	time.sleep(0.227)
	tracef.write(f"218 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 218kbit")
	time.sleep(0.811)
	tracef.write(f"230 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 230kbit")
	time.sleep(0.143)
	tracef.write(f"226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 226kbit")
	time.sleep(0.691)
	tracef.write(f"229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 229kbit")
	time.sleep(0.249)
	tracef.write(f"223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 223kbit")
	time.sleep(0.185)
	tracef.write(f"232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 232kbit")
	time.sleep(0.573)
	tracef.write(f"217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 217kbit")
	time.sleep(0.635)
	tracef.write(f"252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 252kbit")
	time.sleep(0.76)
	tracef.write(f"219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 219kbit")
	time.sleep(0.829)
	tracef.write(f"288 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 288kbit")
	time.sleep(0.246)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.557)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.245)
	tracef.write(f"287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 287kbit")
	time.sleep(0.591)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.412)
	tracef.write(f"287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 287kbit")
	time.sleep(0.54)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.726)
	tracef.write(f"279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 279kbit")
	time.sleep(0.36)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.091)
	tracef.write(f"252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 252kbit")
	time.sleep(0.145)
	tracef.write(f"220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 220kbit")
	time.sleep(0.092)
	tracef.write(f"246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 246kbit")
	time.sleep(0.692)
	tracef.write(f"251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 251kbit")
	time.sleep(0.248)
	tracef.write(f"271 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 271kbit")
	time.sleep(0.617)
	tracef.write(f"271 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 271kbit")
	time.sleep(0.642)
	tracef.write(f"252 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 252kbit")
	time.sleep(0.805)
	tracef.write(f"282 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 282kbit")
	time.sleep(0.508)
	tracef.write(f"289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 289kbit")
	time.sleep(0.755)
	tracef.write(f"281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 281kbit")
	time.sleep(0.282)
	tracef.write(f"274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 274kbit")
	time.sleep(0.643)
	tracef.write(f"263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 263kbit")
	time.sleep(0.36)
	tracef.write(f"234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 234kbit")
	time.sleep(0.35)
	tracef.write(f"226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 226kbit")
	time.sleep(0.112)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.239)
	tracef.write(f"243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 243kbit")
	time.sleep(0.473)
	tracef.write(f"279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 279kbit")
	time.sleep(0.749)
	tracef.write(f"222 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 222kbit")
	time.sleep(0.073)
	tracef.write(f"253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 253kbit")
	time.sleep(0.727)
	tracef.write(f"263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 263kbit")
	time.sleep(0.235)
	tracef.write(f"259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 259kbit")
	time.sleep(0.128)
	tracef.write(f"227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 227kbit")
	time.sleep(0.239)
	tracef.write(f"221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 221kbit")
	time.sleep(0.127)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.286)
	tracef.write(f"297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 297kbit")
	time.sleep(0.48)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.671)
	tracef.write(f"238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 238kbit")
	time.sleep(0.583)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.219)
	tracef.write(f"259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 259kbit")
	time.sleep(0.078)
	tracef.write(f"234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 234kbit")
	time.sleep(0.837)
	tracef.write(f"274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 274kbit")
	time.sleep(0.662)
	tracef.write(f"248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 248kbit")
	time.sleep(0.783)
	tracef.write(f"265 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 265kbit")
	time.sleep(0.105)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.631)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.558)
	tracef.write(f"282 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 282kbit")
	time.sleep(0.194)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.677)
	tracef.write(f"236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 236kbit")
	time.sleep(0.388)
	tracef.write(f"239 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 239kbit")
	time.sleep(0.6)
	tracef.write(f"239 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 239kbit")
	time.sleep(0.092)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.639)
	tracef.write(f"220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 220kbit")
	time.sleep(0.209)
	tracef.write(f"259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 259kbit")
	time.sleep(0.197)
	tracef.write(f"236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 236kbit")
	time.sleep(0.698)
	tracef.write(f"276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 276kbit")
	time.sleep(0.574)
	tracef.write(f"220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 220kbit")
	time.sleep(0.782)
	tracef.write(f"241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 241kbit")
	time.sleep(0.439)
	tracef.write(f"232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 232kbit")
	time.sleep(0.355)
	tracef.write(f"260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 260kbit")
	time.sleep(0.196)
	tracef.write(f"266 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 266kbit")
	time.sleep(0.813)
	tracef.write(f"217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 217kbit")
	time.sleep(0.824)
	tracef.write(f"217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 217kbit")
	time.sleep(0.351)
	tracef.write(f"248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 248kbit")
	time.sleep(0.651)
	tracef.write(f"218 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 218kbit")
	time.sleep(0.634)
	tracef.write(f"235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 235kbit")
	time.sleep(0.566)
	tracef.write(f"218 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 218kbit")
	time.sleep(0.84)
	tracef.write(f"253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 253kbit")
	time.sleep(0.268)
	tracef.write(f"259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 259kbit")
	time.sleep(0.282)
	tracef.write(f"269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 269kbit")
	time.sleep(0.464)
	tracef.write(f"268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 268kbit")
	time.sleep(0.709)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.703)
	tracef.write(f"254 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 254kbit")
	time.sleep(0.644)
	tracef.write(f"240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 240kbit")
	time.sleep(0.675)
	tracef.write(f"224 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 224kbit")
	time.sleep(0.679)
	tracef.write(f"238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 238kbit")
	time.sleep(0.78)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.703)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.543)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.23)
	tracef.write(f"233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 233kbit")
	time.sleep(0.344)
	tracef.write(f"260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 260kbit")
	time.sleep(0.113)
	tracef.write(f"220 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 220kbit")
	time.sleep(0.832)
	tracef.write(f"285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 285kbit")
	time.sleep(0.655)
	tracef.write(f"289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 289kbit")
	time.sleep(0.653)
	tracef.write(f"244 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 244kbit")
	time.sleep(0.738)
	tracef.write(f"267 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 267kbit")
	time.sleep(0.14)
	tracef.write(f"238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 238kbit")
	time.sleep(0.136)
	tracef.write(f"285 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 285kbit")
	time.sleep(0.286)
	tracef.write(f"226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 226kbit")
	time.sleep(0.627)
	tracef.write(f"258 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 258kbit")
	time.sleep(0.385)
	tracef.write(f"250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 250kbit")
	time.sleep(0.235)
	tracef.write(f"260 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 260kbit")
	time.sleep(0.668)
	tracef.write(f"256 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 256kbit")
	time.sleep(0.842)
	tracef.write(f"263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 263kbit")
	time.sleep(0.137)
	tracef.write(f"250 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 250kbit")
	time.sleep(0.186)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.85)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.796)
	tracef.write(f"218 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 218kbit")
	time.sleep(0.699)
	tracef.write(f"261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 261kbit")
	time.sleep(0.441)
	tracef.write(f"292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 292kbit")
	time.sleep(0.097)
	tracef.write(f"229 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 229kbit")
	time.sleep(0.103)
	tracef.write(f"241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 241kbit")
	time.sleep(0.618)
	tracef.write(f"276 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 276kbit")
	time.sleep(0.436)
	tracef.write(f"270 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 270kbit")
	time.sleep(0.477)
	tracef.write(f"217 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 217kbit")
	time.sleep(0.182)
	tracef.write(f"219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 219kbit")
	time.sleep(0.305)
	tracef.write(f"223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 223kbit")
	time.sleep(0.685)
	tracef.write(f"251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 251kbit")
	time.sleep(0.196)
	tracef.write(f"235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 235kbit")
	time.sleep(0.245)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.109)
	tracef.write(f"283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 283kbit")
	time.sleep(0.294)
	tracef.write(f"296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 296kbit")
	time.sleep(0.758)
	tracef.write(f"249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 249kbit")
	time.sleep(0.839)
	tracef.write(f"281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 281kbit")
	time.sleep(0.731)
	tracef.write(f"273 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 273kbit")
	time.sleep(0.668)
	tracef.write(f"299 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 299kbit")
	time.sleep(0.348)
	tracef.write(f"219 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 219kbit")
	time.sleep(0.338)
	tracef.write(f"234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 234kbit")
	time.sleep(0.127)
	tracef.write(f"261 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 261kbit")
	time.sleep(0.679)
	tracef.write(f"240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 240kbit")
	time.sleep(0.683)
	tracef.write(f"287 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 287kbit")
	time.sleep(0.173)
	tracef.write(f"227 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 227kbit")
	time.sleep(0.546)
	tracef.write(f"246 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 246kbit")
	time.sleep(0.792)
	tracef.write(f"251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 251kbit")
	time.sleep(0.431)
	tracef.write(f"275 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 275kbit")
	time.sleep(0.571)
	tracef.write(f"241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 241kbit")
	time.sleep(0.627)
	tracef.write(f"272 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 272kbit")
	time.sleep(0.725)
	tracef.write(f"277 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 277kbit")
	time.sleep(0.139)
	tracef.write(f"278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 278kbit")
	time.sleep(0.717)
	tracef.write(f"268 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 268kbit")
	time.sleep(0.325)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.361)
	tracef.write(f"296 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 296kbit")
	time.sleep(0.672)
	tracef.write(f"263 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 263kbit")
	time.sleep(0.768)
	tracef.write(f"248 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 248kbit")
	time.sleep(0.829)
	tracef.write(f"269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 269kbit")
	time.sleep(0.238)
	tracef.write(f"262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 262kbit")
	time.sleep(0.301)
	tracef.write(f"235 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 235kbit")
	time.sleep(0.758)
	tracef.write(f"241 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 241kbit")
	time.sleep(0.148)
	tracef.write(f"294 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 294kbit")
	time.sleep(0.315)
	tracef.write(f"240 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 240kbit")
	time.sleep(0.558)
	tracef.write(f"293 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 293kbit")
	time.sleep(0.617)
	tracef.write(f"284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 284kbit")
	time.sleep(0.356)
	tracef.write(f"286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 286kbit")
	time.sleep(0.738)
	tracef.write(f"284 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 284kbit")
	time.sleep(0.443)
	tracef.write(f"278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 278kbit")
	time.sleep(0.848)
	tracef.write(f"300 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 300kbit")
	time.sleep(0.711)
	tracef.write(f"231 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 231kbit")
	time.sleep(0.178)
	tracef.write(f"243 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 243kbit")
	time.sleep(0.47)
	tracef.write(f"269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 269kbit")
	time.sleep(0.469)
	tracef.write(f"278 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 278kbit")
	time.sleep(0.643)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.335)
	tracef.write(f"269 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 269kbit")
	time.sleep(0.331)
	tracef.write(f"232 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 232kbit")
	time.sleep(0.323)
	tracef.write(f"289 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 289kbit")
	time.sleep(0.556)
	tracef.write(f"262 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 262kbit")
	time.sleep(0.446)
	tracef.write(f"226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 226kbit")
	time.sleep(0.56)
	tracef.write(f"226 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 226kbit")
	time.sleep(0.109)
	tracef.write(f"233 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 233kbit")
	time.sleep(0.706)
	tracef.write(f"237 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 237kbit")
	time.sleep(0.666)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()