#t:68-786 ; rate:1444-1685 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace132.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace132.txt", 'a+')
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1645kbit")
	time.sleep(0.627)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.495)
	tracef.write(f"1512 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1512kbit")
	time.sleep(0.218)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.344)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.112)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(0.097)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.47)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.696)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.431)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(0.358)
	tracef.write(f"1675 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1675kbit")
	time.sleep(0.692)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.472)
	tracef.write(f"1550 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1550kbit")
	time.sleep(0.276)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(0.131)
	tracef.write(f"1640 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1640kbit")
	time.sleep(0.333)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.737)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.303)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.628)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.095)
	tracef.write(f"1552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1552kbit")
	time.sleep(0.25)
	tracef.write(f"1533 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1533kbit")
	time.sleep(0.643)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.689)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(0.377)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.109)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.487)
	tracef.write(f"1472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1472kbit")
	time.sleep(0.365)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(0.173)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(0.517)
	tracef.write(f"1566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1566kbit")
	time.sleep(0.327)
	tracef.write(f"1502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1502kbit")
	time.sleep(0.677)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.177)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(0.099)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.64)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.074)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.717)
	tracef.write(f"1493 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1493kbit")
	time.sleep(0.197)
	tracef.write(f"1636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1636kbit")
	time.sleep(0.174)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.732)
	tracef.write(f"1684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1684kbit")
	time.sleep(0.312)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.251)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(0.641)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.147)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(0.311)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.384)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.211)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.298)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.587)
	tracef.write(f"1623 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1623kbit")
	time.sleep(0.671)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.465)
	tracef.write(f"1525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1525kbit")
	time.sleep(0.354)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(0.555)
	tracef.write(f"1682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1682kbit")
	time.sleep(0.768)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.449)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(0.663)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.422)
	tracef.write(f"1591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1591kbit")
	time.sleep(0.755)
	tracef.write(f"1665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1665kbit")
	time.sleep(0.517)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(0.085)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.294)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.297)
	tracef.write(f"1498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1498kbit")
	time.sleep(0.307)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.756)
	tracef.write(f"1519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1519kbit")
	time.sleep(0.127)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.175)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.749)
	tracef.write(f"1525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1525kbit")
	time.sleep(0.678)
	tracef.write(f"1544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1544kbit")
	time.sleep(0.417)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(0.184)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.604)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(0.341)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.726)
	tracef.write(f"1602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1602kbit")
	time.sleep(0.685)
	tracef.write(f"1673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1673kbit")
	time.sleep(0.523)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.622)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.208)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(0.254)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.574)
	tracef.write(f"1611 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1611kbit")
	time.sleep(0.595)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.513)
	tracef.write(f"1535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1535kbit")
	time.sleep(0.702)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.513)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.5)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(0.45)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.21)
	tracef.write(f"1552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1552kbit")
	time.sleep(0.174)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.729)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.222)
	tracef.write(f"1681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1681kbit")
	time.sleep(0.261)
	tracef.write(f"1584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1584kbit")
	time.sleep(0.241)
	tracef.write(f"1448 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1448kbit")
	time.sleep(0.476)
	tracef.write(f"1654 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1654kbit")
	time.sleep(0.318)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.498)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.082)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.477)
	tracef.write(f"1561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1561kbit")
	time.sleep(0.524)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.404)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.403)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.094)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(0.708)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.199)
	tracef.write(f"1483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1483kbit")
	time.sleep(0.656)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.2)
	tracef.write(f"1531 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1531kbit")
	time.sleep(0.442)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(0.324)
	tracef.write(f"1444 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1444kbit")
	time.sleep(0.46)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.397)
	tracef.write(f"1541 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1541kbit")
	time.sleep(0.381)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.125)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.5)
	tracef.write(f"1518 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1518kbit")
	time.sleep(0.759)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(0.152)
	tracef.write(f"1624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1624kbit")
	time.sleep(0.596)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.202)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(0.418)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.209)
	tracef.write(f"1670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1670kbit")
	time.sleep(0.631)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.539)
	tracef.write(f"1664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1664kbit")
	time.sleep(0.737)
	tracef.write(f"1509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1509kbit")
	time.sleep(0.443)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(0.509)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.739)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(0.502)
	tracef.write(f"1672 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1672kbit")
	time.sleep(0.51)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.373)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.321)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.09)
	tracef.write(f"1653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1653kbit")
	time.sleep(0.451)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(0.771)
	tracef.write(f"1572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1572kbit")
	time.sleep(0.442)
	tracef.write(f"1591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1591kbit")
	time.sleep(0.767)
	tracef.write(f"1517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1517kbit")
	time.sleep(0.429)
	tracef.write(f"1649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1649kbit")
	time.sleep(0.775)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.377)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.136)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.669)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.646)
	tracef.write(f"1523 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1523kbit")
	time.sleep(0.359)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.342)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.54)
	tracef.write(f"1510 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1510kbit")
	time.sleep(0.422)
	tracef.write(f"1681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1681kbit")
	time.sleep(0.568)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(0.424)
	tracef.write(f"1498 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1498kbit")
	time.sleep(0.071)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.1)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.496)
	tracef.write(f"1462 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1462kbit")
	time.sleep(0.395)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.704)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.346)
	tracef.write(f"1652 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1652kbit")
	time.sleep(0.342)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.692)
	tracef.write(f"1547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1547kbit")
	time.sleep(0.166)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.643)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.786)
	tracef.write(f"1618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1618kbit")
	time.sleep(0.538)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.47)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(0.072)
	tracef.write(f"1536 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1536kbit")
	time.sleep(0.688)
	tracef.write(f"1571 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1571kbit")
	time.sleep(0.732)
	tracef.write(f"1662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1662kbit")
	time.sleep(0.528)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.625)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.43)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.398)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.532)
	tracef.write(f"1569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1569kbit")
	time.sleep(0.142)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(0.255)
	tracef.write(f"1620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1620kbit")
	time.sleep(0.216)
	tracef.write(f"1599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1599kbit")
	time.sleep(0.146)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.455)
	tracef.write(f"1561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1561kbit")
	time.sleep(0.777)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.647)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.526)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.268)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(0.508)
	tracef.write(f"1621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1621kbit")
	time.sleep(0.115)
	tracef.write(f"1667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1667kbit")
	time.sleep(0.526)
	tracef.write(f"1661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1661kbit")
	time.sleep(0.655)
	tracef.write(f"1674 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1674kbit")
	time.sleep(0.706)
	tracef.write(f"1671 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1671kbit")
	time.sleep(0.12)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.677)
	tracef.write(f"1617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1617kbit")
	time.sleep(0.228)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.749)
	tracef.write(f"1563 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1563kbit")
	time.sleep(0.58)
	tracef.write(f"1544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1544kbit")
	time.sleep(0.129)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.125)
	tracef.write(f"1484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1484kbit")
	time.sleep(0.776)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.154)
	tracef.write(f"1458 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1458kbit")
	time.sleep(0.208)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(0.292)
	tracef.write(f"1508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1508kbit")
	time.sleep(0.19)
	tracef.write(f"1467 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1467kbit")
	time.sleep(0.537)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.766)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.251)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.074)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.687)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.34)
	tracef.write(f"1578 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1578kbit")
	time.sleep(0.742)
	tracef.write(f"1646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1646kbit")
	time.sleep(0.195)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.329)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.553)
	tracef.write(f"1545 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1545kbit")
	time.sleep(0.291)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.785)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.137)
	tracef.write(f"1577 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1577kbit")
	time.sleep(0.141)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.781)
	tracef.write(f"1482 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1482kbit")
	time.sleep(0.28)
	tracef.write(f"1551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1551kbit")
	time.sleep(0.475)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.274)
	tracef.write(f"1485 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1485kbit")
	time.sleep(0.161)
	tracef.write(f"1540 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1540kbit")
	time.sleep(0.346)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.1)
	tracef.write(f"1484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1484kbit")
	time.sleep(0.615)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(0.181)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.444)
	tracef.write(f"1681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1681kbit")
	time.sleep(0.288)
	tracef.write(f"1640 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1640kbit")
	time.sleep(0.211)
	tracef.write(f"1673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1673kbit")
	time.sleep(0.108)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.2)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(0.286)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.373)
	tracef.write(f"1557 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1557kbit")
	time.sleep(0.644)
	tracef.write(f"1529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1529kbit")
	time.sleep(0.762)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.707)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.736)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(0.459)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(0.262)
	tracef.write(f"1666 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1666kbit")
	time.sleep(0.615)
	tracef.write(f"1468 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1468kbit")
	time.sleep(0.416)
	tracef.write(f"1506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1506kbit")
	time.sleep(0.438)
	tracef.write(f"1652 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1652kbit")
	time.sleep(0.183)
	tracef.write(f"1508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1508kbit")
	time.sleep(0.423)
	tracef.write(f"1483 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1483kbit")
	time.sleep(0.462)
	tracef.write(f"1447 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1447kbit")
	time.sleep(0.545)
	tracef.write(f"1566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1566kbit")
	time.sleep(0.181)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.729)
	tracef.write(f"1608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1608kbit")
	time.sleep(0.699)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()