# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/27

"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water/
"""
"""
解:
1.暴力法 略
2.机会成本
先从头尾两侧的木板开始装水,逐渐向内寻找可增大容量的木板,此时存在2个影响因子:
    a.横坐标间隔必然缩小
    b.欲使得容量增大纵坐标必应该增加(y_new>y_old)
    c.由于纵坐标大小取决于min(y_1,y_2),所以优先考虑提高较短的y_min = min(y_1,y_2)
这里的代码写的不够优雅,有一定重复,但是效率较高.
"""


class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        y_1, y_2 = height[i], height[j]
        area = min(y_1, y_2) * (j - i)
        while i != j:
            if y_1 < y_2:
                i += 1
                if height[i] > y_1:
                    y_1 = height[i]
                    area = max(area, min(height[i], y_2) * (j - i))
            else:
                j -= 1
                if height[j] > y_2:
                    y_2 = height[j]
                    area = max(area, min(height[j], y_1) * (j - i))
        return area


if __name__ == '__main__':
    solution = Solution()
    height = [2, 3, 4, 5, 18, 17, 6]
    result = solution.maxArea(height)
    print(result)
