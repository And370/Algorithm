# 203. 移除链表元素
#
# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#  
#  Related Topics 链表 
#  👍 516 👎 0


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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        node = head
        first = True
        while node:
            # 若为开头
            # 循环找到首个非指定值的节点
            if first:
                if node.val == val:
                    head = head.next
                    node = head
                else:
                    first = False
                pre = node
            # 非开头
            else:
                # 若相等,则节点下钻
                # 短路原节点
                if node.val == val:
                    node = node.next
                    pre.next = node
                # 否则前节点与当下节点正常下钻
                else:
                    pre = node
                    node = node.next

        return head
# leetcode submit region end(Prohibit modification and deletion)
