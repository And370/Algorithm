# 199. 二叉树的右视图
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  示例: 
# 
#  输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 390 👎 0


"""
解:
广度优先搜索+取每层树的最右节点
"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        results = []
        queue = [root]
        queue_next = []
        result = []

        while queue:
            for node in queue:
                result.append(node.val)
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)
            queue = queue_next
            queue_next = []
            results.append(result)
            result = []

        return [res[-1] for res in results]
# leetcode submit region end(Prohibit modification and deletion)
