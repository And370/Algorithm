# 剑指 Offer 10- I. 斐波那契数列
#
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下： 
# 
#  F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 
# 
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：n = 5
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/ 
#  Related Topics 递归 
#  👍 63 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 递归
# class Solution:
#     def __init__(self):
#         self.cache = {0: 0, 1: 1}
#
#     def fib(self, n: int) -> int:
#         if n in self.cache:
#             return self.cache[n]
#         else:
#             self.cache[n] = (self.fib(n - 1) + self.fib(n - 2)) % 1000000007
#             return self.cache[n]
# 动态规划
class Solution:
    def fib(self, n: int) -> int:
        cache = [0, 1]
        if n <= 1:
            return cache[n]
        for index in range(2, n + 1):
            cache.append(cache[index - 1] + cache[index - 2])
        return cache[-1] % 1000000007
# leetcode submit region end(Prohibit modification and deletion)
