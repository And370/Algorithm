# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/8

"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree/
"""
"""
解:
误区: 要使得其为镜像对称,则每个子树本身对称是不满足的.

1.迭代
应对使用层序遍历,逐层对比左右的元素.
除开根节点,所有层左半边等于右半边.
所以需要每层有一个cache装当前层节点的val.

2.递归
将误区中的概念加以改造:
并非子树对称,而应该是左子树的左子树与右子树的右子树对称,左子树的右子树和右子树的左子树对称.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        pre = [root]
        aft = []
        while any(pre):
            if len(pre) != 1:
                pre_val = list(map(lambda x: x.val if x else None, pre))
                # print(pre_val)
                if pre_val[len(pre_val) // 2:] != pre_val[:len(pre_val) // 2][::-1]:
                    return False
            for node in pre:
                aft.extend([node.left, node.right] if node else [None, None])
            pre = aft
            aft = []
        return True


# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def traverse(node1: TreeNode, node2: TreeNode):
            # 都为None
            if not node1 and not node2:
                return True
            # 仅一者存在
            if not (node1 and node2):
                return False
            # 都存在时要确认本身值相等
            if node1.val == node2.val:
                return traverse(node1.left, node2.right) and traverse(node1.right, node2.left)

        return traverse(root.left, root.right)
