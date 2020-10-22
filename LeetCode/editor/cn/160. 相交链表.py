# 160. 相交链表
#
# 编写一个程序，找到两个单链表相交的起始节点。 
# 
#  如下面的两个链表： 
# 
#  
# 
#  在节点 c1 开始相交。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, s
# kipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1
# ,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
#  1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4
# ]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而
#  skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#  
# 
#  
# 
#  注意： 
# 
#  
#  如果两个链表没有交点，返回 null. 
#  在返回结果后，两个链表仍须保持原有的结构。 
#  可假定整个链表结构中没有循环。 
#  程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 
#  
#  Related Topics 链表 
#  👍 848 👎 0

"""
1.比较尾部
将长的链表先跑,统一起跑线后逐一比较
2.铁人二项
A与B均在完成自己的链表的遍历以后,再去遍历对方的项目
若相交,则会在第二次赛程的交点碰面,否则仅会在终点的None碰面
"""
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         a, b = headA, headB
#         len_a, len_b = 0, 0
#         while a or b:
#             if a and b:
#                 a = a.next
#                 b = b.next
#                 len_a += 1
#                 len_b += 1
#             elif a:
#                 len_a += 1
#                 a = a.next
#             else:
#                 len_b += 1
#                 b = b.next
#
#         a, b, len_a, len_b = (headA, headB, len_a, len_b) if len_a > len_b else (headB, headA, len_b, len_a)
#
#         # 为了将相同的尾部长度比较,先统一起跑线
#         for i in range(len_a - len_b):
#             a = a.next
#         while b:
#             if a == b:
#                 return a
#             a = a.next
#             b = b.next
#         return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        return p1
# leetcode submit region end(Prohibit modification and deletion)
