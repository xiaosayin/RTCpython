#t:410-673 ; rate:1397-1671 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace322.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace322.txt", 'a+')
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1479kbit")
	time.sleep(0.412)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.434)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(0.623)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.422)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.45)
	tracef.write(f"1469 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1469kbit")
	time.sleep(0.478)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.421)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.636)
	tracef.write(f"1521 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1521kbit")
	time.sleep(0.56)
	tracef.write(f"1580 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1580kbit")
	time.sleep(0.551)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(0.544)
	tracef.write(f"1479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1479kbit")
	time.sleep(0.627)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.67)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.459)
	tracef.write(f"1663 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1663kbit")
	time.sleep(0.472)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(0.664)
	tracef.write(f"1464 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1464kbit")
	time.sleep(0.643)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(0.579)
	tracef.write(f"1398 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1398kbit")
	time.sleep(0.651)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(0.626)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.546)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.635)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(0.464)
	tracef.write(f"1636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1636kbit")
	time.sleep(0.559)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.524)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.662)
	tracef.write(f"1563 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1563kbit")
	time.sleep(0.426)
	tracef.write(f"1558 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1558kbit")
	time.sleep(0.655)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.619)
	tracef.write(f"1439 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1439kbit")
	time.sleep(0.627)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.613)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(0.545)
	tracef.write(f"1489 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1489kbit")
	time.sleep(0.648)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.564)
	tracef.write(f"1508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1508kbit")
	time.sleep(0.542)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.64)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.656)
	tracef.write(f"1463 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1463kbit")
	time.sleep(0.413)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(0.482)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(0.602)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.613)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.621)
	tracef.write(f"1631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1631kbit")
	time.sleep(0.533)
	tracef.write(f"1575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1575kbit")
	time.sleep(0.605)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.565)
	tracef.write(f"1567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1567kbit")
	time.sleep(0.444)
	tracef.write(f"1585 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1585kbit")
	time.sleep(0.579)
	tracef.write(f"1454 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1454kbit")
	time.sleep(0.504)
	tracef.write(f"1442 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1442kbit")
	time.sleep(0.601)
	tracef.write(f"1535 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1535kbit")
	time.sleep(0.44)
	tracef.write(f"1452 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1452kbit")
	time.sleep(0.622)
	tracef.write(f"1649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1649kbit")
	time.sleep(0.49)
	tracef.write(f"1660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1660kbit")
	time.sleep(0.443)
	tracef.write(f"1416 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1416kbit")
	time.sleep(0.639)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(0.629)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.504)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(0.47)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(0.57)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(0.504)
	tracef.write(f"1546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1546kbit")
	time.sleep(0.486)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(0.607)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.531)
	tracef.write(f"1572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1572kbit")
	time.sleep(0.505)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.574)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.649)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(0.421)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.562)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(0.517)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.632)
	tracef.write(f"1664 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1664kbit")
	time.sleep(0.56)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.447)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(0.434)
	tracef.write(f"1429 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1429kbit")
	time.sleep(0.553)
	tracef.write(f"1529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1529kbit")
	time.sleep(0.475)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.567)
	tracef.write(f"1513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1513kbit")
	time.sleep(0.623)
	tracef.write(f"1624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1624kbit")
	time.sleep(0.663)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.583)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.542)
	tracef.write(f"1508 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1508kbit")
	time.sleep(0.67)
	tracef.write(f"1594 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1594kbit")
	time.sleep(0.512)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.421)
	tracef.write(f"1563 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1563kbit")
	time.sleep(0.458)
	tracef.write(f"1423 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1423kbit")
	time.sleep(0.552)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(0.597)
	tracef.write(f"1646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1646kbit")
	time.sleep(0.645)
	tracef.write(f"1565 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1565kbit")
	time.sleep(0.462)
	tracef.write(f"1451 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1451kbit")
	time.sleep(0.602)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.668)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.58)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.545)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(0.515)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(0.559)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.579)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.626)
	tracef.write(f"1430 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1430kbit")
	time.sleep(0.437)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(0.572)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.503)
	tracef.write(f"1450 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1450kbit")
	time.sleep(0.598)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(0.478)
	tracef.write(f"1407 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1407kbit")
	time.sleep(0.538)
	tracef.write(f"1529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1529kbit")
	time.sleep(0.486)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.641)
	tracef.write(f"1583 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1583kbit")
	time.sleep(0.524)
	tracef.write(f"1595 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1595kbit")
	time.sleep(0.544)
	tracef.write(f"1634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1634kbit")
	time.sleep(0.542)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.652)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(0.464)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.498)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.52)
	tracef.write(f"1553 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1553kbit")
	time.sleep(0.629)
	tracef.write(f"1666 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1666kbit")
	time.sleep(0.67)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(0.441)
	tracef.write(f"1513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1513kbit")
	time.sleep(0.627)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.613)
	tracef.write(f"1624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1624kbit")
	time.sleep(0.627)
	tracef.write(f"1652 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1652kbit")
	time.sleep(0.45)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.638)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(0.574)
	tracef.write(f"1599 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1599kbit")
	time.sleep(0.598)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.499)
	tracef.write(f"1471 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1471kbit")
	time.sleep(0.606)
	tracef.write(f"1495 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1495kbit")
	time.sleep(0.648)
	tracef.write(f"1650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1650kbit")
	time.sleep(0.443)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.601)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(0.455)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.529)
	tracef.write(f"1659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1659kbit")
	time.sleep(0.503)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(0.487)
	tracef.write(f"1628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1628kbit")
	time.sleep(0.491)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.608)
	tracef.write(f"1544 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1544kbit")
	time.sleep(0.565)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(0.491)
	tracef.write(f"1474 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1474kbit")
	time.sleep(0.632)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.45)
	tracef.write(f"1589 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1589kbit")
	time.sleep(0.585)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(0.645)
	tracef.write(f"1596 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1596kbit")
	time.sleep(0.538)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(0.417)
	tracef.write(f"1665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1665kbit")
	time.sleep(0.513)
	tracef.write(f"1466 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1466kbit")
	time.sleep(0.614)
	tracef.write(f"1445 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1445kbit")
	time.sleep(0.645)
	tracef.write(f"1413 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1413kbit")
	time.sleep(0.607)
	tracef.write(f"1548 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1548kbit")
	time.sleep(0.494)
	tracef.write(f"1546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1546kbit")
	time.sleep(0.601)
	tracef.write(f"1555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1555kbit")
	time.sleep(0.498)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.458)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.504)
	tracef.write(f"1606 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1606kbit")
	time.sleep(0.416)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.422)
	tracef.write(f"1547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1547kbit")
	time.sleep(0.531)
	tracef.write(f"1600 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1600kbit")
	time.sleep(0.585)
	tracef.write(f"1633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1633kbit")
	time.sleep(0.667)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.666)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.422)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.568)
	tracef.write(f"1496 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1496kbit")
	time.sleep(0.652)
	tracef.write(f"1551 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1551kbit")
	time.sleep(0.43)
	tracef.write(f"1643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1643kbit")
	time.sleep(0.548)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.461)
	tracef.write(f"1419 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1419kbit")
	time.sleep(0.522)
	tracef.write(f"1568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1568kbit")
	time.sleep(0.552)
	tracef.write(f"1412 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1412kbit")
	time.sleep(0.459)
	tracef.write(f"1438 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1438kbit")
	time.sleep(0.634)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.561)
	tracef.write(f"1552 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1552kbit")
	time.sleep(0.438)
	tracef.write(f"1405 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1405kbit")
	time.sleep(0.635)
	tracef.write(f"1603 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1603kbit")
	time.sleep(0.436)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.507)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.539)
	tracef.write(f"1446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1446kbit")
	time.sleep(0.634)
	tracef.write(f"1662 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1662kbit")
	time.sleep(0.433)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.598)
	tracef.write(f"1547 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1547kbit")
	time.sleep(0.616)
	tracef.write(f"1592 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1592kbit")
	time.sleep(0.508)
	tracef.write(f"1418 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1418kbit")
	time.sleep(0.624)
	tracef.write(f"1568 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1568kbit")
	time.sleep(0.562)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(0.67)
	tracef.write(f"1441 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1441kbit")
	time.sleep(0.525)
	tracef.write(f"1530 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1530kbit")
	time.sleep(0.474)
	tracef.write(f"1574 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1574kbit")
	time.sleep(0.583)
	tracef.write(f"1612 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1612kbit")
	time.sleep(0.62)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()