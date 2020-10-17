# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/7

"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。



说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1的存储容量肯定>=m+n,m为0则前n项需要以nums2赋值
        if not m:
            nums1[:n] = nums2
            return
        # nums2为空则nums1不需要改动
        if not n:
            return
        # 常规情况
        index = 0
        index_1, index_2 = n, 0
        nums1[n:m + n] = nums1[0:m]
        while True:
            if nums1[index_1] <= nums2[index_2]:
                nums1[index] = nums1[index_1]
                index_1 += 1
            else:
                nums1[index] = nums2[index_2]
                index_2 += 1
            index += 1
            if index_1 == m + n:
                nums1[index:] = nums2[index_2:]
                break
            if index_2 == n:
                break


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
