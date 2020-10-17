# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/5

"""
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        elements = {}
        queues = {1: [root]}
        layer = 1
        while queues.get(layer):
            for current_node in queues[layer]:
                # 注意不要重复覆盖式创建
                if not elements.get(layer):
                    elements[layer] = []
                if not queues.get(layer + 1):
                    queues[layer + 1] = []
                elements[layer].append(current_node.val)
                if current_node.left:
                    queues[layer + 1].append(current_node.left)
                    # print(queues)
                if current_node.right:
                    queues[layer + 1].append(current_node.right)
                    # print(queues)
            layer += 1
        # 降序排列,记得存在不满足的layer,layer - 1
        return [elements[l] for l in range(layer - 1, 0, -1)]
