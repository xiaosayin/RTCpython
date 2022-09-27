#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
from torch import nn
from torch.distributions import MultivariateNormal
import numpy as np


class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim, exploration_param=0.05, device="cpu"):
        super(ActorCritic, self).__init__()
        # output of actor in [0, 1]
        self.actor_linear1 =  nn.Sequential(
                nn.Linear(state_dim, 64),
                nn.LeakyReLU(),
                nn.Linear(64, 64),
                nn.LeakyReLU()
                )
        self.actor_rnn = nn.GRU(64, 64, 2)
        self.actor_linear2 = nn.Sequential(
                            nn.Linear(64, 64),
                            nn.LeakyReLU(),
                            nn.Linear(64, action_dim),
                            nn.Sigmoid()
        )

        # critic
        self.critic_linear1 = nn.Sequential(
                nn.Linear(state_dim, 64),
                nn.LeakyReLU(),
                nn.Linear(64, 64),
                nn.LeakyReLU()
                )
        self.critic_rnn = nn.GRU(64, 64, 2)
        self.critic_linear2 = nn.Sequential(
                            nn.Linear(64, 64),
                            nn.LeakyReLU(),
                            # nn.Linear(64, action_dim)
                            nn.Linear(64, 1)
        )
        self.ha0 = None
        self.hc0 = None
        self.device = device
        self.action_var = torch.full((action_dim,), exploration_param**2).to(self.device)
        print("self.action_var shape: ", self.action_var.shape)
        self.random_action = True

    def reset(self):
        self.ha0 = None
        self.hc0 = None

    def critic(self, state, h, firstAction):
        c1 = self.critic_linear1(state)
        c2 = c1.unsqueeze(0)
        if firstAction:
            c3, hc = self.critic_rnn(c2)
        else:
            c3, hc = self.critic_rnn(c2, h)
        value = self.critic_linear2(c3)
        return value, hc

    def actor(self, state, h, firstAction):
        a1 = self.actor_linear1(state)
        #print("forward_a1: ", a1)
        a2 = a1.unsqueeze(0)
        #print("forward_a2: ", a2)
        #print("a2-shape: ", a2.shape)
        if firstAction:
            #print("first actor!: ")
            a3, ha = self.actor_rnn(a2)
            #print("forward_a3: ", a3)
        else:
            #print("not first actor!: ", [h, h.shape])
            a3, ha = self.actor_rnn(a2, h)
            #print("forward_a3: ", a3)
        action_mean = self.actor_linear2(a3)
        #print("forward_action_mean: ", action_mean)
        #print("critic ha output: ", [ha, ha.shape])
        return action_mean, ha

    def forward(self, state, firstAction):
        value, self.hc0 = self.critic(state, self.hc0, firstAction)
        action_mean, self.ha0 = self.actor(state, self.ha0, firstAction)
        #print("forward: action_mean shape, ", action_mean.shape)
        cov_mat = torch.diag(self.action_var).to(self.device)
        print("forward_action_var: ")#, self.action_var)
        #print("forward: cov_mat shape: ", cov_mat.shape)

        dist = MultivariateNormal(action_mean, cov_mat)
        #print(dist)

        if not self.random_action:
            action = action_mean
        else:
            action = dist.sample()

        action_logprobs = dist.log_prob(action)

        return action.detach(), action_logprobs, value

    def evaluate(self, state, action, firstAction):
        action_means = []
        FirstActionIndex = []
        i = 0
        while i < len(firstAction):
            if firstAction[i]:
                FirstActionIndex.append(i)
            i += 1
        FirstActionIndex.append(len(firstAction))
        i = 0
        while i < len(FirstActionIndex) - 1:
            tmpState = state[FirstActionIndex[i] : FirstActionIndex[i + 1]]
            #print("tmpState: ", tmpState)
            a1 = self.actor_linear1(tmpState)
            #print("evaluate_a1: ", a1)
            a2 = a1.unsqueeze(1)
            #print("evaluate_a2: ", a2)
            #print("a2-shape: ", a2.shape)
            a3, ha = self.actor_rnn(a2)
            #print("evaluate_a3: ", a3)
            tmpaction_mean = self.actor_linear2(a3)
            #print("evaluate_action_mean: ", tmpaction_mean)
            action_means.append(tmpaction_mean)
            i += 1



        action_mean = action_means[0]
        for i in action_means[1:]:
            action_mean = torch.cat((action_mean, i), 0)
        print("evaluate_action_mean_shape:", action_mean.shape)
        print("evaluate_action_var: ", self.action_var)
        cov_mat = torch.diag(self.action_var).to(self.device)
        dist = MultivariateNormal(action_mean, cov_mat)
        action_logprobs = dist.log_prob(action)
        dist_entropy = dist.entropy()


        #print(state)
        print("state.shape ", state.shape)
        values = []
        i = 0
        while i < len(FirstActionIndex) - 1:
            tmpState = state[FirstActionIndex[i] : FirstActionIndex[i + 1]]
            c1 = self.critic_linear1(tmpState)
            c2 = c1.unsqueeze(1)
            c3, hc = self.critic_rnn(c2)
            values.append(self.critic_linear2(c3))
            i += 1
        #print(values)

        value = values[0]
        for i in values[1:]:
            value = torch.cat((value, i), 0)

        return action_logprobs, torch.squeeze(value), dist_entropy

    def updateExploreVal(self, action_dim, exploration_param):
        self.action_var = torch.full((action_dim,), exploration_param**2).to(self.device)