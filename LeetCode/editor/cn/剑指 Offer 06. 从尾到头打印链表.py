# 剑指 Offer 06. 从尾到头打印链表
#
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1] 
# 
#  
# 
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
#  Related Topics 链表 
#  👍 63 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> [int]:
        copy = head
        result = []
        while copy:
            result.append(copy.val)
            copy = copy.next
        return result[::-1]

# leetcode submit region end(Prohibit modification and deletion)
