# 263. 丑数
#
# 编写一个程序判断给定的数是否为丑数。 
# 
#  丑数就是只包含质因数 2, 3, 5 的正整数。 
# 
#  示例 1: 
# 
#  输入: 6
# 输出: true
# 解释: 6 = 2 × 3 
# 
#  示例 2: 
# 
#  输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#  
# 
#  示例 3: 
# 
#  输入: 14
# 输出: false 
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。 
# 
#  说明： 
# 
#  
#  1 是丑数。 
#  输入不会超过 32 位有符号整数的范围: [−231, 231 − 1]。 
#  
#  Related Topics 数学 
#  👍 156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for i in [25, 5, 9, 3, 4, 2]:
            while int(num / i) == num / i:
                num = num / i
        return True if num == 1 else False
# leetcode submit region end(Prohibit modification and deletion)
