# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/6

"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""
"""
解:
注意好Python的"引用"和"赋值"的关系.
以及next的细节.
其中由于新的循环也存在节点交换,需要保存前一节点last.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not (head and head.next):
            return head
        # init
        # l2r:left to right
        # r2l:right to left
        node_l2r = head
        node_r2l = head.next
        first = True
        last = None
        while node_l2r and node_r2l:
            # 交换
            node_l2r.next = node_r2l.next
            node_r2l.next = node_l2r
            # print(node_l2r,node_r2l)
            # 首次,则重定义head
            if first:
                head = node_r2l
                first = False
            else:
                # 因为已经交换过了,所以next应该使用新的左侧,即r2l,此处易错
                last.next = node_r2l
                # print(last.val)
            last = node_l2r
            # print("cached:", last.val)
            # print("node_l2r before:", node_l2r.val)
            node_l2r = node_l2r.next
            # print("node_l2r after:", node_l2r.val)
            if node_l2r:
                node_r2l = node_l2r.next
        return head


if __name__ == '__main__':
    next = ListNode(0)
    for i in range(1, 5):
        pre = ListNode(i)
        pre.next = next
        next = pre
    print("before")
    while pre:
        print(pre.val)
        pre = pre.next
    solution = Solution()
    pre = solution.swapPairs(next)
    while pre:
        print(pre.val)
        pre = pre.next
