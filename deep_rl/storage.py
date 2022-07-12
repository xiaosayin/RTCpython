#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import torch
import pickle

class Storage:
    def __init__(self):
        self.actions = []
        self.values = []
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.rewardRecv = []
        self.rewardDelay = []
        self.rewardLoss = []
        self.rewardFrameDelay = []
        self.is_terminals = []
        self.returns = []
        self.firstAction = []

    def __eq__(self, other):
        index = 0
        for i in self.actions:
            if i != other.actions[index]:
                return False
            index += 1

        index = 0
        for i in self.values:
            if i != other.values[index]:
                return False
            index += 1

        index = 0
        indexj = 0
        for i in self.states:
            indexj = 0
            for j in i[0]:
                if j != other.states[index][0][indexj]:
                    return False
                indexj += 1
            index += 1

        index = 0
        for i in self.logprobs:
            if i != other.logprobs[index]:
                return False
            index += 1

        index = 0
        for i in self.rewards:
            if i != other.rewards[index]:
                return False
            index += 1

        index = 0
        for i in self.is_terminals:
            if i != other.is_terminals[index]:
                return False
            index += 1

        index = 0
        for i in self.returns:
            if i != other.returns[index]:
                return False
            index += 1
        return True



    def compute_returns(self, next_value, gamma):
        # compute returns for advantages
        returns = np.zeros(len(self.rewards)+1)
        returns[-1] = next_value
        for i in reversed(range(len(self.rewards))):
            returns[i] = returns[i+1] * gamma * (1-self.is_terminals[i]) + self.rewards[i]
            self.returns.append(torch.tensor([returns[i]]))
        print("returns: ", returns)
        self.returns.reverse()

    def save_Storage(self, path):
        savef = open("storage.txt", 'w')
        for i in self.actions:
            savef.write(f"{i}\n")
        for i in self.values:
            savef.write(f"{i}\n")
        for i in self.states:
            savef.write(f"{i}\n")
        for i in self.logprobs:
            savef.write(f"{i}\n")
        for i in self.rewards:
            savef.write(f"{i}\n")
        for i in self.is_terminals:
            savef.write(f"{i}\n")
        for i in self.returns:
            savef.write(f"{i}\n")
        savef.close()
        f=open(f'{path}storagePickle','wb')
        pickle.dump(self, f, 0)
        f.close()

    def cat_Storage(self, other):
        self.actions = self.actions + other.actions
        self.values = self.values + other.values
        self.states = self.states + other.states
        self.logprobs = self.logprobs + other.logprobs
        self.rewards = self.rewards + other.rewards
        self.rewardRecv = self.rewardRecv + other.rewardRecv
        self.rewardDelay = self.rewardDelay + other.rewardDelay
        self.rewardLoss = self.rewardLoss + other.rewardLoss
        self.rewardFrameDelay = self.rewardFrameDelay + other.rewardFrameDelay
        self.is_terminals = self.is_terminals + other.is_terminals
        self.returns = self.returns + other.returns
        self.firstAction = self.firstAction + other.firstAction  

    def clear_storage(self):
        self.actions.clear()
        self.values.clear()
        self.states.clear()
        self.logprobs.clear()
        self.rewards.clear()
        self.rewardRecv.clear()
        self.rewardDelay.clear()
        self.rewardLoss.clear()
        self.rewardFrameDelay.clear()
        self.is_terminals.clear()
        self.returns.clear()
        self.firstAction.clear()
