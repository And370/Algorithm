# 16. 最接近的三数之和
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 
#  👍 603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # 初始最小差值的和
        min_delta_sum = sum(nums[:2]) + nums[-1]
        # index右侧至少有left和right双指针
        for index in range(n - 2):
            left = index + 1
            right = n - 1
            while left < right:
                # 当前初始和
                s = nums[index] + nums[left] + nums[right]
                # 若和与目标一致,则最小化了差值,直接返回
                if s == target:
                    return target
                # 若当前和与目标的差值小于历史最小值,则更新
                # TODO 跳过重复值的逻辑可以考虑
                min_delta_sum = s if abs(s - target) < abs(min_delta_sum - target) else min_delta_sum
                # print(nums[index],nums[left],nums[right],min_delta_sum)
                # 根据情况移动左右坐标
                if s > target:
                    right -= 1
                if s < target:
                    left += 1
        return min_delta_sum
# leetcode submit region end(Prohibit modification and deletion)
