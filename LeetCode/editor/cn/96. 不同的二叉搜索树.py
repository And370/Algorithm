# 96. 不同的二叉搜索树
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？ 
# 
#  示例: 
# 
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3 
#  Related Topics 树 动态规划 
#  👍 914 👎 0


"""
解:

n=6时:
nums = [1,2,3,4,5,6]
当3为根节点的结果为
[1,2]的结果 × [4,5,6]的结果

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numTrees(self, n):
        if n <= 1:
            return 1
        cache = [1, 1]
        # 动态规划
        # 从step=2开始逐步解决问题
        # cache[n]代表n的结果
        for step in range(2, n+1):
            # 初始化"和"
            ct = 0
            # 每个result(step) = 求和[to_sum从1~step,result(to_sum-1) * result(step-to_sum)]
            for to_sum in range(1,step+1):
                ct += cache[to_sum - 1] * cache[step - to_sum]
            # print(cache)
            cache.append(ct)
        return cache[-1]
# leetcode submit region end(Prohibit modification and deletion)
