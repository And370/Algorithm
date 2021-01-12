# 129. 求根到叶子节点数字之和
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。 
# 
#  例如，从根到叶子节点路径 1->2->3 代表数字 123。 
# 
#  计算从根到叶子节点生成的所有数字之和。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25. 
# 
#  示例 2: 
# 
#  输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026. 
#  Related Topics 树 深度优先搜索 
#  👍 301 👎 0


"""
解:

深度优先搜索

1.取左右子树的结果值
2.每次的结果为上层值进位(10倍历史值)+当前节点值

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = [0]

        def dfs(node, num):
            # 叶子节点
            if not node.left and not node.right:
                result[0] += num * 10 + node.val
            else:
                # 非叶子节点的左右子树
                num = num * 10 + node.val
                if node.left:
                    dfs(node.left, num)
                if node.right:
                    dfs(node.right, num)

        dfs(root, 0)
        return result[0]

# leetcode submit region end(Prohibit modification and deletion)
