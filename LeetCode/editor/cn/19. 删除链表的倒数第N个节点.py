# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/29


"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""

"""
解:
若要一次遍历单向链表完成删除,则重点是要记录历史节点.
1.暴力记录法
将链表转换出一个列表副本,再进行后续处理.
缺点,空间复杂度为len(ListNode)

2.记录所需长度的链表
相比1所需的空间减少,需要长度为n的空间

3.双指针,仅记录关键节点信息
ListNode = 1->2->3->4->5
n = 3
这种时候实际是要将 1->2 和 ->4->5进行拼接,3被删除
则需要记录的关键节点为2、4、5
与n=2的关系为listNode[-(n+1)]、listNode[-(n-1)]和listNode[-(1)]
* 需要处理好边界情况
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n: int):
        left = head
        right = head
        for i in range(n):
            right = right.next
        if right:
            while right.next:
                left = left.next
                right = right.next
            left.next = left.next.next
            return head
        else:
            head = head.next
            return head


if __name__ == '__main__':
    next = ListNode(0)
    for i in range(1,5):
        pre = ListNode(i)
        pre.next = next
        next = pre
    print("before")
    # while pre.val:
    #     print(pre.val)
    #     pre = pre.next

    solution = Solution()
    pre = solution.removeNthFromEnd(next, 2)
    print("after")
    while pre:
        print(pre.val)
        pre = pre.next
