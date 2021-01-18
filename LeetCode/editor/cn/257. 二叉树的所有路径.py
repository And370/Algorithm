# 257. 二叉树的所有路径
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  输入:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
#  Related Topics 树 深度优先搜索 
#  👍 429 👎 0


"""
解:
此处以叶节点为终点,避免用空节点做终点时左右空节点重复
"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        results = []
        result = []

        def dfs(node):
            # 以叶节点为终点
            # 避免空节点做终点时,左右空节点重复计算
            if not node.left and not node.right:
                result.append(str(node.val))
                results.append("->".join(result))
                result.pop()
            else:
                result.append(str(node.val))
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                result.pop()

        dfs(root)

        return results

# leetcode submit region end(Prohibit modification and deletion)
