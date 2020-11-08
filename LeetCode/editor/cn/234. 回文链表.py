# 234. 回文链表
#
# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 756 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1.栈消法
        node = head
        n = 0
        # 获得长度,O(n)
        while node:
            node = node.next
            n += 1

        node = head
        stack = []
        # 走到中点
        for i in range(n // 2):
            stack.append(node.val)
            node = node.next

        # 若链长为单数,忽略中位节点
        if n % 2:
            node = node.next

        # 此处进行栈与链表剩余节点的对消
        while node:
            if node.val != stack.pop():
                return False
            node = node.next
        return True
# leetcode submit region end(Prohibit modification and deletion)
