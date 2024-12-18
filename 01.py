import torch
import torch.nn as nn
import torch.functional as F


class Model(nn.Module):
    def __init__(self, in_features=4, h1=8, h2=9, output_features=3):

        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, output_features)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x
    
model = Model()


