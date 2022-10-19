import matplotlib.pyplot as plt
def plt_reward_record(record_episode_reward, record_episode_reward1, \
        record_episode_reward2, record_episode_reward3, record_episode_reward4, \
                      record_episode_reward5, record_episode_reward6, record_episode_reward7,figPath):
    plt.cla()
    plt.plot(range(len(record_episode_reward)), record_episode_reward, alpha = 0.7, label='reward', color = 'red')
    plt.plot(range(len(record_episode_reward1)), record_episode_reward1, alpha = 0.7, label='recv_rate', color = 'blue')
    plt.plot(range(len(record_episode_reward2)), record_episode_reward2, alpha = 0.7, label='delay', color = 'green')
    plt.plot(range(len(record_episode_reward3)), record_episode_reward3, alpha = 0.7, label='loss', color = 'grey')
    plt.plot(range(len(record_episode_reward4)), record_episode_reward4, alpha = 0.7, label='frameDelay', color = 'purple')
    plt.plot(range(len(record_episode_reward5)), record_episode_reward5, alpha=0.7, label='active_loss', color='yellow')
    plt.plot(range(len(record_episode_reward6)), record_episode_reward6, alpha=0.7, label='diff_active_loss', color='pink')
    plt.plot(range(len(record_episode_reward7)), record_episode_reward7, alpha=0.7, label='reward_diff_bwe', color='black')
    plt.legend()
    plt.xlabel('Episode')
    plt.ylabel('Averaged episode reward')
    plt.grid()
    plt.savefig(figPath)


def plt_reward_rate(rewardList, rRateList, figPath):
    plt.cla()
    plt.plot(range(len(rewardList)), rewardList,  label='reward', alpha = 0.3, color = 'red')
    plt.plot(range(len(rRateList)), rRateList, label='recv_rate', alpha = 0.3, color = 'blue')
    plt.legend()
    plt.xlabel('action')
    plt.ylabel('reward')
    plt.grid()
    plt.savefig(figPath)

def plt_rate_pdf(intrRateList, figPath):
    plt.cla()
    a = 10
    bins = int((max(intrRateList) - min(intrRateList)) / a)
    plt.hist(intrRateList, bins, density=1, stacked=True)
    plt.xticks(list(range(min(intrRateList), max(intrRateList)))[::200])
    plt.xlabel("rate")
    plt.ylabel("num")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(figPath)

def plt_rate_cdf(intrRateList, figPath):
    plt.cla()
    a = 10
    bins = int((max(intrRateList) - min(intrRateList)) / a)
    plt.hist(intrRateList, bins, density=1, stacked=True, cumulative=True)
    plt.xticks(list(range(min(intrRateList), max(intrRateList)))[::200])
    plt.xlabel("rate")
    plt.ylabel("num")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(figPath)

def plt_track(plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, \
           plotRecvT, plotRecv, mahiT, mahiRate, figPath):
    plt.cla()

    plt.figure(figsize=(12,7))
    plt.plot(plotTargetT, plotTarget, alpha = 0.5, label='vp8 rate', color = 'green')
    plt.plot(plotEncT, plotEnc, alpha = 0.4, label='actual rate', color = 'red')
    plt.plot(plotSetT, plotSet, alpha = 0.4, label='gcc rate', color='blue')
    # plt.plot(plotTraceT, plotTrace, alpha = 0.5, label='network bandwidth', color='grey')
    plt.plot(plotRecvT, plotRecv, alpha = 0.5, label='recv rate', color='orange')
    plt.step(mahiT, mahiRate, alpha = 0.6, label='network bandwidth', color='grey')
    for i in plotRecv:
        print("plotRecv: ", plotRecv)
    plt.legend(loc=1)
    plt.xlabel("t (us)")
    plt.ylabel("bitrate (bps)")
    plt.grid()
    plt.savefig(figPath)

def plt_reward_track(reward, reward1, reward2, reward3, reward4, reward5, reward6, reward7,figPath):
    plt.cla()
    plt.plot(range(len(reward)), reward, alpha = 0.7, label='total_reward', color = 'red')
    plt.plot(range(len(reward1)), reward1, alpha = 0.7, label='recv_reward', color = 'blue')
    plt.plot(range(len(reward2)), reward2, alpha = 0.7, label='delay_reward', color = 'green')
    plt.plot(range(len(reward3)), reward3, alpha = 0.7, label='loss_reward', color = 'grey')
    plt.plot(range(len(reward4)), reward4, alpha = 0.7, label='frameDelay', color = 'purple')
    plt.plot(range(len(reward5)), reward5, alpha=0.7, label='active_loss', color='yellow')
    plt.plot(range(len(reward6)), reward6, alpha=0.7, label='diff_active_loss', color='pink')
    plt.plot(range(len(reward7)), reward7, alpha=0.7, label='reward_diff_bwe', color='black')
    plt.legend()
    plt.xlabel("state Num")
    plt.ylabel("reward")
    plt.grid()
    plt.savefig(figPath)

def plt_delay_throughput(pktDelayList, pktSizeList):
    1


