import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))

x = np.array([1,-1])   #输入向量
w1 = np.array([[1,-2],[-1,1]])  #输入层和第一隐含层之间的权重矩阵
b1 = np.array([1,0])   #第一隐含层神经元的偏置向量
h1 = np.dot(x,w1)

s1 = input()
s2 = s1[::-1]
print(s2)
print(h1)