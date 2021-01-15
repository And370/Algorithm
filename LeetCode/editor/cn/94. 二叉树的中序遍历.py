# 94. 二叉树的中序遍历
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 820 👎 0


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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # 1.递归法
        # if not root:
        #     return root
        #
        # results = []
        #
        # def dfs(node):
        #     if not node:
        #         return
        #     else:
        #         dfs(node.left)
        #         results.append(node.val)
        #         dfs(node.right)
        #
        # dfs(root)
        #
        # return results

        # 2.迭代法

        if not root:
            return root

        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                node = stack.pop()
                results.append(node.val)
            else:
                # 注意要维持stack中所有节点的可用性
                # stack中有且仅有可用节点与None作为已处理标记
                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)

        return results

# leetcode submit region end(Prohibit modification and deletion)
