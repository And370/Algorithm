# 18. 四数之和
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 666 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)

        if not nums or n < 4:
            return result

        nums.sort()
        # TODO
        # unduplicated = [0]
        # for index, num in enumerate(nums):
        #     if num == nums[unduplicated[-1]]:
        #         continue
        #     unduplicated.append(index)

        # 遍历每个元素
        for first in range(0, n - 3):
            # 保证改变
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, n - 2):
                # print("first", nums[first], "second", nums[second])
                # 保证改变
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # 以当前元素为核心点,寻求解剩余两数之和
                left = second + 1
                right = n - 1
                while left < right:
                    # 符合则加入结果集
                    if nums[first] + nums[second] + nums[left] + nums[right] == target:
                        result.append([nums[first], nums[second], nums[left], nums[right]])

                        # 相同数跳过
                        # TODO 此处存在重复计算
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    # 加面加水
                    elif nums[first] + nums[second] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1

        return result

# leetcode submit region end(Prohibit modification and deletion)
