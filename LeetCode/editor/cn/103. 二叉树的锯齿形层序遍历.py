# 103. 二叉树的锯齿形层序遍历
#
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索 
#  👍 367 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # 存储节点
        queue = [root]
        queue_next = []

        # 存储节点值
        results = []
        result = []

        left2right = True
        while queue:
            for node in queue:
                # 此处注意节点值是当前层
                result.append(node.val)
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)

            results.append(result if left2right else result[::-1])
            result = []

            queue = queue_next
            queue_next = []

            left2right = not left2right

        return results
# leetcode submit region end(Prohibit modification and deletion)
