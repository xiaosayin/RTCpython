#t:697-754 ; rate:1860-2077 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace286.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace286.txt", 'a+')
	tracef.write(f"2015 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2015kbit")
	time.sleep(0.701)
	tracef.write(f"1915 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1915kbit")
	time.sleep(0.735)
	tracef.write(f"2055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2055kbit")
	time.sleep(0.754)
	tracef.write(f"1860 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1860kbit")
	time.sleep(0.72)
	tracef.write(f"1899 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1899kbit")
	time.sleep(0.715)
	tracef.write(f"2041 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2041kbit")
	time.sleep(0.745)
	tracef.write(f"1947 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1947kbit")
	time.sleep(0.714)
	tracef.write(f"1969 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1969kbit")
	time.sleep(0.706)
	tracef.write(f"1951 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1951kbit")
	time.sleep(0.707)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.74)
	tracef.write(f"1920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1920kbit")
	time.sleep(0.743)
	tracef.write(f"1954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1954kbit")
	time.sleep(0.712)
	tracef.write(f"2003 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2003kbit")
	time.sleep(0.728)
	tracef.write(f"2076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2076kbit")
	time.sleep(0.71)
	tracef.write(f"2057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2057kbit")
	time.sleep(0.753)
	tracef.write(f"2002 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2002kbit")
	time.sleep(0.698)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.753)
	tracef.write(f"2071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2071kbit")
	time.sleep(0.729)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.72)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.722)
	tracef.write(f"1892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1892kbit")
	time.sleep(0.75)
	tracef.write(f"1958 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1958kbit")
	time.sleep(0.721)
	tracef.write(f"2058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2058kbit")
	time.sleep(0.719)
	tracef.write(f"2024 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2024kbit")
	time.sleep(0.709)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.726)
	tracef.write(f"1955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1955kbit")
	time.sleep(0.708)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.698)
	tracef.write(f"1906 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1906kbit")
	time.sleep(0.753)
	tracef.write(f"2052 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2052kbit")
	time.sleep(0.716)
	tracef.write(f"1949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1949kbit")
	time.sleep(0.724)
	tracef.write(f"1941 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1941kbit")
	time.sleep(0.708)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.708)
	tracef.write(f"2018 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2018kbit")
	time.sleep(0.738)
	tracef.write(f"2043 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2043kbit")
	time.sleep(0.732)
	tracef.write(f"1981 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1981kbit")
	time.sleep(0.701)
	tracef.write(f"1991 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1991kbit")
	time.sleep(0.7)
	tracef.write(f"1873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1873kbit")
	time.sleep(0.718)
	tracef.write(f"1887 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1887kbit")
	time.sleep(0.75)
	tracef.write(f"2029 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2029kbit")
	time.sleep(0.753)
	tracef.write(f"1862 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1862kbit")
	time.sleep(0.702)
	tracef.write(f"1888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1888kbit")
	time.sleep(0.713)
	tracef.write(f"2011 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2011kbit")
	time.sleep(0.709)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.71)
	tracef.write(f"1933 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1933kbit")
	time.sleep(0.722)
	tracef.write(f"2006 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2006kbit")
	time.sleep(0.723)
	tracef.write(f"2016 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2016kbit")
	time.sleep(0.709)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.74)
	tracef.write(f"1973 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1973kbit")
	time.sleep(0.698)
	tracef.write(f"1865 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1865kbit")
	time.sleep(0.704)
	tracef.write(f"1863 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1863kbit")
	time.sleep(0.733)
	tracef.write(f"1957 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1957kbit")
	time.sleep(0.737)
	tracef.write(f"2027 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2027kbit")
	time.sleep(0.733)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.708)
	tracef.write(f"2054 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2054kbit")
	time.sleep(0.729)
	tracef.write(f"2012 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2012kbit")
	time.sleep(0.706)
	tracef.write(f"2013 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2013kbit")
	time.sleep(0.727)
	tracef.write(f"2076 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2076kbit")
	time.sleep(0.714)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.751)
	tracef.write(f"1956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1956kbit")
	time.sleep(0.737)
	tracef.write(f"1938 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1938kbit")
	time.sleep(0.713)
	tracef.write(f"2005 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2005kbit")
	time.sleep(0.707)
	tracef.write(f"1864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1864kbit")
	time.sleep(0.745)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.727)
	tracef.write(f"1940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1940kbit")
	time.sleep(0.748)
	tracef.write(f"1900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1900kbit")
	time.sleep(0.735)
	tracef.write(f"2007 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2007kbit")
	time.sleep(0.708)
	tracef.write(f"1972 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1972kbit")
	time.sleep(0.735)
	tracef.write(f"1967 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1967kbit")
	time.sleep(0.711)
	tracef.write(f"1989 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1989kbit")
	time.sleep(0.715)
	tracef.write(f"1925 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1925kbit")
	time.sleep(0.738)
	tracef.write(f"1913 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1913kbit")
	time.sleep(0.709)
	tracef.write(f"1954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1954kbit")
	time.sleep(0.699)
	tracef.write(f"2010 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2010kbit")
	time.sleep(0.723)
	tracef.write(f"1888 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1888kbit")
	time.sleep(0.748)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.741)
	tracef.write(f"1992 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1992kbit")
	time.sleep(0.701)
	tracef.write(f"1964 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1964kbit")
	time.sleep(0.707)
	tracef.write(f"2045 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2045kbit")
	time.sleep(0.714)
	tracef.write(f"2035 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2035kbit")
	time.sleep(0.737)
	tracef.write(f"1893 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1893kbit")
	time.sleep(0.716)
	tracef.write(f"1999 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1999kbit")
	time.sleep(0.707)
	tracef.write(f"2037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2037kbit")
	time.sleep(0.71)
	tracef.write(f"1908 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1908kbit")
	time.sleep(0.72)
	tracef.write(f"2030 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2030kbit")
	time.sleep(0.732)
	tracef.write(f"1927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1927kbit")
	time.sleep(0.74)
	tracef.write(f"1949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1949kbit")
	time.sleep(0.714)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.752)
	tracef.write(f"2071 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2071kbit")
	time.sleep(0.748)
	tracef.write(f"1874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1874kbit")
	time.sleep(0.723)
	tracef.write(f"1995 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1995kbit")
	time.sleep(0.711)
	tracef.write(f"1978 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1978kbit")
	time.sleep(0.72)
	tracef.write(f"1922 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1922kbit")
	time.sleep(0.724)
	tracef.write(f"2028 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2028kbit")
	time.sleep(0.709)
	tracef.write(f"2037 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2037kbit")
	time.sleep(0.72)
	tracef.write(f"2049 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2049kbit")
	time.sleep(0.743)
	tracef.write(f"1891 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1891kbit")
	time.sleep(0.732)
	tracef.write(f"1900 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1900kbit")
	time.sleep(0.71)
	tracef.write(f"1877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1877kbit")
	time.sleep(0.702)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.75)
	tracef.write(f"2065 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2065kbit")
	time.sleep(0.741)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.73)
	tracef.write(f"2040 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2040kbit")
	time.sleep(0.702)
	tracef.write(f"1995 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1995kbit")
	time.sleep(0.745)
	tracef.write(f"1990 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1990kbit")
	time.sleep(0.717)
	tracef.write(f"1955 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1955kbit")
	time.sleep(0.748)
	tracef.write(f"1942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1942kbit")
	time.sleep(0.711)
	tracef.write(f"1917 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1917kbit")
	time.sleep(0.746)
	tracef.write(f"1903 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1903kbit")
	time.sleep(0.743)
	tracef.write(f"1986 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1986kbit")
	time.sleep(0.752)
	tracef.write(f"1943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1943kbit")
	time.sleep(0.738)
	tracef.write(f"1921 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1921kbit")
	time.sleep(0.708)
	tracef.write(f"1879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1879kbit")
	time.sleep(0.703)
	tracef.write(f"1936 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1936kbit")
	time.sleep(0.744)
	tracef.write(f"1931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1931kbit")
	time.sleep(0.712)
	tracef.write(f"1911 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1911kbit")
	time.sleep(0.737)
	tracef.write(f"2072 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2072kbit")
	time.sleep(0.721)
	tracef.write(f"2032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2032kbit")
	time.sleep(0.698)
	tracef.write(f"1919 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1919kbit")
	time.sleep(0.697)
	tracef.write(f"2048 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2048kbit")
	time.sleep(0.718)
	tracef.write(f"1956 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1956kbit")
	time.sleep(0.715)
	tracef.write(f"2051 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2051kbit")
	time.sleep(0.732)
	tracef.write(f"1926 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1926kbit")
	time.sleep(0.745)
	tracef.write(f"2047 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2047kbit")
	time.sleep(0.73)
	tracef.write(f"2014 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2014kbit")
	time.sleep(0.71)
	tracef.write(f"2061 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2061kbit")
	time.sleep(0.726)
	tracef.write(f"2053 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2053kbit")
	time.sleep(0.72)
	tracef.write(f"1864 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1864kbit")
	time.sleep(0.737)
	tracef.write(f"1892 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1892kbit")
	time.sleep(0.742)
	tracef.write(f"1919 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1919kbit")
	time.sleep(0.744)
	tracef.write(f"2058 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2058kbit")
	time.sleep(0.721)
	tracef.write(f"1878 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1878kbit")
	time.sleep(0.736)
	tracef.write(f"1950 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1950kbit")
	time.sleep(0.739)
	tracef.write(f"1898 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1898kbit")
	time.sleep(0.704)
	tracef.write(f"1954 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1954kbit")
	time.sleep(0.715)
	tracef.write(f"1998 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1998kbit")
	time.sleep(0.717)
	tracef.write(f"2017 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2017kbit")
	time.sleep(0.727)
	tracef.write(f"1885 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1885kbit")
	time.sleep(0.737)
	tracef.write(f"1930 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1930kbit")
	time.sleep(0.706)
	tracef.write(f"2073 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2073kbit")
	time.sleep(0.742)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()