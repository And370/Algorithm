"""
在n维空间中有⼀个n维的正⽅体，有⼀只蚂蚁要从⼀个顶点爬到和这个顶点相对的顶点（要⾛n
步），在每⼀个顶点处，蚂蚁选择与这个顶点相连接的任意⼀条棱的概率都是1/n，求蚂蚁爬到相
对顶点需要的步数的期望。(Hint:⻢尔可夫链)
"""

import numpy as np
from itertools import product
from fractions import Fraction
"""
先考虑三维空间正方形的情况

1.马尔科夫-状态转移矩阵列出,得到期望公式
    1.1 错位相减法
    1.2 程序求和逼近
    1.3 蒙特卡洛模拟
# 经过N次移动后所在位置期望
matrix = np.array([
	[0, 1/3, 0,   0],
	[1, 0,   2/3, 0],
	[0, 2/3, 0,   1],
	[0, 0,   1/3, 0]
])
# 经过N次后是否到达过终点期望
matrix = np.array([
	[0, 1/3, 0,   0],
	[1, 0,   2/3, 0],
	[0, 2/3, 0,   0],
	[0, 0,   1/3, 1],
])

# 经过N次后首次到达终点期望
matrix = np.array([
    [0, 1/3, 0,   0],
    [1, 0,   2/3, 0],
    [0, 2/3, 0,   0],
    [0, 0,   1/3, 0],
])

3	2/9 = 2/3 * 1/3	
5	14/81 = 14/27 * 1/3 = 7/9 * 2/3 * 1/3
7	98/729 = 98/243 * 1/3 = 7/9 * 14/27 * 1/3

i >= 3
P3 = 2/9
Pi = 7/9 * N(i-2) = (7/9)^((i-3)/2) * 2/9

E3 = 3 * P3
当i为奇数
Ei = [3+(i-3)/2] * Pi

Si = ∑(Ni) = sum( i * (7/9)^((i-3)/2) * 2/9 ~)
错位相减

2.这里有更优雅的算法
https://math.stackexchange.com/questions/28179/logic-question-ant-walking-a-cube

E(BD)=2/9(2)+7/9(2+E(BD))
which means
E(BD)=9
It takes one step to go from A to B, so
E(AD)=10

"""
def solution_3():
    matrix = np.array([
        [0, 1/3, 0,   0],
        [1, 0,   2/3, 0],
        [0, 2/3, 0,   0],
        [0, 0,   1/3, 0],
    ])
    x = np.array([[1],[0],[0],[0]])
    # print(matrix)
    s = 0
    for i in range(1, 200):
        x = matrix.dot(x)
        # print(x.tolist())
        print('P(x=' + str(i) + '): ' + str(x[3][0]),'\n')
        s += i * x[3][0]
        print(s)

def solution_3_():
    a = Fraction(1)
    b = Fraction(2)
    c = Fraction(3)
    matrix = np.array([
        [0, a/c, 0,   0],
        [c/c, 0,   b/c, 0],
        [0, b/c, 0,   0],
        [0, 0,   a/c, 0],
    ])
    x = np.array([[1],[0],[0],[0]])
    # print(matrix)
    for i in range(1, 20):
        x = matrix.dot(x)
        print('P(x=' + str(i) + '): ' + str(x[2][0]))
        print('P(x=' + str(i) + '): ' + str(x[3][0]),'\n')



def solution_n(n):
    matrix = np.zeros((n,n))
    # for i,j in product(range(n),range(n)):
    #     matrix[i] = [1,2,3]
    for i in range(n):
        matrix[i] = [0 if j == 1 else 0 for j in range(n) ]
    print(matrix[1,2])


solution_3()
# solution_n(3)


