# 1. 两数之和
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9537 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针
        index_1 = 0
        index_2 = len(numbers) - 1

        # 左右逼夹
        while index_1 < index_2:
            tmp = numbers[index_1] + numbers[index_2]
            if tmp == target:
                return [index_1 + 1, index_2 + 1]
            elif tmp < target:
                index_1 += 1
            else:
                index_2 -= 1
        return []
# leetcode submit region end(Prohibit modification and deletion)
