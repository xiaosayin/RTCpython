#t:448-712 ; rate:1791-2403 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace208.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace208.txt", 'a+')
	tracef.write(f"2381 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2381kbit")
	time.sleep(0.659)
	tracef.write(f"2320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2320kbit")
	time.sleep(0.568)
	tracef.write(f"2279 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2279kbit")
	time.sleep(0.65)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.627)
	tracef.write(f"2388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2388kbit")
	time.sleep(0.574)
	tracef.write(f"1942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1942kbit")
	time.sleep(0.553)
	tracef.write(f"1804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1804kbit")
	time.sleep(0.61)
	tracef.write(f"1918 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1918kbit")
	time.sleep(0.543)
	tracef.write(f"1961 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1961kbit")
	time.sleep(0.519)
	tracef.write(f"2122 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2122kbit")
	time.sleep(0.689)
	tracef.write(f"1803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1803kbit")
	time.sleep(0.495)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.462)
	tracef.write(f"2130 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2130kbit")
	time.sleep(0.55)
	tracef.write(f"1965 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1965kbit")
	time.sleep(0.603)
	tracef.write(f"2251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2251kbit")
	time.sleep(0.669)
	tracef.write(f"1975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1975kbit")
	time.sleep(0.709)
	tracef.write(f"2140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2140kbit")
	time.sleep(0.613)
	tracef.write(f"2371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2371kbit")
	time.sleep(0.598)
	tracef.write(f"2336 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2336kbit")
	time.sleep(0.599)
	tracef.write(f"2041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2041kbit")
	time.sleep(0.675)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.711)
	tracef.write(f"2314 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2314kbit")
	time.sleep(0.648)
	tracef.write(f"2089 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2089kbit")
	time.sleep(0.621)
	tracef.write(f"2249 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2249kbit")
	time.sleep(0.619)
	tracef.write(f"2317 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2317kbit")
	time.sleep(0.537)
	tracef.write(f"2304 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2304kbit")
	time.sleep(0.655)
	tracef.write(f"1985 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1985kbit")
	time.sleep(0.677)
	tracef.write(f"1935 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1935kbit")
	time.sleep(0.486)
	tracef.write(f"2223 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2223kbit")
	time.sleep(0.663)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.674)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.488)
	tracef.write(f"1899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1899kbit")
	time.sleep(0.553)
	tracef.write(f"2345 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2345kbit")
	time.sleep(0.488)
	tracef.write(f"2068 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2068kbit")
	time.sleep(0.526)
	tracef.write(f"1861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1861kbit")
	time.sleep(0.512)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.706)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.694)
	tracef.write(f"2016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2016kbit")
	time.sleep(0.494)
	tracef.write(f"1974 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1974kbit")
	time.sleep(0.593)
	tracef.write(f"2362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2362kbit")
	time.sleep(0.628)
	tracef.write(f"2356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2356kbit")
	time.sleep(0.549)
	tracef.write(f"1937 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1937kbit")
	time.sleep(0.686)
	tracef.write(f"1841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1841kbit")
	time.sleep(0.608)
	tracef.write(f"2259 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2259kbit")
	time.sleep(0.669)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.666)
	tracef.write(f"2118 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2118kbit")
	time.sleep(0.542)
	tracef.write(f"2388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2388kbit")
	time.sleep(0.585)
	tracef.write(f"2138 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2138kbit")
	time.sleep(0.641)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.645)
	tracef.write(f"1958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1958kbit")
	time.sleep(0.626)
	tracef.write(f"1991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1991kbit")
	time.sleep(0.651)
	tracef.write(f"1920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1920kbit")
	time.sleep(0.598)
	tracef.write(f"2320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2320kbit")
	time.sleep(0.698)
	tracef.write(f"2156 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2156kbit")
	time.sleep(0.641)
	tracef.write(f"1913 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1913kbit")
	time.sleep(0.464)
	tracef.write(f"2211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2211kbit")
	time.sleep(0.589)
	tracef.write(f"2131 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2131kbit")
	time.sleep(0.606)
	tracef.write(f"2238 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2238kbit")
	time.sleep(0.62)
	tracef.write(f"2103 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2103kbit")
	time.sleep(0.701)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.448)
	tracef.write(f"2001 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2001kbit")
	time.sleep(0.695)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.626)
	tracef.write(f"1882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1882kbit")
	time.sleep(0.57)
	tracef.write(f"2292 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2292kbit")
	time.sleep(0.642)
	tracef.write(f"2207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2207kbit")
	time.sleep(0.519)
	tracef.write(f"1884 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1884kbit")
	time.sleep(0.698)
	tracef.write(f"2179 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2179kbit")
	time.sleep(0.56)
	tracef.write(f"1894 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1894kbit")
	time.sleep(0.477)
	tracef.write(f"2325 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2325kbit")
	time.sleep(0.693)
	tracef.write(f"2352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2352kbit")
	time.sleep(0.614)
	tracef.write(f"2360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2360kbit")
	time.sleep(0.605)
	tracef.write(f"1982 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1982kbit")
	time.sleep(0.543)
	tracef.write(f"2221 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2221kbit")
	time.sleep(0.625)
	tracef.write(f"2203 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2203kbit")
	time.sleep(0.572)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.556)
	tracef.write(f"2380 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2380kbit")
	time.sleep(0.659)
	tracef.write(f"2194 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2194kbit")
	time.sleep(0.64)
	tracef.write(f"2100 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2100kbit")
	time.sleep(0.462)
	tracef.write(f"1895 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1895kbit")
	time.sleep(0.472)
	tracef.write(f"2298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2298kbit")
	time.sleep(0.522)
	tracef.write(f"2141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2141kbit")
	time.sleep(0.499)
	tracef.write(f"2038 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2038kbit")
	time.sleep(0.615)
	tracef.write(f"2039 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2039kbit")
	time.sleep(0.467)
	tracef.write(f"2273 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2273kbit")
	time.sleep(0.546)
	tracef.write(f"1934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1934kbit")
	time.sleep(0.647)
	tracef.write(f"2320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2320kbit")
	time.sleep(0.581)
	tracef.write(f"2274 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2274kbit")
	time.sleep(0.659)
	tracef.write(f"2210 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2210kbit")
	time.sleep(0.535)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.449)
	tracef.write(f"2021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2021kbit")
	time.sleep(0.538)
	tracef.write(f"2347 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2347kbit")
	time.sleep(0.514)
	tracef.write(f"1827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1827kbit")
	time.sleep(0.487)
	tracef.write(f"2251 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2251kbit")
	time.sleep(0.558)
	tracef.write(f"2098 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2098kbit")
	time.sleep(0.655)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.647)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.621)
	tracef.write(f"2085 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2085kbit")
	time.sleep(0.68)
	tracef.write(f"1918 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1918kbit")
	time.sleep(0.489)
	tracef.write(f"2257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2257kbit")
	time.sleep(0.622)
	tracef.write(f"1851 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1851kbit")
	time.sleep(0.524)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.684)
	tracef.write(f"1909 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1909kbit")
	time.sleep(0.637)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.554)
	tracef.write(f"2247 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2247kbit")
	time.sleep(0.61)
	tracef.write(f"2253 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2253kbit")
	time.sleep(0.619)
	tracef.write(f"1810 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1810kbit")
	time.sleep(0.708)
	tracef.write(f"1811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1811kbit")
	time.sleep(0.482)
	tracef.write(f"2257 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2257kbit")
	time.sleep(0.466)
	tracef.write(f"2234 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2234kbit")
	time.sleep(0.69)
	tracef.write(f"1795 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1795kbit")
	time.sleep(0.512)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.541)
	tracef.write(f"1919 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1919kbit")
	time.sleep(0.592)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.511)
	tracef.write(f"1826 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1826kbit")
	time.sleep(0.532)
	tracef.write(f"2043 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2043kbit")
	time.sleep(0.458)
	tracef.write(f"1996 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1996kbit")
	time.sleep(0.527)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.642)
	tracef.write(f"2331 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2331kbit")
	time.sleep(0.551)
	tracef.write(f"1958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1958kbit")
	time.sleep(0.601)
	tracef.write(f"2059 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2059kbit")
	time.sleep(0.462)
	tracef.write(f"1840 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1840kbit")
	time.sleep(0.659)
	tracef.write(f"1945 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1945kbit")
	time.sleep(0.702)
	tracef.write(f"2242 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2242kbit")
	time.sleep(0.478)
	tracef.write(f"2366 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2366kbit")
	time.sleep(0.637)
	tracef.write(f"2186 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2186kbit")
	time.sleep(0.494)
	tracef.write(f"2343 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2343kbit")
	time.sleep(0.63)
	tracef.write(f"2189 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2189kbit")
	time.sleep(0.614)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.573)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.548)
	tracef.write(f"1822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1822kbit")
	time.sleep(0.69)
	tracef.write(f"2099 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2099kbit")
	time.sleep(0.49)
	tracef.write(f"2000 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2000kbit")
	time.sleep(0.615)
	tracef.write(f"1966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1966kbit")
	time.sleep(0.586)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.555)
	tracef.write(f"1922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1922kbit")
	time.sleep(0.523)
	tracef.write(f"1856 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1856kbit")
	time.sleep(0.549)
	tracef.write(f"1894 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1894kbit")
	time.sleep(0.699)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.673)
	tracef.write(f"2382 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2382kbit")
	time.sleep(0.483)
	tracef.write(f"2297 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2297kbit")
	time.sleep(0.462)
	tracef.write(f"2328 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2328kbit")
	time.sleep(0.68)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.695)
	tracef.write(f"2021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2021kbit")
	time.sleep(0.492)
	tracef.write(f"1824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1824kbit")
	time.sleep(0.465)
	tracef.write(f"2112 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2112kbit")
	time.sleep(0.478)
	tracef.write(f"2074 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2074kbit")
	time.sleep(0.512)
	tracef.write(f"2196 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2196kbit")
	time.sleep(0.643)
	tracef.write(f"2042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2042kbit")
	time.sleep(0.466)
	tracef.write(f"2207 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2207kbit")
	time.sleep(0.683)
	tracef.write(f"2118 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2118kbit")
	time.sleep(0.561)
	tracef.write(f"1894 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1894kbit")
	time.sleep(0.551)
	tracef.write(f"2213 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2213kbit")
	time.sleep(0.471)
	tracef.write(f"2369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2369kbit")
	time.sleep(0.6)
	tracef.write(f"2141 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2141kbit")
	time.sleep(0.463)
	tracef.write(f"1923 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1923kbit")
	time.sleep(0.707)
	tracef.write(f"2137 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2137kbit")
	time.sleep(0.541)
	tracef.write(f"1948 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1948kbit")
	time.sleep(0.501)
	tracef.write(f"1959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1959kbit")
	time.sleep(0.626)
	tracef.write(f"2236 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2236kbit")
	time.sleep(0.617)
	tracef.write(f"2214 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2214kbit")
	time.sleep(0.504)
	tracef.write(f"2188 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2188kbit")
	time.sleep(0.575)
	tracef.write(f"1988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1988kbit")
	time.sleep(0.555)
	tracef.write(f"2211 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2211kbit")
	time.sleep(0.594)
	tracef.write(f"2105 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2105kbit")
	time.sleep(0.649)
	tracef.write(f"2150 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2150kbit")
	time.sleep(0.492)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.694)
	tracef.write(f"2329 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2329kbit")
	time.sleep(0.525)
	tracef.write(f"1836 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1836kbit")
	time.sleep(0.545)
	tracef.write(f"2045 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2045kbit")
	time.sleep(0.656)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.511)
	tracef.write(f"2228 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2228kbit")
	time.sleep(0.528)
	tracef.write(f"2108 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2108kbit")
	time.sleep(0.673)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()