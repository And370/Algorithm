# 326. 3的幂
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。 
# 
#  整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 27
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 9
# 输出：true
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 45
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= n <= 231 - 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能不使用循环或者递归来完成本题吗？ 
#  
#  Related Topics 数学 
#  👍 136 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # # 1.逐步除3直至可为1则为3的幂
        # # 2.除3有余则非3的幂
        # while n >= 1:
        #     if n == 1:
        #         return True
        #     if n % 3:
        #         return False
        #     n = n / 3
        # return False

        # 3.计算数值范围内最大的3的幂m,以m对n求余,若有余则非
        return (n > 0) and not bool(1162261467 % n)

# leetcode submit region end(Prohibit modification and deletion)
