# 121. 买卖股票的最佳时机
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。 
# 
#  注意：你不能在买入股票前卖出股票。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#  Related Topics 数组 动态规划 
#  👍 1273 👎 0


"""
解:

"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            min_price, max_price = prices[0],prices[0]
            delta = 0
            prices = prices[1:]
            for j in prices:
                # 持续爬坡
                if j > max_price:
                    max_price = j
                # 若回落,重置
                elif j < min_price:
                    max_price = j
                    min_price = j
                # 比较每个差值
                if max_price - min_price > delta:
                    delta = max_price - min_price
            return delta
        return 0
# leetcode submit region end(Prohibit modification and deletion)
