#t:251-549 ; rate:1352-1774 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace251.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace251.txt", 'a+')
	tracef.write(f"1721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 1721kbit")
	time.sleep(0.4)
	tracef.write(f"1475 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1475kbit")
	time.sleep(0.437)
	tracef.write(f"1639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1639kbit")
	time.sleep(0.3)
	tracef.write(f"1669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1669kbit")
	time.sleep(0.505)
	tracef.write(f"1773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1773kbit")
	time.sleep(0.32)
	tracef.write(f"1528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1528kbit")
	time.sleep(0.402)
	tracef.write(f"1356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1356kbit")
	time.sleep(0.406)
	tracef.write(f"1525 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1525kbit")
	time.sleep(0.434)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.453)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(0.312)
	tracef.write(f"1626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1626kbit")
	time.sleep(0.535)
	tracef.write(f"1554 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1554kbit")
	time.sleep(0.518)
	tracef.write(f"1476 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1476kbit")
	time.sleep(0.293)
	tracef.write(f"1757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1757kbit")
	time.sleep(0.406)
	tracef.write(f"1604 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1604kbit")
	time.sleep(0.405)
	tracef.write(f"1371 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1371kbit")
	time.sleep(0.515)
	tracef.write(f"1505 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1505kbit")
	time.sleep(0.306)
	tracef.write(f"1691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1691kbit")
	time.sleep(0.449)
	tracef.write(f"1362 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1362kbit")
	time.sleep(0.532)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.481)
	tracef.write(f"1571 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1571kbit")
	time.sleep(0.427)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.289)
	tracef.write(f"1504 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1504kbit")
	time.sleep(0.314)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.342)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(0.317)
	tracef.write(f"1377 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1377kbit")
	time.sleep(0.545)
	tracef.write(f"1670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1670kbit")
	time.sleep(0.326)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(0.41)
	tracef.write(f"1622 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1622kbit")
	time.sleep(0.508)
	tracef.write(f"1461 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1461kbit")
	time.sleep(0.367)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(0.256)
	tracef.write(f"1755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1755kbit")
	time.sleep(0.458)
	tracef.write(f"1576 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1576kbit")
	time.sleep(0.486)
	tracef.write(f"1424 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1424kbit")
	time.sleep(0.266)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.336)
	tracef.write(f"1737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1737kbit")
	time.sleep(0.301)
	tracef.write(f"1363 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1363kbit")
	time.sleep(0.28)
	tracef.write(f"1369 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1369kbit")
	time.sleep(0.344)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.479)
	tracef.write(f"1443 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1443kbit")
	time.sleep(0.318)
	tracef.write(f"1726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1726kbit")
	time.sleep(0.273)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.514)
	tracef.write(f"1615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1615kbit")
	time.sleep(0.397)
	tracef.write(f"1519 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1519kbit")
	time.sleep(0.411)
	tracef.write(f"1653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1653kbit")
	time.sleep(0.475)
	tracef.write(f"1680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1680kbit")
	time.sleep(0.263)
	tracef.write(f"1701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1701kbit")
	time.sleep(0.397)
	tracef.write(f"1581 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1581kbit")
	time.sleep(0.523)
	tracef.write(f"1630 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1630kbit")
	time.sleep(0.336)
	tracef.write(f"1460 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1460kbit")
	time.sleep(0.319)
	tracef.write(f"1507 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1507kbit")
	time.sleep(0.461)
	tracef.write(f"1356 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1356kbit")
	time.sleep(0.396)
	tracef.write(f"1556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1556kbit")
	time.sleep(0.368)
	tracef.write(f"1425 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1425kbit")
	time.sleep(0.265)
	tracef.write(f"1747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1747kbit")
	time.sleep(0.468)
	tracef.write(f"1686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1686kbit")
	time.sleep(0.367)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(0.37)
	tracef.write(f"1644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1644kbit")
	time.sleep(0.315)
	tracef.write(f"1364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1364kbit")
	time.sleep(0.483)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.478)
	tracef.write(f"1620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1620kbit")
	time.sleep(0.284)
	tracef.write(f"1659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1659kbit")
	time.sleep(0.377)
	tracef.write(f"1539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1539kbit")
	time.sleep(0.286)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.381)
	tracef.write(f"1740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1740kbit")
	time.sleep(0.366)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(0.524)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.252)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.459)
	tracef.write(f"1584 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1584kbit")
	time.sleep(0.405)
	tracef.write(f"1470 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1470kbit")
	time.sleep(0.519)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.503)
	tracef.write(f"1538 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1538kbit")
	time.sleep(0.393)
	tracef.write(f"1506 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1506kbit")
	time.sleep(0.498)
	tracef.write(f"1593 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1593kbit")
	time.sleep(0.509)
	tracef.write(f"1617 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1617kbit")
	time.sleep(0.443)
	tracef.write(f"1653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1653kbit")
	time.sleep(0.501)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.491)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.393)
	tracef.write(f"1503 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1503kbit")
	time.sleep(0.323)
	tracef.write(f"1726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1726kbit")
	time.sleep(0.254)
	tracef.write(f"1655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1655kbit")
	time.sleep(0.473)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.483)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.479)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.502)
	tracef.write(f"1586 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1586kbit")
	time.sleep(0.539)
	tracef.write(f"1453 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1453kbit")
	time.sleep(0.386)
	tracef.write(f"1656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1656kbit")
	time.sleep(0.451)
	tracef.write(f"1532 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1532kbit")
	time.sleep(0.306)
	tracef.write(f"1391 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1391kbit")
	time.sleep(0.444)
	tracef.write(f"1387 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1387kbit")
	time.sleep(0.432)
	tracef.write(f"1668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1668kbit")
	time.sleep(0.397)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.357)
	tracef.write(f"1646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1646kbit")
	time.sleep(0.342)
	tracef.write(f"1744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1744kbit")
	time.sleep(0.339)
	tracef.write(f"1601 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1601kbit")
	time.sleep(0.254)
	tracef.write(f"1509 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1509kbit")
	time.sleep(0.402)
	tracef.write(f"1572 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1572kbit")
	time.sleep(0.341)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.457)
	tracef.write(f"1771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1771kbit")
	time.sleep(0.549)
	tracef.write(f"1648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1648kbit")
	time.sleep(0.52)
	tracef.write(f"1688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1688kbit")
	time.sleep(0.295)
	tracef.write(f"1759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1759kbit")
	time.sleep(0.478)
	tracef.write(f"1625 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1625kbit")
	time.sleep(0.451)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.287)
	tracef.write(f"1711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1711kbit")
	time.sleep(0.534)
	tracef.write(f"1613 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1613kbit")
	time.sleep(0.392)
	tracef.write(f"1751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1751kbit")
	time.sleep(0.405)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(0.519)
	tracef.write(f"1446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1446kbit")
	time.sleep(0.473)
	tracef.write(f"1698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1698kbit")
	time.sleep(0.373)
	tracef.write(f"1484 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1484kbit")
	time.sleep(0.415)
	tracef.write(f"1763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1763kbit")
	time.sleep(0.374)
	tracef.write(f"1638 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1638kbit")
	time.sleep(0.505)
	tracef.write(f"1543 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1543kbit")
	time.sleep(0.391)
	tracef.write(f"1502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1502kbit")
	time.sleep(0.52)
	tracef.write(f"1490 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1490kbit")
	time.sleep(0.435)
	tracef.write(f"1735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1735kbit")
	time.sleep(0.386)
	tracef.write(f"1562 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1562kbit")
	time.sleep(0.514)
	tracef.write(f"1651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1651kbit")
	time.sleep(0.456)
	tracef.write(f"1627 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1627kbit")
	time.sleep(0.326)
	tracef.write(f"1747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1747kbit")
	time.sleep(0.395)
	tracef.write(f"1526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1526kbit")
	time.sleep(0.544)
	tracef.write(f"1687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1687kbit")
	time.sleep(0.364)
	tracef.write(f"1566 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1566kbit")
	time.sleep(0.409)
	tracef.write(f"1514 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1514kbit")
	time.sleep(0.29)
	tracef.write(f"1605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1605kbit")
	time.sleep(0.282)
	tracef.write(f"1636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1636kbit")
	time.sleep(0.37)
	tracef.write(f"1765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1765kbit")
	time.sleep(0.454)
	tracef.write(f"1434 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1434kbit")
	time.sleep(0.347)
	tracef.write(f"1656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1656kbit")
	time.sleep(0.361)
	tracef.write(f"1582 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1582kbit")
	time.sleep(0.368)
	tracef.write(f"1641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1641kbit")
	time.sleep(0.471)
	tracef.write(f"1491 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1491kbit")
	time.sleep(0.334)
	tracef.write(f"1415 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1415kbit")
	time.sleep(0.397)
	tracef.write(f"1449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1449kbit")
	time.sleep(0.463)
	tracef.write(f"1360 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1360kbit")
	time.sleep(0.524)
	tracef.write(f"1765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1765kbit")
	time.sleep(0.454)
	tracef.write(f"1395 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1395kbit")
	time.sleep(0.265)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.534)
	tracef.write(f"1409 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1409kbit")
	time.sleep(0.47)
	tracef.write(f"1397 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1397kbit")
	time.sleep(0.536)
	tracef.write(f"1414 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1414kbit")
	time.sleep(0.275)
	tracef.write(f"1372 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1372kbit")
	time.sleep(0.259)
	tracef.write(f"1365 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1365kbit")
	time.sleep(0.43)
	tracef.write(f"1716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1716kbit")
	time.sleep(0.54)
	tracef.write(f"1616 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1616kbit")
	time.sleep(0.502)
	tracef.write(f"1516 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1516kbit")
	time.sleep(0.489)
	tracef.write(f"1749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1749kbit")
	time.sleep(0.503)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.258)
	tracef.write(f"1770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1770kbit")
	time.sleep(0.333)
	tracef.write(f"1659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1659kbit")
	time.sleep(0.412)
	tracef.write(f"1392 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1392kbit")
	time.sleep(0.541)
	tracef.write(f"1632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1632kbit")
	time.sleep(0.474)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.343)
	tracef.write(f"1404 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1404kbit")
	time.sleep(0.547)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(0.463)
	tracef.write(f"1642 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1642kbit")
	time.sleep(0.436)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(0.472)
	tracef.write(f"1429 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1429kbit")
	time.sleep(0.349)
	tracef.write(f"1570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1570kbit")
	time.sleep(0.257)
	tracef.write(f"1465 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1465kbit")
	time.sleep(0.328)
	tracef.write(f"1695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1695kbit")
	time.sleep(0.476)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.476)
	tracef.write(f"1587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1587kbit")
	time.sleep(0.439)
	tracef.write(f"1367 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1367kbit")
	time.sleep(0.438)
	tracef.write(f"1388 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1388kbit")
	time.sleep(0.466)
	tracef.write(f"1396 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1396kbit")
	time.sleep(0.504)
	tracef.write(f"1427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1427kbit")
	time.sleep(0.4)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.355)
	tracef.write(f"1708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1708kbit")
	time.sleep(0.425)
	tracef.write(f"1752 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1752kbit")
	time.sleep(0.293)
	tracef.write(f"1436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1436kbit")
	time.sleep(0.403)
	tracef.write(f"1564 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1564kbit")
	time.sleep(0.372)
	tracef.write(f"1734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1734kbit")
	time.sleep(0.267)
	tracef.write(f"1459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1459kbit")
	time.sleep(0.256)
	tracef.write(f"1370 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1370kbit")
	time.sleep(0.502)
	tracef.write(f"1502 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1502kbit")
	time.sleep(0.345)
	tracef.write(f"1559 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1559kbit")
	time.sleep(0.481)
	tracef.write(f"1390 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1390kbit")
	time.sleep(0.331)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(0.333)
	tracef.write(f"1683 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1683kbit")
	time.sleep(0.296)
	tracef.write(f"1486 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1486kbit")
	time.sleep(0.542)
	tracef.write(f"1733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1733kbit")
	time.sleep(0.414)
	tracef.write(f"1501 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1501kbit")
	time.sleep(0.518)
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1511kbit")
	time.sleep(0.422)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.385)
	tracef.write(f"1560 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1560kbit")
	time.sleep(0.29)
	tracef.write(f"1709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1709kbit")
	time.sleep(0.314)
	tracef.write(f"1694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1694kbit")
	time.sleep(0.451)
	tracef.write(f"1522 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1522kbit")
	time.sleep(0.479)
	tracef.write(f"1715 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1715kbit")
	time.sleep(0.415)
	tracef.write(f"1737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1737kbit")
	time.sleep(0.465)
	tracef.write(f"1693 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1693kbit")
	time.sleep(0.342)
	tracef.write(f"1477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1477kbit")
	time.sleep(0.435)
	tracef.write(f"1473 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1473kbit")
	time.sleep(0.425)
	tracef.write(f"1767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1767kbit")
	time.sleep(0.282)
	tracef.write(f"1598 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1598kbit")
	time.sleep(0.336)
	tracef.write(f"1488 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1488kbit")
	time.sleep(0.487)
	tracef.write(f"1500 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1500kbit")
	time.sleep(0.418)
	tracef.write(f"1417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1417kbit")
	time.sleep(0.266)
	tracef.write(f"1748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1748kbit")
	time.sleep(0.517)
	tracef.write(f"1621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1621kbit")
	time.sleep(0.452)
	tracef.write(f"1527 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1527kbit")
	time.sleep(0.492)
	tracef.write(f"1745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1745kbit")
	time.sleep(0.437)
	tracef.write(f"1588 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1588kbit")
	time.sleep(0.308)
	tracef.write(f"1573 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1573kbit")
	time.sleep(0.302)
	tracef.write(f"1674 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1674kbit")
	time.sleep(0.484)
	tracef.write(f"1497 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1497kbit")
	time.sleep(0.339)
	tracef.write(f"1511 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1511kbit")
	time.sleep(0.323)
	tracef.write(f"1670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1670kbit")
	time.sleep(0.358)
	tracef.write(f"1658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1658kbit")
	time.sleep(0.467)
	tracef.write(f"1456 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1456kbit")
	time.sleep(0.516)
	tracef.write(f"1457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1457kbit")
	time.sleep(0.353)
	tracef.write(f"1679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1679kbit")
	time.sleep(0.4)
	tracef.write(f"1431 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1431kbit")
	time.sleep(0.296)
	tracef.write(f"1546 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1546kbit")
	time.sleep(0.316)
	tracef.write(f"1698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1698kbit")
	time.sleep(0.407)
	tracef.write(f"1374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1374kbit")
	time.sleep(0.327)
	tracef.write(f"1478 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1478kbit")
	time.sleep(0.532)
	tracef.write(f"1618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1618kbit")
	time.sleep(0.538)
	tracef.write(f"1619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1619kbit")
	time.sleep(0.492)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(0.411)
	tracef.write(f"1720 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1720kbit")
	time.sleep(0.375)
	tracef.write(f"1494 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1494kbit")
	time.sleep(0.508)
	tracef.write(f"1408 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1408kbit")
	time.sleep(0.392)
	tracef.write(f"1481 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1481kbit")
	time.sleep(0.266)
	tracef.write(f"1758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1758kbit")
	time.sleep(0.482)
	tracef.write(f"1736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1736kbit")
	time.sleep(0.457)
	tracef.write(f"1646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1646kbit")
	time.sleep(0.417)
	tracef.write(f"1757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1757kbit")
	time.sleep(0.506)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(0.53)
	tracef.write(f"1647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1647kbit")
	time.sleep(0.301)
	tracef.write(f"1440 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1440kbit")
	time.sleep(0.29)
	tracef.write(f"1432 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1432kbit")
	time.sleep(0.45)
	tracef.write(f"1671 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1671kbit")
	time.sleep(0.457)
	tracef.write(f"1713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1713kbit")
	time.sleep(0.372)
	tracef.write(f"1428 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1428kbit")
	time.sleep(0.445)
	tracef.write(f"1422 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1422kbit")
	time.sleep(0.274)
	tracef.write(f"1702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1702kbit")
	time.sleep(0.346)
	tracef.write(f"1665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1665kbit")
	time.sleep(0.35)
	tracef.write(f"1743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1743kbit")
	time.sleep(0.294)
	tracef.write(f"1410 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1410kbit")
	time.sleep(0.459)
	tracef.write(f"1694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1694kbit")
	time.sleep(0.397)
	tracef.write(f"1717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1717kbit")
	time.sleep(0.517)
	tracef.write(f"1537 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1537kbit")
	time.sleep(0.43)
	tracef.write(f"1645 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1645kbit")
	time.sleep(0.396)
	tracef.write(f"1368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1368kbit")
	time.sleep(0.331)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()