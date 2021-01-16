# 235. 二叉搜索树的最近公共祖先
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#  
# 
#  示例 2: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。 
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉搜索树中。 
#  
#  Related Topics 树 
#  👍 517 👎 0


"""
解:

注意利用二叉搜索树的有序性质
"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # # 1.剪枝法
        # if not root:
        #     return root
        #
        # p, q = p.val, q.val
        # ancestor = root
        #
        # # 当前点一直在所需两点的一侧时
        # # 可直接向一侧下钻,预剪枝
        # while True:
        #     if ancestor.val > p and ancestor.val > q:
        #         ancestor = ancestor.left
        #     elif ancestor.val < p and ancestor.val < q:
        #         ancestor = ancestor.right
        #     else:
        #         break
        #
        # return ancestor

        # 2.共同路径法

        p_path = []
        q_path = []

        to_p = root
        to_q = root

        p,q = p.val,q.val

        while to_p != p:
            p_path.append(to_p)
            if to_p.val > p:
                to_p = to_p.left
            elif to_p.val < p:
                to_p = to_p.right
            else:
                break

        while to_q != q:
            q_path.append(to_q)
            if to_q.val > q:
                to_q = to_q.left
            elif to_q.val < q:
                to_q = to_q.right
            else:
                break

        ancestor = None
        for to_p,to_q in zip(p_path,q_path):
            if to_p == to_q:
                ancestor = to_p
            else:
                break

        return ancestor
# leetcode submit region end(Prohibit modification and deletion)
