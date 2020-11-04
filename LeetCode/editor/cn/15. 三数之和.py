# 15. 三数之和
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
#
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        n = len(nums)

        if not nums or n < 3:
            return result

        nums.sort()

        # 排序后若前2者大于0则无法拼出0
        # 若最大值小于0页无法拼出
        if sum(nums[:2]) > 0 or nums[-1] < 0:
            return result

        # 遍历每个元素
        for i in range(0, n - 2):
            # 当前值大于0则结束
            if nums[i] > 0:
                return result
            # 跳过重复值
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 以当前元素为核心点,寻求解剩余两数之和
            left = i + 1
            right = n - 1
            while left < right:
                # 符合则加入结果集
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 相同数跳过
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                # 加面加水
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result

# leetcode submit region end(Prohibit modification and deletion)
