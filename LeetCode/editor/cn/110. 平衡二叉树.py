# 110. 平衡二叉树
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -104 <= Node.val <= 104 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 568 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 1.自底向上,避免自顶向下重复计算底部节点
        if not root:
            return True

        self.result = True

        self.get_max_height(root)

        return self.result

    def get_max_height(self, node):
        # 此处若结果得出可较快跳出递归栈
        # 一旦结果变化,该函数的结果不再重要
        if not self.result:
            return 0
        if not node:
            return 0
        else:
            height_left = self.get_max_height(node.left)

            height_right = self.get_max_height(node.right)

            # 若左右节点差值大于1则非平衡树
            # 根+左+右 均需要满足该条件

            if abs(height_left - height_right) > 1:
                self.result = False
                # 同理,此处也可以立刻返回结果
                return 0
            return max(height_left, height_right) + 1
# leetcode submit region end(Prohibit modification and deletion)
