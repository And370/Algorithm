# 98. 验证二叉搜索树
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 
#  👍 823 👎 0


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
    def isValidBST(self, root: TreeNode) -> bool:

        # 1.存储路径节点
        # 要存储大量的冗余对象,性能很差
        # if not root:
        #     return True
        # if (not root.left) and (not root.right):
        #     return True
        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)

        # 递归法
        def helper(node, left, right):
            if not node:
                return True
            else:
                # 若不符合条件则可立刻返回
                if node.val <= left or node.val >= right:
                    return False
                # 否则继续下钻
                else:
                    return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float('-inf'), float('inf'))
# leetcode submit region end(Prohibit modification and deletion)
