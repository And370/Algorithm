# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/7

"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        index_0 = 0
        index_2 = len(nums) - 1
        # 注意此处的index_0和index_2都是待验证待交换
        while index <= index_2:
            # 当值为0时，和0索引交换位置
            if nums[index] == 0:
                nums[index] = nums[index_0]
                nums[index_0] = 0
                index_0 += 1
            if nums[index] == 2:
                nums[index] = nums[index_2]
                nums[index_2] = 2
                index_2 -= 1
                index -= 1
            index += 1
