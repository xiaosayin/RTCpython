#t:280-874 ; rate:1783-2023 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace302.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace302.txt", 'a+')
	tracef.write(f"1816 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1816kbit")
	time.sleep(0.359)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.769)
	tracef.write(f"1959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1959kbit")
	time.sleep(0.368)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.341)
	tracef.write(f"1883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1883kbit")
	time.sleep(0.317)
	tracef.write(f"1914 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1914kbit")
	time.sleep(0.281)
	tracef.write(f"1798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1798kbit")
	time.sleep(0.467)
	tracef.write(f"1843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1843kbit")
	time.sleep(0.431)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.797)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.74)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.821)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.455)
	tracef.write(f"1901 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1901kbit")
	time.sleep(0.545)
	tracef.write(f"1862 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1862kbit")
	time.sleep(0.525)
	tracef.write(f"1904 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1904kbit")
	time.sleep(0.525)
	tracef.write(f"1858 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1858kbit")
	time.sleep(0.786)
	tracef.write(f"1794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1794kbit")
	time.sleep(0.734)
	tracef.write(f"1946 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1946kbit")
	time.sleep(0.788)
	tracef.write(f"1932 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1932kbit")
	time.sleep(0.642)
	tracef.write(f"1954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1954kbit")
	time.sleep(0.467)
	tracef.write(f"1826 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1826kbit")
	time.sleep(0.554)
	tracef.write(f"1882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1882kbit")
	time.sleep(0.763)
	tracef.write(f"1939 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1939kbit")
	time.sleep(0.352)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.605)
	tracef.write(f"1883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1883kbit")
	time.sleep(0.756)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.438)
	tracef.write(f"1947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1947kbit")
	time.sleep(0.648)
	tracef.write(f"1927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1927kbit")
	time.sleep(0.409)
	tracef.write(f"1831 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1831kbit")
	time.sleep(0.814)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.554)
	tracef.write(f"2002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2002kbit")
	time.sleep(0.336)
	tracef.write(f"2022 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2022kbit")
	time.sleep(0.699)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.837)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.504)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.555)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.795)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.75)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.432)
	tracef.write(f"1841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1841kbit")
	time.sleep(0.87)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.645)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.603)
	tracef.write(f"1798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1798kbit")
	time.sleep(0.365)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.334)
	tracef.write(f"1797 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1797kbit")
	time.sleep(0.691)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.616)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.528)
	tracef.write(f"1857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1857kbit")
	time.sleep(0.364)
	tracef.write(f"2016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2016kbit")
	time.sleep(0.812)
	tracef.write(f"1833 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1833kbit")
	time.sleep(0.301)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.466)
	tracef.write(f"1943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1943kbit")
	time.sleep(0.405)
	tracef.write(f"1824 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1824kbit")
	time.sleep(0.347)
	tracef.write(f"1928 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1928kbit")
	time.sleep(0.372)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.615)
	tracef.write(f"1844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1844kbit")
	time.sleep(0.657)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.814)
	tracef.write(f"1813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1813kbit")
	time.sleep(0.526)
	tracef.write(f"1950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1950kbit")
	time.sleep(0.413)
	tracef.write(f"1854 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1854kbit")
	time.sleep(0.678)
	tracef.write(f"1904 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1904kbit")
	time.sleep(0.32)
	tracef.write(f"1846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1846kbit")
	time.sleep(0.438)
	tracef.write(f"1864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1864kbit")
	time.sleep(0.423)
	tracef.write(f"1843 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1843kbit")
	time.sleep(0.291)
	tracef.write(f"1833 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1833kbit")
	time.sleep(0.748)
	tracef.write(f"1967 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1967kbit")
	time.sleep(0.576)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.511)
	tracef.write(f"1940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1940kbit")
	time.sleep(0.318)
	tracef.write(f"1857 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1857kbit")
	time.sleep(0.694)
	tracef.write(f"1943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1943kbit")
	time.sleep(0.287)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.457)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.675)
	tracef.write(f"1986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1986kbit")
	time.sleep(0.335)
	tracef.write(f"1980 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1980kbit")
	time.sleep(0.514)
	tracef.write(f"1790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1790kbit")
	time.sleep(0.834)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.694)
	tracef.write(f"1940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1940kbit")
	time.sleep(0.465)
	tracef.write(f"1897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1897kbit")
	time.sleep(0.628)
	tracef.write(f"1934 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1934kbit")
	time.sleep(0.747)
	tracef.write(f"2021 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2021kbit")
	time.sleep(0.518)
	tracef.write(f"1883 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1883kbit")
	time.sleep(0.529)
	tracef.write(f"1870 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1870kbit")
	time.sleep(0.716)
	tracef.write(f"1788 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1788kbit")
	time.sleep(0.599)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.71)
	tracef.write(f"2011 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2011kbit")
	time.sleep(0.69)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.323)
	tracef.write(f"1966 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1966kbit")
	time.sleep(0.454)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.673)
	tracef.write(f"1806 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1806kbit")
	time.sleep(0.871)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.545)
	tracef.write(f"1803 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1803kbit")
	time.sleep(0.719)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.833)
	tracef.write(f"2008 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2008kbit")
	time.sleep(0.614)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.662)
	tracef.write(f"1962 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1962kbit")
	time.sleep(0.754)
	tracef.write(f"2018 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2018kbit")
	time.sleep(0.509)
	tracef.write(f"1926 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1926kbit")
	time.sleep(0.545)
	tracef.write(f"1955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1955kbit")
	time.sleep(0.386)
	tracef.write(f"1786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1786kbit")
	time.sleep(0.38)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.574)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.542)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.86)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.463)
	tracef.write(f"1850 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1850kbit")
	time.sleep(0.386)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.342)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.69)
	tracef.write(f"1853 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1853kbit")
	time.sleep(0.416)
	tracef.write(f"1813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1813kbit")
	time.sleep(0.557)
	tracef.write(f"1818 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1818kbit")
	time.sleep(0.748)
	tracef.write(f"1977 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1977kbit")
	time.sleep(0.798)
	tracef.write(f"1827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1827kbit")
	time.sleep(0.318)
	tracef.write(f"1848 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1848kbit")
	time.sleep(0.67)
	tracef.write(f"1993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1993kbit")
	time.sleep(0.697)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.484)
	tracef.write(f"1928 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1928kbit")
	time.sleep(0.392)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.542)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.478)
	tracef.write(f"1844 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1844kbit")
	time.sleep(0.634)
	tracef.write(f"1852 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1852kbit")
	time.sleep(0.494)
	tracef.write(f"2005 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2005kbit")
	time.sleep(0.555)
	tracef.write(f"1881 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1881kbit")
	time.sleep(0.571)
	tracef.write(f"1872 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1872kbit")
	time.sleep(0.721)
	tracef.write(f"1793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1793kbit")
	time.sleep(0.645)
	tracef.write(f"1987 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1987kbit")
	time.sleep(0.729)
	tracef.write(f"1980 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1980kbit")
	time.sleep(0.643)
	tracef.write(f"1881 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1881kbit")
	time.sleep(0.826)
	tracef.write(f"1978 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1978kbit")
	time.sleep(0.838)
	tracef.write(f"1927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1927kbit")
	time.sleep(0.348)
	tracef.write(f"1993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1993kbit")
	time.sleep(0.528)
	tracef.write(f"1959 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1959kbit")
	time.sleep(0.86)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.739)
	tracef.write(f"1849 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1849kbit")
	time.sleep(0.573)
	tracef.write(f"1886 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1886kbit")
	time.sleep(0.314)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.707)
	tracef.write(f"2010 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2010kbit")
	time.sleep(0.504)
	tracef.write(f"1947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1947kbit")
	time.sleep(0.66)
	tracef.write(f"1805 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1805kbit")
	time.sleep(0.584)
	tracef.write(f"1885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1885kbit")
	time.sleep(0.334)
	tracef.write(f"1829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1829kbit")
	time.sleep(0.285)
	tracef.write(f"1993 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1993kbit")
	time.sleep(0.479)
	tracef.write(f"1980 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1980kbit")
	time.sleep(0.462)
	tracef.write(f"1920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1920kbit")
	time.sleep(0.507)
	tracef.write(f"1915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1915kbit")
	time.sleep(0.61)
	tracef.write(f"1997 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1997kbit")
	time.sleep(0.87)
	tracef.write(f"1819 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1819kbit")
	time.sleep(0.845)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.425)
	tracef.write(f"1972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1972kbit")
	time.sleep(0.583)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.822)
	tracef.write(f"1832 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1832kbit")
	time.sleep(0.505)
	tracef.write(f"1953 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1953kbit")
	time.sleep(0.495)
	tracef.write(f"1889 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1889kbit")
	time.sleep(0.725)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.644)
	tracef.write(f"2006 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2006kbit")
	time.sleep(0.378)
	tracef.write(f"1828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1828kbit")
	time.sleep(0.766)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.293)
	tracef.write(f"1884 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1884kbit")
	time.sleep(0.656)
	tracef.write(f"1882 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1882kbit")
	time.sleep(0.357)
	tracef.write(f"2002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2002kbit")
	time.sleep(0.475)
	tracef.write(f"1871 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1871kbit")
	time.sleep(0.449)
	tracef.write(f"1936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1936kbit")
	time.sleep(0.47)
	tracef.write(f"1871 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1871kbit")
	time.sleep(0.574)
	tracef.write(f"1930 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1930kbit")
	time.sleep(0.777)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.853)
	tracef.write(f"1852 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1852kbit")
	time.sleep(0.417)
	tracef.write(f"1892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1892kbit")
	time.sleep(0.538)
	tracef.write(f"1944 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1944kbit")
	time.sleep(0.733)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.779)
	tracef.write(f"1890 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1890kbit")
	time.sleep(0.465)
	tracef.write(f"1864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1864kbit")
	time.sleep(0.486)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.526)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.728)
	tracef.write(f"1970 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1970kbit")
	time.sleep(0.292)
	tracef.write(f"2019 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2019kbit")
	time.sleep(0.401)
	tracef.write(f"1988 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1988kbit")
	time.sleep(0.662)
	tracef.write(f"1818 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1818kbit")
	time.sleep(0.323)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.731)
	tracef.write(f"1801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1801kbit")
	time.sleep(0.625)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()