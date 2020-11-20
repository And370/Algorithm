# 55. 跳跃游戏
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个位置。 
# 
#  示例 1: 
# 
#  输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#  
# 
#  示例 2: 
# 
#  输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#  
#  Related Topics 贪心算法 数组 
#  👍 930 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        # 最后一位元素无意义
        nums.pop()

        n = len(nums)
        index = 1
        delta = 1

        # 从右向左，若遇到不可达元素，则增加间隔，否则视作到达当前元素即可
        # 将每个当前可达元素作为之后的目标元素
        while index <= n:
            if nums[-index] >= delta:
                nums[-index] = True
                delta = 1
            else:
                nums[-index] = False
                delta += 1
            index += 1
        return nums[0]

# leetcode submit region end(Prohibit modification and deletion)
