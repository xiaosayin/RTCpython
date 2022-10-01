#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import sizeof
from pdb import Restart
import sys
import os
import subprocess
import traceback
import json
import time
import multiprocessing as mp
from multiprocessing import Array
import importlib

from numpy import true_divide
from rtc_env import GymEnv
from CLCC.RL.storage import Storage
from CLCC.RL.ppo_agent import PPO
import torch
import matplotlib.pyplot as plt
import bitRateAnalysis2
from runInRemote import catStorage, runInRemote
import pickle
from printLog import printLog
import plotResult
import random
import math
sys.path.append(os.getcwd())
os.system("rm result/*")
os.system("rm result/tmp/*")
# os.system("rm result/delay/*")
TEST_MODE = False     #whether run for a test or training
TEST_PTH = './data/ppo_2022_09_29_18_02_53'    #if run for a test, the tested pth
# TEST_PTH = './historical_data/ppo_2022_09_15_18_20_36'
ACTION_PATH = "/home/yinwenpei/rtc_signal/action_fifo"

# periodic random
TEST_traceType = 'random'   #test environment
TEST_traceNum = 92
TEST_Que = 168
TEST_Loss = 3   #%
TEST_VIDEO = 1    #[Johnny, KristenAndSara, vidyo1, vidyo3, FourPeople]
if TEST_MODE:
    multiPC = False
    reStart = False
else:
    multiPC = True
    reStart = True



