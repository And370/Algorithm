# 102. 二叉树的层序遍历
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 685 👎 0


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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []

        # 前层节点
        pre = [root]
        # 前层值
        pre_value = []
        # 当前层
        now = []

        while pre:
            res = pre.pop(0)
            # 若当前节点非空
            if res:
                pre_value.append(res.val)
                now.extend([res.left, res.right])
            print(pre_value)
            # 若pop后pre已空,且now非空
            # 此处最后一层的叶节点在被遍历前就加入到了results
            # 但其本身无法产生子节点
            if (not pre) and now:
                pre = now
                now = []
                results.append(pre_value)
                pre_value = []

        return results
# leetcode submit region end(Prohibit modification and deletion)
