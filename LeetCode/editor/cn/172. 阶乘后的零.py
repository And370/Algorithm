# 172. 阶乘后的零
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。 
# 
#  示例 1: 
# 
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零. 
# 
#  说明: 你算法的时间复杂度应为 O(log n) 。 
#  Related Topics 数学 
#  👍 373 👎 0
"""
解:
1.n! = n * (n-1) * ... * 1
2.个位数能相乘得到0的情况须得是(偶数*5)的组合
3.2*5~8*5 = 10 ~ 40,个位相乘最高也只能是1个0
4.由于阶乘中5随后紧跟4,则每次遇5的1次幂(仅)的倍数则得1个0
10的乘数中存在2个5的1次幂倍数(10和5)
25则为2个0
~
5^k次方为k个0
5.样本观察:
1~4     0
5~9     1
10~14   2
15~19   3
20~24   4
25~29   6
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            n = n // 5
            result += n
        return result
# leetcode submit region end(Prohibit modification and deletion)