def main():

    ############## Hyperparameters for the experiments ##############
    env_name = "AlphaRTC"
    range1 = 50
    range2 = 60
    range3 = 70
    exp1 = 0.25
    exp2 = 0.15
    exp3 = 0.1
    exp4 = 0.01
    max_num_episodes = range1 + range2 + range3    # maximal episodes
    if TEST_MODE:
        max_num_episodes = 1   #single test

    sample_Maxnum = 300
    if TEST_MODE:
        sample_Maxnum = 1
    save_interval = 2          # save model every save_interval episode
    exploration_param = 0.7    # the std var of action distribution
    K_epochs = 15              # update policy for K_epochs
    ppo_clip = 0.1             # clip parameter of PPO
    gamma = 0.8                # discount factor

    lrMax = 3e-3                 # Adam parameters
    lrMin = 3e-5

    betas = (0.9, 0.999)
    state_dim = 8
    state_length = 4
    action_dim = 2
    data_path = f'./data/' # Save model and reward curve here
    localPath = f'/home/yinwenpei/RTCPython/localFiles/'
    #############################################
    
    #'tony', 'koyong', 'racheal', 'yuanjinghao'
    remotePath, remoteip, remoteid, remotePSword = setRemotePCs(['yinwenpei']) #set which PCs to remote distribute

    if not os.path.exists(data_path):
        os.makedirs(data_path)
    mp.set_start_method('fork')
    env = GymEnv(200)
    storage = Storage() # used for storing data
    ppo = PPO(state_dim, state_length, action_dim, exploration_param, lrMax, lrMax, lrMin, max_num_episodes, betas, gamma, K_epochs, ppo_clip)
    print("before ha0: ", ppo.policy.ha0)
    os.system("rm localFiles/*")
    if reStart:
        os.system("rm data/*")
        os.system("rm data/log/*")
        os.system("rm data/ratepdf/*")
        os.system("rm data/ratecdf/*")
    else:
        checkpoint = torch.load(TEST_PTH)
        ppo.policy.load_state_dict(checkpoint['model'])
        ppo.policy_old.load_state_dict(checkpoint['model'])
        ppo.optimizer.load_state_dict(checkpoint['optimizer'])
        #ppo.policy.load_state_dict(torch.load('./backupData/02_02_1.3*delay_2000/ppo_2022_02_02_13_04_00.pth'))
        #ppo.policy_old.load_state_dict(torch.load('./backupData/02_02_1.3*delay_2000/ppo_2022_02_02_13_04_00.pth'))
    ppo.save_docker_model(localPath)

    print("after ha0: ", ppo.policy.ha0)
    record_episode_reward = []
    record_episode_rewardRecv = [] #recv_rate
    record_episode_rewardDelay = [] #delay
    record_episode_rewardLoss = [] #loss
    record_episode_rewardFrameDelay = [] #frameDelay
    record_episode_reward_active_loss = []
    record_episode_diff_active_loss = []

    rewardList = []
    rRateList = []

    episode_reward  = 0
    time_step = 0

    stateRecvRate = []
    statePacketDelay = []
    statePacketDelayGradient =[]
    statePacketLoss = []
    statePsnr = []
    stateFrameDelay = []
    stateFrameDelayGradient = []
    stateFrameSkip = []
    stateWidth = []
    stateBWE = []
    stateReward = []
    stateRewardRecv = []
    stateRewardDelay = []
    stateRewardLoss = []
    stateRewardFrameDelay = []
    # training loop
    # training loop
    for episode in range(max_num_episodes):

        if episode <= range1:
            this_exploration_param = ( exp1 - (exp1 - exp2)/range1 * episode)
        if episode > range1 and episode <= range1 + range2:
            this_exploration_param = ( exp2 - (exp2 - exp3)/range2 * (episode - range1))
        if episode > range1 + range2:
            this_exploration_param = ( exp3 - (exp3 - exp4)/range3 * (episode - range1 - range2))
        #if episode > range1 + range2 + range3:
        #    this_exploration_param = ( exp4 - (exp4 - exp5)/range4 * (episode - range1 - range2 - range3))
        if TEST_MODE:
            this_exploration_param = 0.01
        if multiPC:
            p1 = mp.Process(target=runInRemote, args=(localPath, remotePath, remoteip, remoteid, \
                            remotePSword, this_exploration_param))
            p1.start()
        ppo.policy_old.updateExploreVal(action_dim, this_exploration_param)
        ppo.policy.updateExploreVal(action_dim, this_exploration_param)
        episode_reward = 0
        episode_rewardRecv = 0
        episode_rewardDelay = 0
        episode_rewardLoss = 0
        episode_rewardFrameDelay = 0
        episode_reward_active_loss = 0
        episode_diff_active_loss = 0
        time_step = 0
        sample_cnt = 0
        rewardList = []
        rRateList = []

        os.system(f"rm -rf {localPath}storage*")
        print("clear historic storagefiles from remote!")

        while True:
            done = False
            #state = torch.zeros((1, state_dim, state_length)).cuda()
            #state = [0, 0, 0, 0, 0, 0, 0]
            state = [0] * state_dim    #R3NET
            stateRecvRate = []
            statePacketDelay = []
            statePacketDelayGradient = []
            statePacketLoss = []
            statePacketBurstLoss = []
            statePsnr = []
            stateFrameDelay = []
            stateFrameDelayGradient = []
            stateWidth = []
            stateFrameSkip = []
            stateBWE = []
            stateEncRate = []
            stateRewardRecv = []
            stateRewardDelay = []
            stateRewardLoss = []
            stateRewardFrameDelay = []
            stateReward = []
            stateReward_active_loss = []
            state_diff_active_loss = []

            state = torch.Tensor(state).cuda()

            traceRandom = random.randint(0, 999)
            if traceRandom < 500:
                traceType = 'random'
            else:
                traceType = 'periodic'
            traceNum = traceRandom % 500
            queLength = random.randint(6, 349)
            lossRate = float(random.randint(0, 500)) / 100
            video = random.randint(0, 4)    #[Johnny, KristenAndSara, vidyo1, vidyo3, FourPeople]

            if TEST_MODE:
                traceType = TEST_traceType
                traceNum = TEST_traceNum
                queLength = TEST_Que
                lossRate = TEST_Loss
                video = TEST_VIDEO

            # time.sleep(5)
            env.reset(traceType, traceNum, queLength, lossRate, video)
            ppo.policy_old.reset()
            ppo.policy.reset()

            firstAction = True  #to record whether RNN needs a h0
            time_step = 0
            while not done:# and time_step < update_interval:
                action = ppo.select_action(state, storage, firstAction)
                print(f"give action {sample_cnt}====={action}=======================")
                listState, reward, reward_recv, reward_delay, reward_loss, reward_frameDelay, done, recv_rate, \
                reward_active_loss, diff_active_loss,_ = env.step(action,firstAction)
                firstAction = False
                #[0: receiving_rate, 1: delay, 2: delay_gradient, 3: loss_ratio, 4: burst_loss, \
                # 5: psnr, 6: frameDelay, 7: frameDelayGradient, 8: frameSkip, 9: width, 10: lasetBWE, 11: encLoss]
                rewardList.append(reward)
                rRateList.append(recv_rate)
                time_step += 1
                sample_cnt += 1
                print("listState: ")#, listState)
                state = state.clone().detach()
              

                
                ## with PSNR
                state[0] = listState[1]     #delay
                state[1] = listState[2]     #delayGradient
                state[2] = listState[4]     #burstLoss
                state[3] = listState[5]     #PSNR
                #state[3] = listState[12]    # gcc bwe
                state[4] = listState[6]     #frameDelay
                state[5] = listState[7]     #frameDelayGradient
                state[6] = listState[9]     #width
                state[7] = listState[10]     #last frame loss Action
                print("terminal state:", state)
                '''encodeRates
                ## withOUT PSNR
                state[0] = listState[1]     #delay
                state[1] = listState[2]     #delayGradient
                state[2] = listState[4]     #burstLoss
                state[3] = listState[6]     #frameDelay
                state[4] = listState[7]     #frameDelayGradient
                state[5] = listState[10]     #lastAction
                '''

                '''
                ## Only pkt
                state[0] = listState[1]     #delay
                state[1] = listState[2]     #delayGradient
                state[2] = listState[4]     #burstLoss
                state[3] = listState[10]     #lastAction
                
                '''

                stateRecvRate.append(listState[0])
                statePacketDelay.append(listState[1])
                statePacketDelayGradient.append(listState[2])
                statePacketLoss.append(listState[3])
                statePacketBurstLoss.append(listState[4])
                statePsnr.append(listState[5])
                stateFrameDelay.append(listState[6])
                stateFrameDelayGradient.append(listState[7])
                stateFrameSkip.append(listState[8])
                stateWidth.append(listState[9])
                stateBWE.append(listState[10])
                stateEncRate.append(listState[11])
                stateReward.append(reward)
                stateRewardRecv.append(reward_recv)
                stateRewardDelay.append(reward_delay)
                stateRewardLoss.append(reward_loss)
                stateRewardFrameDelay.append(reward_frameDelay)
                stateReward_active_loss.append(reward_active_loss)
                state_diff_active_loss.append(diff_active_loss)
                if (listState[3] < 0 or listState[3] > 1):
                    print("stateLoss: ", listState[3])
                    return
                # Collect data for update
                if not done:
                    storage.rewards.append(reward)
                    storage.rewardRecv.append(reward_recv)
                    storage.rewardDelay.append(reward_delay)
                    storage.rewardLoss.append(reward_loss)
                    storage.rewardFrameDelay.append(reward_frameDelay)
                    storage.reward_active_loss.append(reward_active_loss)
                    storage.diff_active_loss.append(diff_active_loss)
                    storage.is_terminals.append(done)
                    episode_reward += reward
                    episode_rewardRecv += reward_recv
                    episode_rewardDelay += reward_delay
                    episode_rewardLoss += reward_loss
                    episode_rewardFrameDelay += reward_frameDelay
                    episode_reward_active_loss += reward_active_loss
                    episode_diff_active_loss += diff_active_loss
                    
                else:
                    sample_cnt -= 1
                    env.recv_ratef.close()
                    if time_step != 1:
                        storage.actions.pop()
                        storage.values.pop()
                        storage.states.pop()
                        storage.logprobs.pop()
                        storage.firstAction.pop()
                        storage.is_terminals[-1] = True

                    else:
                        storage.logprobs.pop()
                        storage.values.pop()
                        storage.states.pop()
                        storage.actions.pop()
                        storage.firstAction.pop()
                    print(f"one rtc ended. {time_step} actions in this RTC. ============================\n")
                    time_step = 0
                print("reward:")#, reward)
                print("state")#, state)
                print("one action ended============================\n")

            if done and sample_cnt > sample_Maxnum:
                curTime = time.strftime("%d_%H_%M_%S", time.localtime())
                if queLength < 10:
                    logQ = f"00{queLength}"
                elif queLength >= 10 and queLength < 100:
                    logQ = f"0{queLength}"
                else:
                    logQ = f"{queLength}"
                logL = math.floor(lossRate)


                print("lenof storage before cat: ", len(storage.actions))
                if multiPC:
                    p1.join()
                    storage = catStorage(localPath, storage)

                print("abs(sum(storage.rewardDelay): ", abs(sum(storage.rewardDelay)))
                print("len(sum(storage.rewardDelay):", len(storage.rewardDelay))
                if (abs(sum(storage.rewardDelay) / len(storage.rewardDelay)) > 100):
                    print("abs(sum(storage.rewardDelay) / len(storage.rewardDelay)) > 100")
                    env.run_terminal()
                    time.sleep(1)
                    episode -= 1
                    print("env.run_terminal()!")
                    storage.clear_storage()
                    break

                print("lenof storage after cat: ", len(storage.rewards))
                next_value = ppo.get_value(state)
                next_value.detach()
                storage.compute_returns(next_value, gamma)

                print("rewards: ", storage.returns)
                # update
                if not TEST_MODE:
                    policy_loss, val_loss = ppo.update(storage, state, action_dim, episode)
                else:
                    policy_loss, val_loss = 0, 0
                currTime = ""
                drawPlt('stateNum', 'stateRecvRate', f'{data_path}state0RecvRate_{currTime}.jpg', stateRecvRate)
                drawPlt('stateNum', 'statePacketDelay', f'{data_path}state1PacketDelay_{currTime}.jpg', statePacketDelay)
                drawPlt('stateNum', 'statePacketDelayGradient', f'{data_path}state2PacketDelayGradient_{currTime}.jpg', statePacketDelayGradient)
                drawPlt('stateNum', 'statePacketLoss', f'{data_path}state3PacketLoss_{currTime}.jpg', statePacketLoss)
                drawPlt('stateNum', 'statePacketBurstLoss', f'{data_path}state4PacketBurstLoss_{currTime}.jpg', statePacketBurstLoss)

                drawPlt('stateNum', 'statePsnr', f'{data_path}state5Psnr_{currTime}.jpg', statePsnr)
                drawPlt('stateNum', 'stateFrameDelay', f'{data_path}state6FrameDelay_{currTime}.jpg', stateFrameDelay)
                drawPlt('stateNum', 'stateFrameDelayGradient', f'{data_path}state7FrameDelayGradient_{currTime}.jpg', stateFrameDelayGradient)
                drawPlt('stateNum', 'stateFrameSkip', f'{data_path}state8FrameSkip_{currTime}.jpg', stateFrameSkip)
                drawPlt('stateNum', 'stateWidth', f'{data_path}state9Width_{currTime}.jpg', stateWidth)
                drawPlt('stateNum', 'stateBWE', f'{data_path}state10BWE_{currTime}.jpg', stateBWE)
                drawPlt('stateNum', 'stateEncRate', f'{data_path}state11EncRate_{currTime}.jpg', stateEncRate)
                plotResult.plt_reward_track(stateReward, stateRewardRecv, stateRewardDelay, stateRewardLoss, stateRewardFrameDelay, \
                stateReward_active_loss, state_diff_active_loss, f'{data_path}reward{episode}_q:{logQ}_L:{logL}_{curTime}_v_{video}_{traceType[0]}:{traceNum}.jpg')


                #plot reward line
                episode_reward /= sample_cnt
                episode_rewardRecv /= sample_cnt
                episode_rewardDelay /= sample_cnt
                episode_rewardLoss /= sample_cnt
                episode_rewardFrameDelay /= sample_cnt
                episode_reward_active_loss /= sample_cnt
                episode_diff_active_loss /= sample_cnt
                record_episode_reward.append(sum(storage.rewards) / len(storage.rewards))
                record_episode_rewardRecv.append(sum(storage.rewardRecv) / len(storage.rewardRecv))
                record_episode_rewardDelay.append(sum(storage.rewardDelay) / len(storage.rewardDelay))
                record_episode_rewardLoss.append(sum(storage.rewardLoss) / len(storage.rewardLoss))
                record_episode_rewardFrameDelay.append(sum(storage.rewardFrameDelay) / len(storage.rewardFrameDelay))
                record_episode_reward_active_loss.append(sum(storage.reward_active_loss) / len(storage.reward_active_loss))
                record_episode_diff_active_loss.append(sum(storage.diff_active_loss)/ len(storage.diff_active_loss))


                
                print('Episode {} \t Average policy loss, value loss, reward {}, {}, {}'.format(episode, policy_loss, val_loss, episode_reward))

                #drawPlt('Episode', 'Averaged episode reward', '%sreward_record.jpg' % (data_path), record_episode_reward)

                plotResult.plt_reward_record(record_episode_reward, record_episode_rewardRecv, \
                    record_episode_rewardDelay, record_episode_rewardLoss, record_episode_rewardFrameDelay,record_episode_reward_active_loss,\
                    record_episode_diff_active_loss, '%sreward_record.jpg' % (data_path))

                plotResult.plt_reward_rate(rewardList, rRateList, '%ssingleReward.jpg' % (data_path))

                intrRateList = []
                i = 0
                while i < len(rRateList):
                    intrRateList.append(int(rRateList[i] / 1000))
                    print("intrRateList", intrRateList[-1])
                    i += 1
                #plotResult.plt_rate_pdf(intrRateList, '{}ratepdf/rate_pdf_{}.jpg'.format(data_path, curTime))

                #plotResult.plt_rate_cdf(intrRateList, '{}ratecdf/rate_cdf_{}.jpg'.format(data_path, curTime))

                if episode >= 0 and not (episode % save_interval):
                    ppo.save_model(data_path)
                ppo.save_docker_model(localPath)
                try:
                    plotTargetT, plotTarget, plotEncT, plotEnc, plotSetT, plotSet, \
                        plotRecvT, plotRecv, mahiT, mahiRate = bitRateAnalysis2.getPLTlist(traceType, traceNum)
                    plotResult.plt_track(plotTargetT, plotTarget, plotEncT, plotEnc, \
                        plotSetT, plotSet, plotRecvT, plotRecv, mahiT, mahiRate,  f'{data_path}track{episode}_q:{logQ}_L:{logL}_{curTime}_v_{video}_{traceType[0]}:{traceNum}.jpg')
                except:
                    print("Plot track encode rates fail!")
                print("one RTC finished. ")
                RTCrate, RTCdelay, RTCloss = env.getThisRTCTotalStat()
                print(f"In this RTC, recv_rate = {RTCrate}, delay = {RTCdelay}, loss = {RTCloss}")
                env.run_terminal()
                time.sleep(1)
                print("env.run_terminal()!")

                print("ready to clear storage!")
                storage.clear_storage()
                print("ready to break!")
                break

