#t:780-899 ; rate:2733-2779 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace63.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace63.txt", 'a+')
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2744kbit")
	time.sleep(0.884)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.862)
	tracef.write(f"2738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2738kbit")
	time.sleep(0.807)
	tracef.write(f"2740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2740kbit")
	time.sleep(0.789)
	tracef.write(f"2770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2770kbit")
	time.sleep(0.898)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.836)
	tracef.write(f"2759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2759kbit")
	time.sleep(0.852)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.831)
	tracef.write(f"2756 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2756kbit")
	time.sleep(0.829)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.804)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.851)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.845)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.856)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.867)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.789)
	tracef.write(f"2759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2759kbit")
	time.sleep(0.886)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.85)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.814)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.786)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.877)
	tracef.write(f"2759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2759kbit")
	time.sleep(0.783)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.895)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.851)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.847)
	tracef.write(f"2738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2738kbit")
	time.sleep(0.848)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.812)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.796)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.816)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.848)
	tracef.write(f"2745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2745kbit")
	time.sleep(0.811)
	tracef.write(f"2768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2768kbit")
	time.sleep(0.849)
	tracef.write(f"2759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2759kbit")
	time.sleep(0.869)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.865)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.852)
	tracef.write(f"2743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2743kbit")
	time.sleep(0.787)
	tracef.write(f"2743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2743kbit")
	time.sleep(0.842)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.818)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.792)
	tracef.write(f"2741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2741kbit")
	time.sleep(0.856)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.895)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.846)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.808)
	tracef.write(f"2776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2776kbit")
	time.sleep(0.887)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.855)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.86)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.887)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.854)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.868)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.795)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.802)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.807)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.866)
	tracef.write(f"2756 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2756kbit")
	time.sleep(0.842)
	tracef.write(f"2743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2743kbit")
	time.sleep(0.78)
	tracef.write(f"2770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2770kbit")
	time.sleep(0.797)
	tracef.write(f"2777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2777kbit")
	time.sleep(0.827)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.851)
	tracef.write(f"2745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2745kbit")
	time.sleep(0.826)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.844)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.85)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.798)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.817)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.811)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.867)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.868)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.852)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.791)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.83)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.882)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.81)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.802)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.837)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.866)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.833)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.854)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.841)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.88)
	tracef.write(f"2739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2739kbit")
	time.sleep(0.838)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.884)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.882)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.79)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.87)
	tracef.write(f"2745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2745kbit")
	time.sleep(0.81)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.869)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.88)
	tracef.write(f"2767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2767kbit")
	time.sleep(0.832)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.832)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.853)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.794)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.883)
	tracef.write(f"2770 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2770kbit")
	time.sleep(0.815)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.815)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.887)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.863)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.792)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.81)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.859)
	tracef.write(f"2745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2745kbit")
	time.sleep(0.784)
	tracef.write(f"2737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2737kbit")
	time.sleep(0.837)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.856)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.87)
	tracef.write(f"2760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2760kbit")
	time.sleep(0.845)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.796)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.89)
	tracef.write(f"2757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2757kbit")
	time.sleep(0.826)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.883)
	tracef.write(f"2759 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2759kbit")
	time.sleep(0.794)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.892)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.896)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.868)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.855)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.849)
	tracef.write(f"2776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2776kbit")
	time.sleep(0.832)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.863)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.879)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.802)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.786)
	tracef.write(f"2768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2768kbit")
	time.sleep(0.859)
	tracef.write(f"2767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2767kbit")
	time.sleep(0.87)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()