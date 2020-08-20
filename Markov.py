"""
在n维空间中有⼀个n维的正⽅体，有⼀只蚂蚁要从⼀个顶点爬到和这个顶点相对的顶点（要⾛n
步），在每⼀个顶点处，蚂蚁选择与这个顶点相连接的任意⼀条棱的概率都是1/n，求蚂蚁爬到相
对顶点需要的步数的期望。(Hint:⻢尔可夫链)
"""

import numpy as np
from itertools import product
"""
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
"""
def solution_3():
    matrix = np.array([
        [0, 1/3, 0,   0],
        [1, 0,   2/3, 0],
        [0, 2/3, 0,   0],
        [0, 0,   1/3, 1],
    ])
    x = np.array([[1],[0],[0],[0]])
    # print(matrix)
    for i in range(1, 20):
        x = matrix.dot(x)
        print(x.tolist())
        print('P(x=' + str(i) + '): ' + str(x[3][0]))

# solution_3()


def solution_n(n):
    matrix = np.zeros((n,n))
    # for i,j in product(range(n),range(n)):
    #     matrix[i] = [1,2,3]
    for i in range(n):
        matrix[i] = [0 if j == 1 else 0 for j in range(n) ]
    print(matrix[1,2])
solution_n(3)
