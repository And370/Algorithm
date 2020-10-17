# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/5

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 节点存在
        if p and q:
            if p.val == q.val \
                    and self.isSameTree(p.left, q.left) \
                    and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        # 空节点
        elif p == q:
            return True
        # 不等
        else:
            return False
