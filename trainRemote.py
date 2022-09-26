#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import sizeof
import sys
import os
import subprocess
import traceback
import json
import time
import multiprocessing as mp
from multiprocessing import Array
import importlib
import pickle

from numpy import true_divide
from rtc_env import GymEnv
from CLCC.RL.storage import Storage
from CLCC.RL.ppo_agent import PPO
import torch
import matplotlib.pyplot as plt
from printLog import printLog
import info
import random
sys.path.append(os.getcwd())
os.system("rm result/*")
os.system("rm result/tmp/*")
os.system("rm result/delay/*")


def trainRemote():
    ############## Hyperparameters for the experiments ##############
    env_name = "AlphaRTC"
    sample_Maxnum = 300
    range1 = 50
    range2 = 60
    range3 = 70
    max_num_episodes = range1 + range2 + range3
    exploration_param = 0.7    # the std var of action distribution
    K_epochs = 15               # update policy for K_epochs
    ppo_clip = 0.1            # clip parameter of PPO
    gamma = 0.8                # discount factor

    lrMax = 3e-3                 # Adam parameters
    lrMin = 3e-5
    betas = (0.9, 0.999)
    state_dim = 8
    state_length = 10
    action_dim = 1
    data_path = f'./data/' # Save model and reward curve here
    remotePath = os.getcwd() + '/remoteFiles/'
    #############################################
    printSwitch = True

    if not os.path.exists(data_path):
        os.makedirs(data_path)
    mp.set_start_method('fork')
    env = GymEnv(200)
    storage = Storage() # used for storing data
    ppo = PPO(state_dim, state_length, action_dim, exploration_param, lrMax, lrMax, lrMin, max_num_episodes, betas, gamma, K_epochs, ppo_clip)
    checkpoint = torch.load(f'{remotePath}docker_pth')
    ppo.policy.load_state_dict(checkpoint['model'])
    ppo.policy_old.load_state_dict(checkpoint['model'])
    #ppo.policy.load_state_dict(torch.load(f'{remotePath}docker_pth.pth'))
    #ppo.policy_old.load_state_dict(torch.load(f'{remotePath}docker_pth.pth'))

    expf = open(f"{remotePath}exp.txt", "r")
    expline = expf.readline()
    this_exploration_param = float(expline)
    expf.close()
    # this_exploration_param = 0.25
    ppo.policy_old.updateExploreVal(action_dim, this_exploration_param)
    ppo.policy.updateExploreVal(action_dim, this_exploration_param)

    #os.system("rm data/*")
    #os.system("rm data/log/*")


    record_episode_reward = []
    episode_reward  = 0
    time_step = 0

    # training loop

    episode_reward = 0
    time_step = 0
    sample_cnt = 0
    while True :
        done = False
        state = [0] * state_dim    #R3NET
        state = torch.Tensor(state).cuda()
        traceRandom = random.randint(0, 999)
        if traceRandom < 500:
            traceType = 'random'
        else:
            traceType = 'periodic'
        traceNum = traceRandom % 500
        queLength = random.randint(6, 349)
        lossRate = float(random.randint(0, 500)) / 100
        video = random.randint(0, 4)  # [Johnny, KristenAndSara, vidyo1, vidyo3, FourPeople]
        # traceType = 'periodic'
        # traceNum = 38
        # queLength = 168
        # lossRate = 3.0
        # video = 1


        env.reset(traceType, traceNum, queLength, lossRate, video)
        ppo.policy_old.reset()
        ppo.policy.reset()

        firstAction = True  #to record whether RNN needs a h0
        time_step = 0
        while not done:# and time_step < update_interval:
            action = ppo.select_action(state, storage, firstAction)

            print(f"give action {sample_cnt}============================")
            listState, reward, reward_recv, reward_delay, reward_loss, reward_frameDelay, done, recv_rate, \
            reward_active_loss, diff_active_loss,_ = env.step(action,firstAction)
            firstAction = False
            time_step += 1
            sample_cnt += 1
            printLog(f"before listState:  at ", info.logSwitch, None)

            print("listState: ")#, listState)
            printLog(f"before state.clone().detach() at ", info.logSwitch, None)
            state = state.clone().detach()
            printLog(f"state.clone().detach() at ", info.logSwitch, None)

            ## with PSNR
            state[0] = listState[1]     #delay
            state[1] = listState[2]     #delayGradient
            state[2] = listState[4]     #burstLoss
            state[3] = listState[5]     #PSNR
            #state[3] = listState[12]    # gcc bwe
            # print("state[3]:", state[3])
            state[4] = listState[6]     #frameDelay
            state[5] = listState[7]     #frameDelayGradient
            state[6] = listState[9]     #width
            state[7] = listState[10]     #lastAction

            ## withOUT PSNR
            # state[0] = listState[1]     #delay
            # state[1] = listState[2]     #delayGradient
            # state[2] = listState[4]     #burstLoss
            # state[3] = listState[6]     #frameDelay
            # state[4] = listState[7]     #frameDelayGradient
            # state[5] = listState[10]     #lastAction
            
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
            else:
                sample_cnt -= 1
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
                time_step = 0
            episode_reward += reward
            print("reward:", reward)
            print("state")#, state)
            print("one action ended============================\n")
        print("one rtc ended============================\n")
        RTCrate, RTCdelay, RTCloss = env.getThisRTCTotalStat()
        print(f"In this RTC, recv_rate = {RTCrate}, delay = {RTCdelay}, loss = {RTCloss}")
        if done and sample_cnt > sample_Maxnum:
            if (abs(sum(storage.rewardDelay) / len(storage.rewardDelay)) > 100):
                print("abs(sum(storage.rewardDelay) / len(storage.rewardDelay)) > 100")
                env.run_terminal()
                os.system(f"rm -rf {remotePath}storagePickle")
                time.sleep(1)
                return
            storage.save_Storage(remotePath)
            env.run_terminal()
            break
    #f1 = open(f'{remotePath}storagePickle', 'rb')
    #storageB = pickle.load(f1)
    #f1.close()
    #print("storage == storageB?: ", storage == storageB)

#draw.draw_module(ppo.policy, data_path)

def main():
    trainRemote()

if __name__ == "__main__":
    main()
