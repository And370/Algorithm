# 114. 二叉树展开为链表
#
# 给定一个二叉树，原地将它展开为一个单链表。 
# 
#  
# 
#  例如，给定二叉树 
# 
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6 
# 
#  将其展开为： 
# 
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6 
#  Related Topics 树 深度优先搜索 
#  👍 681 👎 0


"""
解:
深度优先搜索

单次操作内容为:
1.原左子树展开,原右子树展开
2.原右子树存储
3.原左子树变成右子树
4.左子树置空
5.将右子树下探到底,其right接上原右子树

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        def dfs(node):
            if not node.left and not node.right:
                return
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                old_right = node.right
                node.right = node.left
                node.left = None
                while node.right:
                    node = node.right
                node.right = old_right

        dfs(root)
        return root

# leetcode submit region end(Prohibit modification and deletion)
