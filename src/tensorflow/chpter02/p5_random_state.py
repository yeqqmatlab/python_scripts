import numpy as np

'''
在该状态下生成的随机序列（正态分布）一定会有相同的模式。
但是，不同的随机种子状态将会有不同的数据生成模式。
这一特点在随机数据生成的统计格式控制显得很重要。
'''

rdm = np.random.RandomState(seed=1)

a = rdm.rand()

b = rdm.rand(2, 3)

print(a)
print(b)