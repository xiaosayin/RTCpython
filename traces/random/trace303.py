#t:370-535 ; rate:2680-2789 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace303.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace303.txt", 'a+')
	tracef.write(f"2695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2695kbit")
	time.sleep(0.416)
	tracef.write(f"2722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2722kbit")
	time.sleep(0.455)
	tracef.write(f"2729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2729kbit")
	time.sleep(0.482)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.399)
	tracef.write(f"2767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2767kbit")
	time.sleep(0.395)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.408)
	tracef.write(f"2699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2699kbit")
	time.sleep(0.428)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.418)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.394)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.431)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.501)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.502)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.409)
	tracef.write(f"2728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2728kbit")
	time.sleep(0.41)
	tracef.write(f"2760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2760kbit")
	time.sleep(0.5)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.49)
	tracef.write(f"2777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2777kbit")
	time.sleep(0.377)
	tracef.write(f"2680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2680kbit")
	time.sleep(0.474)
	tracef.write(f"2787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2787kbit")
	time.sleep(0.532)
	tracef.write(f"2713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2713kbit")
	time.sleep(0.44)
	tracef.write(f"2754 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2754kbit")
	time.sleep(0.505)
	tracef.write(f"2698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2698kbit")
	time.sleep(0.471)
	tracef.write(f"2696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2696kbit")
	time.sleep(0.382)
	tracef.write(f"2713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2713kbit")
	time.sleep(0.489)
	tracef.write(f"2762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2762kbit")
	time.sleep(0.45)
	tracef.write(f"2743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2743kbit")
	time.sleep(0.449)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.446)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.531)
	tracef.write(f"2707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2707kbit")
	time.sleep(0.436)
	tracef.write(f"2721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2721kbit")
	time.sleep(0.436)
	tracef.write(f"2741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2741kbit")
	time.sleep(0.457)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.461)
	tracef.write(f"2699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2699kbit")
	time.sleep(0.39)
	tracef.write(f"2692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2692kbit")
	time.sleep(0.383)
	tracef.write(f"2716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2716kbit")
	time.sleep(0.409)
	tracef.write(f"2722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2722kbit")
	time.sleep(0.376)
	tracef.write(f"2682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2682kbit")
	time.sleep(0.43)
	tracef.write(f"2695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2695kbit")
	time.sleep(0.521)
	tracef.write(f"2732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2732kbit")
	time.sleep(0.462)
	tracef.write(f"2710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2710kbit")
	time.sleep(0.407)
	tracef.write(f"2711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2711kbit")
	time.sleep(0.465)
	tracef.write(f"2706 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2706kbit")
	time.sleep(0.393)
	tracef.write(f"2752 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2752kbit")
	time.sleep(0.471)
	tracef.write(f"2701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2701kbit")
	time.sleep(0.512)
	tracef.write(f"2707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2707kbit")
	time.sleep(0.46)
	tracef.write(f"2782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2782kbit")
	time.sleep(0.38)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.5)
	tracef.write(f"2704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2704kbit")
	time.sleep(0.371)
	tracef.write(f"2719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2719kbit")
	time.sleep(0.436)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.476)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.409)
	tracef.write(f"2694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2694kbit")
	time.sleep(0.502)
	tracef.write(f"2707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2707kbit")
	time.sleep(0.374)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.414)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.477)
	tracef.write(f"2722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2722kbit")
	time.sleep(0.392)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.462)
	tracef.write(f"2710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2710kbit")
	time.sleep(0.399)
	tracef.write(f"2709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2709kbit")
	time.sleep(0.37)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.401)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.467)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.485)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.496)
	tracef.write(f"2702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2702kbit")
	time.sleep(0.449)
	tracef.write(f"2704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2704kbit")
	time.sleep(0.508)
	tracef.write(f"2719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2719kbit")
	time.sleep(0.438)
	tracef.write(f"2752 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2752kbit")
	time.sleep(0.517)
	tracef.write(f"2703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2703kbit")
	time.sleep(0.384)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.465)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.471)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.478)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.4)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.528)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.385)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.376)
	tracef.write(f"2709 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2709kbit")
	time.sleep(0.463)
	tracef.write(f"2691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2691kbit")
	time.sleep(0.479)
	tracef.write(f"2702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2702kbit")
	time.sleep(0.4)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.377)
	tracef.write(f"2717 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2717kbit")
	time.sleep(0.526)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.499)
	tracef.write(f"2780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2780kbit")
	time.sleep(0.473)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.389)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.406)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.484)
	tracef.write(f"2760 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2760kbit")
	time.sleep(0.508)
	tracef.write(f"2731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2731kbit")
	time.sleep(0.474)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.443)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.486)
	tracef.write(f"2691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2691kbit")
	time.sleep(0.503)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.494)
	tracef.write(f"2779 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2779kbit")
	time.sleep(0.525)
	tracef.write(f"2707 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2707kbit")
	time.sleep(0.419)
	tracef.write(f"2682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2682kbit")
	time.sleep(0.512)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.4)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.519)
	tracef.write(f"2740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2740kbit")
	time.sleep(0.432)
	tracef.write(f"2705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2705kbit")
	time.sleep(0.47)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.463)
	tracef.write(f"2724 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2724kbit")
	time.sleep(0.378)
	tracef.write(f"2712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2712kbit")
	time.sleep(0.433)
	tracef.write(f"2714 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2714kbit")
	time.sleep(0.461)
	tracef.write(f"2757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2757kbit")
	time.sleep(0.507)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.497)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.418)
	tracef.write(f"2726 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2726kbit")
	time.sleep(0.515)
	tracef.write(f"2756 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2756kbit")
	time.sleep(0.437)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.493)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.501)
	tracef.write(f"2738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2738kbit")
	time.sleep(0.38)
	tracef.write(f"2692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2692kbit")
	time.sleep(0.471)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.435)
	tracef.write(f"2683 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2683kbit")
	time.sleep(0.45)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.48)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.394)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.377)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.493)
	tracef.write(f"2718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2718kbit")
	time.sleep(0.495)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.423)
	tracef.write(f"2732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2732kbit")
	time.sleep(0.451)
	tracef.write(f"2757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2757kbit")
	time.sleep(0.514)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.383)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.431)
	tracef.write(f"2701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2701kbit")
	time.sleep(0.386)
	tracef.write(f"2754 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2754kbit")
	time.sleep(0.492)
	tracef.write(f"2708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2708kbit")
	time.sleep(0.535)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.485)
	tracef.write(f"2685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2685kbit")
	time.sleep(0.531)
	tracef.write(f"2704 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2704kbit")
	time.sleep(0.399)
	tracef.write(f"2780 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2780kbit")
	time.sleep(0.465)
	tracef.write(f"2718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2718kbit")
	time.sleep(0.425)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.432)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.38)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.435)
	tracef.write(f"2696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2696kbit")
	time.sleep(0.45)
	tracef.write(f"2697 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2697kbit")
	time.sleep(0.482)
	tracef.write(f"2779 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2779kbit")
	time.sleep(0.496)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.377)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.481)
	tracef.write(f"2695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2695kbit")
	time.sleep(0.406)
	tracef.write(f"2734 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2734kbit")
	time.sleep(0.51)
	tracef.write(f"2710 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2710kbit")
	time.sleep(0.403)
	tracef.write(f"2688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2688kbit")
	time.sleep(0.485)
	tracef.write(f"2785 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2785kbit")
	time.sleep(0.399)
	tracef.write(f"2729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2729kbit")
	time.sleep(0.533)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.482)
	tracef.write(f"2784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2784kbit")
	time.sleep(0.414)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.387)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.457)
	tracef.write(f"2689 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2689kbit")
	time.sleep(0.512)
	tracef.write(f"2685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2685kbit")
	time.sleep(0.533)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.392)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.522)
	tracef.write(f"2743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2743kbit")
	time.sleep(0.383)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.492)
	tracef.write(f"2729 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2729kbit")
	time.sleep(0.371)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.406)
	tracef.write(f"2711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2711kbit")
	time.sleep(0.476)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.379)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.417)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.44)
	tracef.write(f"2782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2782kbit")
	time.sleep(0.474)
	tracef.write(f"2776 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2776kbit")
	time.sleep(0.483)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.499)
	tracef.write(f"2784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2784kbit")
	time.sleep(0.525)
	tracef.write(f"2695 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2695kbit")
	time.sleep(0.467)
	tracef.write(f"2698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2698kbit")
	time.sleep(0.39)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.482)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.494)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.453)
	tracef.write(f"2766 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2766kbit")
	time.sleep(0.481)
	tracef.write(f"2718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2718kbit")
	time.sleep(0.4)
	tracef.write(f"2715 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2715kbit")
	time.sleep(0.504)
	tracef.write(f"2718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2718kbit")
	time.sleep(0.507)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.384)
	tracef.write(f"2688 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2688kbit")
	time.sleep(0.481)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.373)
	tracef.write(f"2682 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2682kbit")
	time.sleep(0.529)
	tracef.write(f"2784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2784kbit")
	time.sleep(0.4)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.517)
	tracef.write(f"2781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2781kbit")
	time.sleep(0.518)
	tracef.write(f"2777 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2777kbit")
	time.sleep(0.498)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.501)
	tracef.write(f"2687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2687kbit")
	time.sleep(0.462)
	tracef.write(f"2680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2680kbit")
	time.sleep(0.439)
	tracef.write(f"2784 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2784kbit")
	time.sleep(0.51)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.533)
	tracef.write(f"2720 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2720kbit")
	time.sleep(0.461)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.429)
	tracef.write(f"2687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2687kbit")
	time.sleep(0.432)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.434)
	tracef.write(f"2694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2694kbit")
	time.sleep(0.394)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.442)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.42)
	tracef.write(f"2787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2787kbit")
	time.sleep(0.52)
	tracef.write(f"2731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2731kbit")
	time.sleep(0.46)
	tracef.write(f"2768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2768kbit")
	time.sleep(0.416)
	tracef.write(f"2783 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2783kbit")
	time.sleep(0.53)
	tracef.write(f"2701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2701kbit")
	time.sleep(0.389)
	tracef.write(f"2769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2769kbit")
	time.sleep(0.512)
	tracef.write(f"2680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2680kbit")
	time.sleep(0.533)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.455)
	tracef.write(f"2691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2691kbit")
	time.sleep(0.403)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.514)
	tracef.write(f"2787 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2787kbit")
	time.sleep(0.533)
	tracef.write(f"2685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2685kbit")
	time.sleep(0.386)
	tracef.write(f"2773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2773kbit")
	time.sleep(0.504)
	tracef.write(f"2712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2712kbit")
	time.sleep(0.441)
	tracef.write(f"2699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2699kbit")
	time.sleep(0.5)
	tracef.write(f"2703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2703kbit")
	time.sleep(0.413)
	tracef.write(f"2745 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2745kbit")
	time.sleep(0.433)
	tracef.write(f"2781 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2781kbit")
	time.sleep(0.407)
	tracef.write(f"2751 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2751kbit")
	time.sleep(0.478)
	tracef.write(f"2703 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2703kbit")
	time.sleep(0.481)
	tracef.write(f"2692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2692kbit")
	time.sleep(0.375)
	tracef.write(f"2681 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2681kbit")
	time.sleep(0.397)
	tracef.write(f"2702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2702kbit")
	time.sleep(0.453)
	tracef.write(f"2741 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2741kbit")
	time.sleep(0.516)
	tracef.write(f"2694 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2694kbit")
	time.sleep(0.462)
	tracef.write(f"2785 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2785kbit")
	time.sleep(0.374)
	tracef.write(f"2747 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2747kbit")
	time.sleep(0.463)
	tracef.write(f"2708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2708kbit")
	time.sleep(0.419)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()