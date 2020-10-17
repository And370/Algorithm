# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/27
"""
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""

"""
解:
1.合并有序数组并根据长度取index 略
由于两个数组有序,则取中位数可以直接进行交叉插入后进行取中位数index,这样的时间复杂度为O(m+n),
在m和n较大时,时间绝对值会远超过O(log(m+n)).

2.二分查找
利用二分法逐步舍弃不可能为中位数的一侧值.
主要在于边界条件的处理.
"""


# TODO
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1, nums2 = (nums1, nums2) if nums1[0] <= nums2[0] else (nums2, nums1)
        len_1, len_2 = len(nums1), len(nums2)
        is_odd = (len_1 + len_2) % 2
        if nums1[-1] <= nums2[0]:
            nums1 += nums2
            return nums1[(len_1 + len_2) // 2] \
                if is_odd \
                else sum(nums1[(len_1 + len_2) // 2],
                         nums1[(len_1 + len_2) // 2 - 1]) / 2

        i, j = len_1 // 2, len_2 // 2
        while True:
            pass
