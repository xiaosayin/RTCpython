#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
import numpy as np
import time
from torch import nn
from CLCC.RL.actor_critic import ActorCritic
from printLog import printLog
import info
import math
class PPO:
    def __init__(self, state_dim, state_length, action_dim, exploration_param, lr, lrMax, lrMin, max_num_episodes, betas, gamma, ppo_epoch, ppo_clip, use_gae=False):
        self.lr = lr
        self.max_num_episodes = max_num_episodes
        self.lrMax = lrMax
        self.lrMin = lrMin
        self.betas = betas
        self.gamma = gamma
        self.ppo_clip = ppo_clip
        self.ppo_epoch = ppo_epoch
        self.use_gae = use_gae
        self.updateNum = 0
        self.device = torch.device("cuda")
        self.policy = ActorCritic(state_dim, action_dim, exploration_param, self.device).to(self.device)
        self.optimizer = torch.optim.Adam(self.policy.parameters(), lr=lr, betas=betas)

        self.policy_old = ActorCritic(state_dim,  action_dim, exploration_param, self.device).to(self.device)
        self.policy_old.load_state_dict(self.policy.state_dict())

    def select_action(self, state, storage, firstAction):
        printLog(f"Before FloatTensor_reshap at ", info.logSwitch, None)
        state = torch.cuda.FloatTensor(state.reshape(1, -1))
        printLog(f"FloatTensor_reshaped at ", info.logSwitch, None)
        action, action_logprobs, value= self.policy_old.forward(state, firstAction)
        printLog(f"policy_old.forwarded at ", info.logSwitch, None)
        storage.logprobs.append(action_logprobs)
        storage.values.append(value)
        storage.states.append(state)
        storage.actions.append(action)
        storage.firstAction.append(firstAction)
        return action

    def get_value(self, state):
        print("get_value")
        state = torch.cuda.FloatTensor(state.reshape(1, -1))
        action, action_logprobs, value = self.policy_old.forward(state, False)
        return value

    def update(self, storage, state, actionDim, episode):
        episode_policy_loss = 0
        episode_value_loss = 0
        if self.use_gae:
            raise NotImplementedError
        advantages = (torch.tensor(storage.returns) - torch.tensor(storage.values)).to(self.device).detach()
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-5)
        print("advantages: ", advantages)
        old_states = torch.squeeze(torch.stack(storage.states).to(self.device), 1).detach()
        old_actions = torch.squeeze(torch.stack(storage.actions).to(self.device), 1).detach()
        old_action_logprobs = torch.squeeze(torch.stack(storage.logprobs), 1).to(self.device).detach()
        old_returns = torch.squeeze(torch.stack(storage.returns), 1).to(self.device).detach()

        for t in range(self.ppo_epoch):
            print("t1:", round(time.time() * 1000))
            logprobs, state_values, dist_entropy = self.policy.evaluate(old_states, old_actions, storage.firstAction)
            print("t2:", round(time.time() * 1000))
            print("logprobs.shape: ", logprobs.shape)
            print("old_action_logprobs.shape: ", old_action_logprobs.shape)
            ratios = torch.exp(logprobs - old_action_logprobs)
            ratios = torch.squeeze(ratios)
            print("ratios:", ratios)
            print("ratios.shape: ", ratios.shape)
            print("advantages.shape: ", advantages.shape)
            print("t3:", round(time.time() * 1000))
            surr1 = ratios * advantages
            print("t4:", round(time.time() * 1000))
            surr2 = torch.clamp(ratios, 1-self.ppo_clip, 1+self.ppo_clip) * advantages
            print("surr1, surr2:", surr1, surr2)
            print("t5:", round(time.time() * 1000))
            policy_loss = -torch.min(surr1, surr2).mean()
            print("t6:", round(time.time() * 1000))
            print("state_values:", state_values)
            print("state_values.shape: ", state_values.shape)
            print("old_returns.shape: ", old_returns.shape)
            value_loss = 0.5 * (state_values - old_returns).pow(2).mean()
            print("t7:", round(time.time() * 1000))
            loss = policy_loss + value_loss
            print("t8:", round(time.time() * 1000))
            self.optimizer.zero_grad()
            print("t9:", round(time.time() * 1000))

            loss.backward()
            print("t10:", round(time.time() * 1000))

            self.optimizer.step()
            print("t11:", round(time.time() * 1000))
            episode_policy_loss += policy_loss.detach()
            print("t12:", round(time.time() * 1000))
            episode_value_loss += value_loss.detach()
        self.policy_old.load_state_dict(self.policy.state_dict())
        self.updateNum += 1
        for p in self.optimizer.param_groups:
            print("OPTIMIZER LR:", p["lr"])

        #update network hyper param
        self.adjust_learning_rate(episode)


        return episode_policy_loss / self.ppo_epoch, episode_value_loss / self.ppo_epoch

    def adjust_learning_rate(self, episode):
        a = self.lrMax
        b = self.lrMin
        e = self.max_num_episodes
        d = [50, 60, 70]
        episodesList = []
        for i in range(len(d)):
            if i == 0:
                episodesList.append(d[i])
            else:
                episodesList.append(d[i] + episodesList[i - 1])
        #self.optimizer.param_groups[0]['lr'] = (a - b) / 2 * math.cos(1 / e * math.pi  * episode) + (a + b) / 2
        if episode in episodesList:

            self.optimizer.param_groups[0]['lr'] = self.optimizer.param_groups[0]['lr'] * 0.1

    def save_model(self, data_path):
        checkpoint = {
            'model': self.policy.state_dict(),
            'optimizer': self.optimizer.state_dict(),
        }
        #torch.save(self.policy.state_dict(), '{}ppo_{}.pth'.format(data_path, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))
        torch.save(checkpoint, '{}ppo_{}'.format(data_path, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())))

    def save_docker_model(self, data_path):
        checkpoint = {
            'model': self.policy.state_dict(),
            'optimizer': self.optimizer.state_dict(),
        }
        #torch.save(self.policy.state_dict(), '{}docker_pth.pth'.format(data_path))
        torch.save(checkpoint, '{}docker_pth'.format(data_path))

