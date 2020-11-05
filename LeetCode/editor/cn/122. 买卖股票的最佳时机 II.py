# 122. 买卖股票的最佳时机 II
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  
# 
#  示例 2: 
# 
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 10 ^ 4 
#  0 <= prices[i] <= 10 ^ 4 
#  
#  Related Topics 贪心算法 数组 
#  👍 886 👎 0

"""
解:
1.以局部峰值将数据分段
* 峰值即为【当前值】小于【前一值】的时候的【前一值】
2.累积每次峰值及其之前最小值的绝对差
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        # 双指针
        low = prices[0]
        high = low

        for price in prices:
            # 持续爬坡
            if price > high:
                high = price
                continue
            # 若将遇回落,则卖出
            if price < high:
                result += (high - low)
                low = price
                high = low
        # 补充计算由于无回落未累积的最后一段
        result += (high - low)
        return result

# leetcode submit region end(Prohibit modification and deletion)
