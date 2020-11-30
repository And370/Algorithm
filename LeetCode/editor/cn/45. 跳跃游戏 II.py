# 45. 跳跃游戏 II
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 754 👎 0


"""
解:
n:数组长度

1.逐元素更新最佳跳跃值,且以第一步的最佳值为边界
2.若当前元素已达边界,则边界更新为最佳跳跃值,并增加跳跃次数,这样相当于,每次跳跃都为最远处

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        n = len(nums)

        max_value, step, boundary = 0, 0, 0

        for index in range(n - 1):
            # 当前最大值
            max_value = max(max_value, index + nums[index])
            # 若遇到当前跳跃边界,则进一步
            if index == boundary:
                boundary = max_value
                step += 1
        return step

# leetcode submit region end(Prohibit modification and deletion)
