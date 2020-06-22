#!/usr/bin/env python3

import gym
import numpy as np
from termcolor import colored

env = gym.make('gym_grasper:Grasper-v0')

N_EPISODES = 100
N_STEPS = 100

env.print_info()

for episode in range(1, N_EPISODES+1):
    obs = env.reset()
    for step in range(N_STEPS):
        print('#################################################################')
        print(colored('EPISODE {} STEP {}'.format(episode, step+1), color='white', attrs=['bold']))
        print('#################################################################')
        action = env.action_space.sample()
        # action = [100,100]
        observation, reward, done, _ = env.step(action)

env.close()

print('Finished.')