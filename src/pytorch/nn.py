import torch
import numpy as np
# 导入torch内置数据集
from torchvision.datasets import mnist
# 导入预处理模块
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
# 导入nn以及优化器
import torch.nn.functional as F
import torch.optim as optim
from torch import nn
import matplotlib.pyplot as plt

# 定义超参数
train_batch_size = 64
test_batch_size = 128
learn_rate = 0.01
num_epoches = 20
lr = 0.01
momentum = 0.5

# 下载数据并对数据做预处理
# 定义预处理函数，这些预处理依次放在Compose函数中
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5], [0.5])])
train_dataset = mnist.MNIST('./data', train=True, transform=transform, download=True)
test_dataset = mnist.MNIST('./data', train=False, transform=transform)
# dataloader 是一个可迭代对象，可以像使用迭代器一样使用
train_loader = DataLoader(train_dataset, batch_size=train_batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=test_batch_size, shuffle=False)

examples = enumerate(test_dataset)
batch_idx, (example_data, example_targets) = next(examples)

fig = plt.figure()
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.tight_layout()
    plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
    plt.title("Ground Truth: {}".format(example_targets[i]))
    plt.xticks([])
    plt.yticks([])




