#t:630-951 ; rate:1580-1650 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace55.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace55.txt", 'a+')
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1587kbit")
	time.sleep(0.697)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.89)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.869)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.675)
	tracef.write(f"1597 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1597kbit")
	time.sleep(0.939)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.773)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.788)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.895)
	tracef.write(f"1646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1646kbit")
	time.sleep(0.748)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.647)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.656)
	tracef.write(f"1611 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1611kbit")
	time.sleep(0.677)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.863)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.829)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.876)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.738)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.873)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.819)
	tracef.write(f"1609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1609kbit")
	time.sleep(0.826)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.737)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.826)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.922)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.794)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.925)
	tracef.write(f"1640 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1640kbit")
	time.sleep(0.835)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.784)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.819)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.814)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.824)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.69)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.673)
	tracef.write(f"1620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1620kbit")
	time.sleep(0.91)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.634)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.892)
	tracef.write(f"1599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1599kbit")
	time.sleep(0.806)
	tracef.write(f"1637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1637kbit")
	time.sleep(0.785)
	tracef.write(f"1624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1624kbit")
	time.sleep(0.755)
	tracef.write(f"1600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1600kbit")
	time.sleep(0.907)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.938)
	tracef.write(f"1602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1602kbit")
	time.sleep(0.771)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.679)
	tracef.write(f"1608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1608kbit")
	time.sleep(0.744)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.765)
	tracef.write(f"1611 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1611kbit")
	time.sleep(0.927)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.762)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.72)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.904)
	tracef.write(f"1602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1602kbit")
	time.sleep(0.832)
	tracef.write(f"1627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1627kbit")
	time.sleep(0.887)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.864)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.647)
	tracef.write(f"1627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1627kbit")
	time.sleep(0.757)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.735)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.718)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.67)
	tracef.write(f"1584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1584kbit")
	time.sleep(0.927)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.951)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.895)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.689)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.709)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.869)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.687)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.648)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.812)
	tracef.write(f"1597 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1597kbit")
	time.sleep(0.697)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.705)
	tracef.write(f"1608 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1608kbit")
	time.sleep(0.763)
	tracef.write(f"1629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1629kbit")
	time.sleep(0.917)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.669)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.88)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.937)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.772)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.641)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.836)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.93)
	tracef.write(f"1609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1609kbit")
	time.sleep(0.943)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.934)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.868)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.682)
	tracef.write(f"1636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1636kbit")
	time.sleep(0.725)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.878)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.801)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.757)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.793)
	tracef.write(f"1649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1649kbit")
	time.sleep(0.641)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.89)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.663)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.897)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.927)
	tracef.write(f"1610 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1610kbit")
	time.sleep(0.925)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.641)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.918)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.812)
	tracef.write(f"1617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1617kbit")
	time.sleep(0.874)
	tracef.write(f"1590 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1590kbit")
	time.sleep(0.743)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.873)
	tracef.write(f"1612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1612kbit")
	time.sleep(0.948)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.763)
	tracef.write(f"1636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1636kbit")
	time.sleep(0.771)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.754)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.802)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.713)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.767)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.782)
	tracef.write(f"1600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1600kbit")
	time.sleep(0.711)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.801)
	tracef.write(f"1591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1591kbit")
	time.sleep(0.732)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.878)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.718)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.699)
	tracef.write(f"1607 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1607kbit")
	time.sleep(0.717)
	tracef.write(f"1620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1620kbit")
	time.sleep(0.911)
	tracef.write(f"1584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1584kbit")
	time.sleep(0.783)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.815)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.945)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.911)
	tracef.write(f"1600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1600kbit")
	time.sleep(0.737)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.941)
	tracef.write(f"1609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1609kbit")
	time.sleep(0.771)
	tracef.write(f"1614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1614kbit")
	time.sleep(0.935)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.644)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.879)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.721)
	tracef.write(f"1597 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1597kbit")
	time.sleep(0.796)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.917)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()