def drawPlt(x, y, pltName, listPlt):
    plt.cla()
    plt.plot(range(len(listPlt)), listPlt)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.savefig(pltName)

def setRemotePCs(names):
    # allPath = [f'/home/tony/KoyongRTC/AlphaRTCNoDocker/',f'/home/koyong/AlphaRTCNoDocker/',\
    #              f'/home/racheal/KoyongRTC/AlphaRTCNoDocker/', f'/home/yuanjinghao/KoyongRTC/AlphaRTCNoDocker/']
    allPath = [f'/home/tony/KoyongRTC/AlphaRTCNoDocker/',f'/home/yinwenpei/RTCPython/', \
               f'/home/racheal/KoyongRTC/AlphaRTCNoDocker/', f'/home/yuanjinghao/KoyongRTC/AlphaRTCNoDocker/']
    allip = ['172.16.6.117', '172.16.6.104',\
                '172.16.6.164', '172.16.6.165']
    allid = ['tony', 'yinwenpei',\
                'racheal', 'yuanjinghao']
    allPSword = ['555888','medialab2022',\
                    '010203', '9375']
    remotePath = []
    remoteip = []
    remoteid = []
    remotePSWord = []
    for id in names:
        index = allid.index(id)
        remotePath.append(allPath[index])
        remoteip.append(allip[index])
        remoteid.append(allid[index])
        remotePSWord.append(allPSword[index])
    return remotePath, remoteip, remoteid, remotePSWord




if __name__ == "__main__":
    main()
