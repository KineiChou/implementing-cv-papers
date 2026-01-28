import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    """
    LeNet-5 architecture implementation.
    Reference: http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf
    """
    def __init__(self, num_classes=10):
        super(LeNet, self).__init__()
        # TODO: Implement layers
        # C1: Convolutional Layer
        # S2: Subsampling Layer
        # C3: Convolutional Layer
        # S4: Subsampling Layer
        # C5: Convolutional Layer
        # F6: Fully Connected Layer
        # Output Layer
        pass

    def forward(self, x):
        # TODO: Implement forward pass
        return x
