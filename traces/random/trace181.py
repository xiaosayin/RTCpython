#t:303-553 ; rate:2613-2831 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace181.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace181.txt", 'a+')
	tracef.write(f"2804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 2804kbit")
	time.sleep(0.394)
	tracef.write(f"2655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2655kbit")
	time.sleep(0.466)
	tracef.write(f"2822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2822kbit")
	time.sleep(0.424)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.332)
	tracef.write(f"2706 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2706kbit")
	time.sleep(0.312)
	tracef.write(f"2739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2739kbit")
	time.sleep(0.414)
	tracef.write(f"2740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2740kbit")
	time.sleep(0.524)
	tracef.write(f"2809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2809kbit")
	time.sleep(0.516)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.414)
	tracef.write(f"2641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2641kbit")
	time.sleep(0.322)
	tracef.write(f"2828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2828kbit")
	time.sleep(0.49)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.537)
	tracef.write(f"2793 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2793kbit")
	time.sleep(0.401)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.475)
	tracef.write(f"2644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2644kbit")
	time.sleep(0.49)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.305)
	tracef.write(f"2818 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2818kbit")
	time.sleep(0.328)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.344)
	tracef.write(f"2757 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2757kbit")
	time.sleep(0.496)
	tracef.write(f"2665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2665kbit")
	time.sleep(0.493)
	tracef.write(f"2624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2624kbit")
	time.sleep(0.429)
	tracef.write(f"2677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2677kbit")
	time.sleep(0.481)
	tracef.write(f"2644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2644kbit")
	time.sleep(0.504)
	tracef.write(f"2692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2692kbit")
	time.sleep(0.31)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.414)
	tracef.write(f"2822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2822kbit")
	time.sleep(0.407)
	tracef.write(f"2713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2713kbit")
	time.sleep(0.474)
	tracef.write(f"2827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2827kbit")
	time.sleep(0.432)
	tracef.write(f"2614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2614kbit")
	time.sleep(0.546)
	tracef.write(f"2828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2828kbit")
	time.sleep(0.314)
	tracef.write(f"2655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2655kbit")
	time.sleep(0.42)
	tracef.write(f"2797 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2797kbit")
	time.sleep(0.331)
	tracef.write(f"2771 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2771kbit")
	time.sleep(0.396)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.364)
	tracef.write(f"2737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2737kbit")
	time.sleep(0.324)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.34)
	tracef.write(f"2789 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2789kbit")
	time.sleep(0.337)
	tracef.write(f"2723 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2723kbit")
	time.sleep(0.465)
	tracef.write(f"2636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2636kbit")
	time.sleep(0.517)
	tracef.write(f"2685 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2685kbit")
	time.sleep(0.499)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.447)
	tracef.write(f"2640 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2640kbit")
	time.sleep(0.317)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.421)
	tracef.write(f"2636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2636kbit")
	time.sleep(0.406)
	tracef.write(f"2739 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2739kbit")
	time.sleep(0.341)
	tracef.write(f"2668 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2668kbit")
	time.sleep(0.503)
	tracef.write(f"2767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2767kbit")
	time.sleep(0.307)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.406)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.382)
	tracef.write(f"2794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2794kbit")
	time.sleep(0.546)
	tracef.write(f"2716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2716kbit")
	time.sleep(0.492)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.305)
	tracef.write(f"2629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2629kbit")
	time.sleep(0.534)
	tracef.write(f"2708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2708kbit")
	time.sleep(0.53)
	tracef.write(f"2651 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2651kbit")
	time.sleep(0.435)
	tracef.write(f"2620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2620kbit")
	time.sleep(0.411)
	tracef.write(f"2660 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2660kbit")
	time.sleep(0.318)
	tracef.write(f"2631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2631kbit")
	time.sleep(0.505)
	tracef.write(f"2815 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2815kbit")
	time.sleep(0.462)
	tracef.write(f"2689 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2689kbit")
	time.sleep(0.34)
	tracef.write(f"2650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2650kbit")
	time.sleep(0.309)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.426)
	tracef.write(f"2801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2801kbit")
	time.sleep(0.493)
	tracef.write(f"2711 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2711kbit")
	time.sleep(0.338)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.404)
	tracef.write(f"2671 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2671kbit")
	time.sleep(0.46)
	tracef.write(f"2801 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2801kbit")
	time.sleep(0.449)
	tracef.write(f"2624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2624kbit")
	time.sleep(0.338)
	tracef.write(f"2718 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2718kbit")
	time.sleep(0.544)
	tracef.write(f"2722 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2722kbit")
	time.sleep(0.34)
	tracef.write(f"2708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2708kbit")
	time.sleep(0.304)
	tracef.write(f"2635 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2635kbit")
	time.sleep(0.528)
	tracef.write(f"2649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2649kbit")
	time.sleep(0.374)
	tracef.write(f"2687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2687kbit")
	time.sleep(0.399)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.473)
	tracef.write(f"2618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2618kbit")
	time.sleep(0.448)
	tracef.write(f"2799 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2799kbit")
	time.sleep(0.472)
	tracef.write(f"2813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2813kbit")
	time.sleep(0.527)
	tracef.write(f"2634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2634kbit")
	time.sleep(0.502)
	tracef.write(f"2809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2809kbit")
	time.sleep(0.408)
	tracef.write(f"2667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2667kbit")
	time.sleep(0.303)
	tracef.write(f"2796 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2796kbit")
	time.sleep(0.498)
	tracef.write(f"2641 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2641kbit")
	time.sleep(0.54)
	tracef.write(f"2738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2738kbit")
	time.sleep(0.506)
	tracef.write(f"2648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2648kbit")
	time.sleep(0.369)
	tracef.write(f"2764 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2764kbit")
	time.sleep(0.331)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.43)
	tracef.write(f"2794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2794kbit")
	time.sleep(0.314)
	tracef.write(f"2633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2633kbit")
	time.sleep(0.434)
	tracef.write(f"2804 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2804kbit")
	time.sleep(0.453)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.408)
	tracef.write(f"2786 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2786kbit")
	time.sleep(0.373)
	tracef.write(f"2714 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2714kbit")
	time.sleep(0.46)
	tracef.write(f"2746 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2746kbit")
	time.sleep(0.328)
	tracef.write(f"2708 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2708kbit")
	time.sleep(0.429)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.534)
	tracef.write(f"2653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2653kbit")
	time.sleep(0.404)
	tracef.write(f"2720 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2720kbit")
	time.sleep(0.536)
	tracef.write(f"2696 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2696kbit")
	time.sleep(0.472)
	tracef.write(f"2699 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2699kbit")
	time.sleep(0.488)
	tracef.write(f"2637 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2637kbit")
	time.sleep(0.372)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.417)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.418)
	tracef.write(f"2653 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2653kbit")
	time.sleep(0.466)
	tracef.write(f"2628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2628kbit")
	time.sleep(0.453)
	tracef.write(f"2649 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2649kbit")
	time.sleep(0.407)
	tracef.write(f"2624 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2624kbit")
	time.sleep(0.452)
	tracef.write(f"2732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2732kbit")
	time.sleep(0.406)
	tracef.write(f"2686 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2686kbit")
	time.sleep(0.397)
	tracef.write(f"2812 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2812kbit")
	time.sleep(0.312)
	tracef.write(f"2629 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2629kbit")
	time.sleep(0.519)
	tracef.write(f"2693 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2693kbit")
	time.sleep(0.514)
	tracef.write(f"2669 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2669kbit")
	time.sleep(0.421)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.391)
	tracef.write(f"2636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2636kbit")
	time.sleep(0.305)
	tracef.write(f"2805 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2805kbit")
	time.sleep(0.345)
	tracef.write(f"2659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2659kbit")
	time.sleep(0.493)
	tracef.write(f"2727 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2727kbit")
	time.sleep(0.321)
	tracef.write(f"2828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2828kbit")
	time.sleep(0.35)
	tracef.write(f"2705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2705kbit")
	time.sleep(0.344)
	tracef.write(f"2798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2798kbit")
	time.sleep(0.356)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.328)
	tracef.write(f"2687 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2687kbit")
	time.sleep(0.345)
	tracef.write(f"2716 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2716kbit")
	time.sleep(0.534)
	tracef.write(f"2679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2679kbit")
	time.sleep(0.523)
	tracef.write(f"2816 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2816kbit")
	time.sleep(0.372)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.513)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.517)
	tracef.write(f"2773 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2773kbit")
	time.sleep(0.537)
	tracef.write(f"2791 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2791kbit")
	time.sleep(0.314)
	tracef.write(f"2690 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2690kbit")
	time.sleep(0.507)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.344)
	tracef.write(f"2644 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2644kbit")
	time.sleep(0.51)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.307)
	tracef.write(f"2639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2639kbit")
	time.sleep(0.305)
	tracef.write(f"2755 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2755kbit")
	time.sleep(0.517)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.341)
	tracef.write(f"2691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2691kbit")
	time.sleep(0.438)
	tracef.write(f"2719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2719kbit")
	time.sleep(0.364)
	tracef.write(f"2721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2721kbit")
	time.sleep(0.547)
	tracef.write(f"2778 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2778kbit")
	time.sleep(0.448)
	tracef.write(f"2680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2680kbit")
	time.sleep(0.38)
	tracef.write(f"2817 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2817kbit")
	time.sleep(0.499)
	tracef.write(f"2813 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2813kbit")
	time.sleep(0.349)
	tracef.write(f"2657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2657kbit")
	time.sleep(0.314)
	tracef.write(f"2750 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2750kbit")
	time.sleep(0.353)
	tracef.write(f"2828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2828kbit")
	time.sleep(0.51)
	tracef.write(f"2643 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2643kbit")
	time.sleep(0.486)
	tracef.write(f"2698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2698kbit")
	time.sleep(0.447)
	tracef.write(f"2820 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2820kbit")
	time.sleep(0.458)
	tracef.write(f"2800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2800kbit")
	time.sleep(0.55)
	tracef.write(f"2667 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2667kbit")
	time.sleep(0.436)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.52)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.352)
	tracef.write(f"2701 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2701kbit")
	time.sleep(0.512)
	tracef.write(f"2830 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2830kbit")
	time.sleep(0.545)
	tracef.write(f"2792 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2792kbit")
	time.sleep(0.471)
	tracef.write(f"2767 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2767kbit")
	time.sleep(0.461)
	tracef.write(f"2713 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2713kbit")
	time.sleep(0.384)
	tracef.write(f"2691 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2691kbit")
	time.sleep(0.467)
	tracef.write(f"2798 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2798kbit")
	time.sleep(0.33)
	tracef.write(f"2647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2647kbit")
	time.sleep(0.447)
	tracef.write(f"2735 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2735kbit")
	time.sleep(0.34)
	tracef.write(f"2618 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2618kbit")
	time.sleep(0.416)
	tracef.write(f"2648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2648kbit")
	time.sleep(0.548)
	tracef.write(f"2656 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2656kbit")
	time.sleep(0.431)
	tracef.write(f"2632 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2632kbit")
	time.sleep(0.542)
	tracef.write(f"2673 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2673kbit")
	time.sleep(0.452)
	tracef.write(f"2806 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2806kbit")
	time.sleep(0.544)
	tracef.write(f"2689 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2689kbit")
	time.sleep(0.438)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.495)
	tracef.write(f"2737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2737kbit")
	time.sleep(0.337)
	tracef.write(f"2634 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2634kbit")
	time.sleep(0.394)
	tracef.write(f"2693 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2693kbit")
	time.sleep(0.324)
	tracef.write(f"2733 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2733kbit")
	time.sleep(0.429)
	tracef.write(f"2827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2827kbit")
	time.sleep(0.524)
	tracef.write(f"2775 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2775kbit")
	time.sleep(0.362)
	tracef.write(f"2725 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2725kbit")
	time.sleep(0.313)
	tracef.write(f"2670 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2670kbit")
	time.sleep(0.438)
	tracef.write(f"2829 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2829kbit")
	time.sleep(0.475)
	tracef.write(f"2619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2619kbit")
	time.sleep(0.369)
	tracef.write(f"2647 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2647kbit")
	time.sleep(0.396)
	tracef.write(f"2744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2744kbit")
	time.sleep(0.449)
	tracef.write(f"2742 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2742kbit")
	time.sleep(0.54)
	tracef.write(f"2639 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2639kbit")
	time.sleep(0.357)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.543)
	tracef.write(f"2636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2636kbit")
	time.sleep(0.388)
	tracef.write(f"2715 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2715kbit")
	time.sleep(0.416)
	tracef.write(f"2628 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2628kbit")
	time.sleep(0.365)
	tracef.write(f"2827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2827kbit")
	time.sleep(0.397)
	tracef.write(f"2636 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2636kbit")
	time.sleep(0.487)
	tracef.write(f"2620 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2620kbit")
	time.sleep(0.536)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.364)
	tracef.write(f"2800 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2800kbit")
	time.sleep(0.472)
	tracef.write(f"2748 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2748kbit")
	time.sleep(0.511)
	tracef.write(f"2659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2659kbit")
	time.sleep(0.385)
	tracef.write(f"2659 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2659kbit")
	time.sleep(0.316)
	tracef.write(f"2761 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2761kbit")
	time.sleep(0.312)
	tracef.write(f"2679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2679kbit")
	time.sleep(0.34)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.325)
	tracef.write(f"2763 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2763kbit")
	time.sleep(0.456)
	tracef.write(f"2702 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2702kbit")
	time.sleep(0.411)
	tracef.write(f"2623 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2623kbit")
	time.sleep(0.468)
	tracef.write(f"2753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2753kbit")
	time.sleep(0.515)
	tracef.write(f"2626 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2626kbit")
	time.sleep(0.373)
	tracef.write(f"2650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2650kbit")
	time.sleep(0.5)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.351)
	tracef.write(f"2740 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2740kbit")
	time.sleep(0.439)
	tracef.write(f"2650 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2650kbit")
	time.sleep(0.457)
	tracef.write(f"2749 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2749kbit")
	time.sleep(0.363)
	tracef.write(f"2721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2721kbit")
	time.sleep(0.47)
	tracef.write(f"2737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2737kbit")
	time.sleep(0.391)
	tracef.write(f"2692 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2692kbit")
	time.sleep(0.493)
	tracef.write(f"2615 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2615kbit")
	time.sleep(0.334)
	tracef.write(f"2811 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2811kbit")
	time.sleep(0.513)
	tracef.write(f"2758 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2758kbit")
	time.sleep(0.501)
	tracef.write(f"2728 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2728kbit")
	time.sleep(0.434)
	tracef.write(f"2736 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2736kbit")
	time.sleep(0.443)
	tracef.write(f"2774 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2774kbit")
	time.sleep(0.315)
	tracef.write(f"2809 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2809kbit")
	time.sleep(0.312)
	tracef.write(f"2684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2684kbit")
	time.sleep(0.394)
	tracef.write(f"2658 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2658kbit")
	time.sleep(0.421)
	tracef.write(f"2657 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2657kbit")
	time.sleep(0.32)
	tracef.write(f"2765 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2765kbit")
	time.sleep(0.307)
	tracef.write(f"2677 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2677kbit")
	time.sleep(0.432)
	tracef.write(f"2661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2661kbit")
	time.sleep(0.443)
	tracef.write(f"2828 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2828kbit")
	time.sleep(0.33)
	tracef.write(f"2715 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2715kbit")
	time.sleep(0.423)
	tracef.write(f"2782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2782kbit")
	time.sleep(0.363)
	tracef.write(f"2721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2721kbit")
	time.sleep(0.447)
	tracef.write(f"2646 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2646kbit")
	time.sleep(0.461)
	tracef.write(f"2631 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2631kbit")
	time.sleep(0.413)
	tracef.write(f"2633 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2633kbit")
	time.sleep(0.443)
	tracef.write(f"2772 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2772kbit")
	time.sleep(0.318)
	tracef.write(f"2700 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2700kbit")
	time.sleep(0.411)
	tracef.write(f"2790 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2790kbit")
	time.sleep(0.422)
	tracef.write(f"2665 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 2665kbit")
	time.sleep(0.497)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()