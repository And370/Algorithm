# 86. 分隔链表
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例: 
# 
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针 
#  👍 282 👎 0


"""
解:
双指针,先建立less链,再增加more链
"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        more = head
        less = head


        # 移动到符合自身条件的节点上
        while less.val >= x and less.next:
            less = less.next

        while more.val < x and more.next:
            more = more.next


        result = None
        result_index = None

        # 确保双区间均实际存在
        if more and less:
            # 遍历链表取小值
            while less:
                # print(less)
                if less.val < x:
                    # 当result已经建立时,添加小值
                    if result_index:
                        result_index.next = ListNode(less.val)
                        result_index = result_index.next
                    # 建立result
                    else:
                        result = ListNode(less.val)
                        result_index = result
                less = less.next

            while more:
                # print(more)
                if more.val >= x:
                    if result_index:
                        result_index.next = ListNode(more.val)
                        result_index = result_index.next
                    else:
                        result = ListNode(more.val)
                        result_index = result
                more = more.next

            return result
        return head

# leetcode submit region end(Prohibit modification and deletion)
