#t:674-826 ; rate:276-1207 ; loss_0.0-0.0 ; delay:0-0
import os
import time
def link():
	tracef = open("traces/random/trace297.txt", 'w')
	tracef.close()
	tracef = open("traces/random/trace297.txt", 'a+')
	tracef.write(f"320 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc add dev lo root netem rate 320kbit")
	time.sleep(0.798)
	tracef.write(f"789 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 789kbit")
	time.sleep(0.822)
	tracef.write(f"689 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 689kbit")
	time.sleep(0.815)
	tracef.write(f"794 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 794kbit")
	time.sleep(0.787)
	tracef.write(f"931 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 931kbit")
	time.sleep(0.708)
	tracef.write(f"1087 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1087kbit")
	time.sleep(0.815)
	tracef.write(f"1201 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1201kbit")
	time.sleep(0.727)
	tracef.write(f"614 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 614kbit")
	time.sleep(0.703)
	tracef.write(f"619 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 619kbit")
	time.sleep(0.697)
	tracef.write(f"1140 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1140kbit")
	time.sleep(0.733)
	tracef.write(f"327 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 327kbit")
	time.sleep(0.711)
	tracef.write(f"517 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 517kbit")
	time.sleep(0.794)
	tracef.write(f"539 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 539kbit")
	time.sleep(0.72)
	tracef.write(f"877 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 877kbit")
	time.sleep(0.701)
	tracef.write(f"368 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 368kbit")
	time.sleep(0.807)
	tracef.write(f"364 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 364kbit")
	time.sleep(0.761)
	tracef.write(f"605 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 605kbit")
	time.sleep(0.816)
	tracef.write(f"1139 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1139kbit")
	time.sleep(0.733)
	tracef.write(f"942 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 942kbit")
	time.sleep(0.695)
	tracef.write(f"648 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 648kbit")
	time.sleep(0.712)
	tracef.write(f"731 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 731kbit")
	time.sleep(0.736)
	tracef.write(f"905 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 905kbit")
	time.sleep(0.79)
	tracef.write(f"684 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 684kbit")
	time.sleep(0.792)
	tracef.write(f"1055 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1055kbit")
	time.sleep(0.791)
	tracef.write(f"291 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 291kbit")
	time.sleep(0.798)
	tracef.write(f"927 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 927kbit")
	time.sleep(0.826)
	tracef.write(f"1032 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1032kbit")
	time.sleep(0.767)
	tracef.write(f"587 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 587kbit")
	time.sleep(0.803)
	tracef.write(f"897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 897kbit")
	time.sleep(0.822)
	tracef.write(f"283 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 283kbit")
	time.sleep(0.682)
	tracef.write(f"446 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 446kbit")
	time.sleep(0.801)
	tracef.write(f"827 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 827kbit")
	time.sleep(0.715)
	tracef.write(f"1103 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1103kbit")
	time.sleep(0.783)
	tracef.write(f"874 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 874kbit")
	time.sleep(0.736)
	tracef.write(f"782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 782kbit")
	time.sleep(0.799)
	tracef.write(f"1050 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1050kbit")
	time.sleep(0.766)
	tracef.write(f"409 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 409kbit")
	time.sleep(0.752)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.681)
	tracef.write(f"661 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 661kbit")
	time.sleep(0.771)
	tracef.write(f"569 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 569kbit")
	time.sleep(0.733)
	tracef.write(f"897 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 897kbit")
	time.sleep(0.809)
	tracef.write(f"479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 479kbit")
	time.sleep(0.682)
	tracef.write(f"513 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 513kbit")
	time.sleep(0.699)
	tracef.write(f"420 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 420kbit")
	time.sleep(0.793)
	tracef.write(f"555 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 555kbit")
	time.sleep(0.768)
	tracef.write(f"967 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 967kbit")
	time.sleep(0.76)
	tracef.write(f"744 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 744kbit")
	time.sleep(0.706)
	tracef.write(f"929 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 929kbit")
	time.sleep(0.73)
	tracef.write(f"472 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 472kbit")
	time.sleep(0.763)
	tracef.write(f"737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 737kbit")
	time.sleep(0.757)
	tracef.write(f"352 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 352kbit")
	time.sleep(0.748)
	tracef.write(f"1111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1111kbit")
	time.sleep(0.682)
	tracef.write(f"879 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 879kbit")
	time.sleep(0.711)
	tracef.write(f"477 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 477kbit")
	time.sleep(0.814)
	tracef.write(f"807 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 807kbit")
	time.sleep(0.697)
	tracef.write(f"655 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 655kbit")
	time.sleep(0.736)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(0.701)
	tracef.write(f"528 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 528kbit")
	time.sleep(0.727)
	tracef.write(f"873 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 873kbit")
	time.sleep(0.743)
	tracef.write(f"949 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 949kbit")
	time.sleep(0.688)
	tracef.write(f"732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 732kbit")
	time.sleep(0.724)
	tracef.write(f"916 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 916kbit")
	time.sleep(0.75)
	tracef.write(f"909 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 909kbit")
	time.sleep(0.696)
	tracef.write(f"286 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 286kbit")
	time.sleep(0.763)
	tracef.write(f"861 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 861kbit")
	time.sleep(0.782)
	tracef.write(f"743 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 743kbit")
	time.sleep(0.758)
	tracef.write(f"1131 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1131kbit")
	time.sleep(0.699)
	tracef.write(f"712 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 712kbit")
	time.sleep(0.768)
	tracef.write(f"846 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 846kbit")
	time.sleep(0.716)
	tracef.write(f"338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 338kbit")
	time.sleep(0.713)
	tracef.write(f"678 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 678kbit")
	time.sleep(0.679)
	tracef.write(f"298 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 298kbit")
	time.sleep(0.809)
	tracef.write(f"338 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 338kbit")
	time.sleep(0.765)
	tracef.write(f"856 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 856kbit")
	time.sleep(0.736)
	tracef.write(f"721 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 721kbit")
	time.sleep(0.769)
	tracef.write(f"459 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 459kbit")
	time.sleep(0.746)
	tracef.write(f"526 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 526kbit")
	time.sleep(0.808)
	tracef.write(f"529 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 529kbit")
	time.sleep(0.798)
	tracef.write(f"341 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 341kbit")
	time.sleep(0.75)
	tracef.write(f"975 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 975kbit")
	time.sleep(0.729)
	tracef.write(f"753 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 753kbit")
	time.sleep(0.803)
	tracef.write(f"591 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 591kbit")
	time.sleep(0.776)
	tracef.write(f"1190 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1190kbit")
	time.sleep(0.793)
	tracef.write(f"762 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 762kbit")
	time.sleep(0.729)
	tracef.write(f"575 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 575kbit")
	time.sleep(0.778)
	tracef.write(f"920 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 920kbit")
	time.sleep(0.771)
	tracef.write(f"609 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 609kbit")
	time.sleep(0.689)
	tracef.write(f"822 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 822kbit")
	time.sleep(0.79)
	tracef.write(f"427 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 427kbit")
	time.sleep(0.712)
	tracef.write(f"705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 705kbit")
	time.sleep(0.693)
	tracef.write(f"340 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 340kbit")
	time.sleep(0.795)
	tracef.write(f"281 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 281kbit")
	time.sleep(0.759)
	tracef.write(f"1206 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1206kbit")
	time.sleep(0.74)
	tracef.write(f"457 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 457kbit")
	time.sleep(0.675)
	tracef.write(f"570 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 570kbit")
	time.sleep(0.705)
	tracef.write(f"1042 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1042kbit")
	time.sleep(0.826)
	tracef.write(f"561 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 561kbit")
	time.sleep(0.749)
	tracef.write(f"449 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 449kbit")
	time.sleep(0.75)
	tracef.write(f"859 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 859kbit")
	time.sleep(0.755)
	tracef.write(f"1095 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1095kbit")
	time.sleep(0.772)
	tracef.write(f"698 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 698kbit")
	time.sleep(0.724)
	tracef.write(f"374 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 374kbit")
	time.sleep(0.804)
	tracef.write(f"1178 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1178kbit")
	time.sleep(0.728)
	tracef.write(f"738 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 738kbit")
	time.sleep(0.681)
	tracef.write(f"719 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 719kbit")
	time.sleep(0.705)
	tracef.write(f"705 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 705kbit")
	time.sleep(0.741)
	tracef.write(f"929 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 929kbit")
	time.sleep(0.683)
	tracef.write(f"896 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 896kbit")
	time.sleep(0.726)
	tracef.write(f"621 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 621kbit")
	time.sleep(0.688)
	tracef.write(f"940 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 940kbit")
	time.sleep(0.769)
	tracef.write(f"782 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 782kbit")
	time.sleep(0.697)
	tracef.write(f"567 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 567kbit")
	time.sleep(0.798)
	tracef.write(f"680 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 680kbit")
	time.sleep(0.777)
	tracef.write(f"1111 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1111kbit")
	time.sleep(0.799)
	tracef.write(f"768 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 768kbit")
	time.sleep(0.751)
	tracef.write(f"960 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 960kbit")
	time.sleep(0.695)
	tracef.write(f"602 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 602kbit")
	time.sleep(0.799)
	tracef.write(f"943 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 943kbit")
	time.sleep(0.784)
	tracef.write(f"436 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 436kbit")
	time.sleep(0.7)
	tracef.write(f"556 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 556kbit")
	time.sleep(0.751)
	tracef.write(f"679 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 679kbit")
	time.sleep(0.696)
	tracef.write(f"769 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 769kbit")
	time.sleep(0.703)
	tracef.write(f"675 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 675kbit")
	time.sleep(0.737)
	tracef.write(f"312 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 312kbit")
	time.sleep(0.808)
	tracef.write(f"417 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 417kbit")
	time.sleep(0.811)
	tracef.write(f"1085 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1085kbit")
	time.sleep(0.679)
	tracef.write(f"737 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 737kbit")
	time.sleep(0.678)
	tracef.write(f"1154 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1154kbit")
	time.sleep(0.823)
	tracef.write(f"732 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 732kbit")
	time.sleep(0.773)
	tracef.write(f"1176 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1176kbit")
	time.sleep(0.681)
	tracef.write(f"1057 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1057kbit")
	time.sleep(0.724)
	tracef.write(f"479 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 479kbit")
	time.sleep(0.73)
	tracef.write(f"1090 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 1090kbit")
	time.sleep(0.748)
	tracef.write(f"841 ; {round(time.time() * 1000)}\n")
	os.system("echo 1 | sudo -S tc qdisc change dev lo root netem rate 841kbit")
	time.sleep(0.794)
	os.system("echo 1 | sudo -S tc qdisc del dev lo root")
	tracef.close()
def main():
	link()
if __name__ == "__main__":
	main()