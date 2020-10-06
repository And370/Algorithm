# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/6

"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cache = set()
        # 双指针
        pre = None
        node = head
        while node:
            if node.val in cache:
                # 短路重复部分
                node = node.next
                pre.next = node
            else:
                cache.add(node.val)
                pre = node
                node = node.next
        return head
