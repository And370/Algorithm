# -*- coding: utf-8 -*-
# author:And370
# time:2020/8/15
import random
# from Sort import *
from Markov import *


# 归并排序
def check(func, *args):
    to_sort = [random.randrange(1, 10000) for i in range(100)]
    return func(to_sort, *args) == sorted(to_sort)


def merge_sort(nums: list):
    if len(nums) < 2:
        return nums

    split_line = len(nums) // 2
    nums1, nums2 = nums[:split_line], nums[split_line:]
    return sub_sort(merge_sort(nums1), merge_sort(nums2))


def sub_sort(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    i, j = 0, 0

    nums = []
    while i < len1 and j < len2:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    nums += nums1[i:]
    nums += nums2[j:]
    return nums


def quick_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    left, right = 0, n - 1
    pivot = n // 2

    while left != right:
        while (nums[left] <= nums[pivot]) and left != right:
            left += 1
        while (nums[right] >= nums[pivot]) and left != right:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[left], nums[pivot] = nums[pivot], nums[left]
    return quick_sort(nums[:pivot])+ quick_sort(nums[pivot:])


if __name__ == "__main__":
    # test
    print(check(quick_sort))
