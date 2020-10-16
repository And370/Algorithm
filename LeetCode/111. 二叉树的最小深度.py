# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/16

"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""
"""
解:
此处注意最小深度为到任意叶子节点的最短距离.

此处用递归
1.左右节点为空,返回1
2.左右节点不为空,取min(不为空节点的最小深度+1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        if not root.left and not root.right:
            return 1
        if root.left:
            return self.minDepth(root.left) + 1
        if root.right:
            return self.minDepth(root.right) + 1
