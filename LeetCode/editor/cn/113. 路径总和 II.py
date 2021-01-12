# 113. 路径总和 II
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 
#  👍 405 👎 0


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

# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         if not root:
#             return []
#
#         results = []
#
#         def dfs(node, sum, paths):
#             if not node:
#                 return
#             if node.val == sum and not node.left and not node.right:
#                 results.append(paths + [node.val])
#             else:
#                 dfs(node.left, sum - node.val, paths + [node.val])
#                 dfs(node.right, sum - node.val, paths + [node.val])
#
#         dfs(root, sum, [])
#
#         return results

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        results = []
        paths = []

        def dfs(node, sum):
            if not node:
                return
            if node.val == sum and not node.left and not node.right:
                results.append(paths + [node.val])
            else:
                paths.append(node.val)
                dfs(node.left, sum - node.val)
                dfs(node.right, sum - node.val)
                paths.pop()

        dfs(root, sum)

        return results
# leetcode submit region end(Prohibit modification and deletion)
