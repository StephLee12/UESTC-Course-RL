import gym
import math
import random

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 输入为state 输出为state的value
class Net(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        # 两个全连层
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x