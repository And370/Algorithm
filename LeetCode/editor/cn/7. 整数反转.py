# 7. 整数反转
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学 
#  👍 2311 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 1.切片法
        # # 额外k空间
        # k = k % len(nums)
        # tmp = nums[-k:]
        # nums[k:] = nums[:-k]
        # nums[:k] = tmp

        # 2.反转法
        k = k % len(nums)
        nums.reverse()
        for index in range(k):
            # print(index, nums)
            if index < k - 1 - index:
                nums[index], nums[k - 1 - index] = nums[k - 1 - index], nums[index]
            else:
                break
        count = 0
        for index in range(k, len(nums)):
            if index < len(nums) - 1 - count:
                nums[index], nums[len(nums) - 1 - count] = nums[len(nums) - 1 - count], nums[index]
            else:
                break
            count += 1
# leetcode submit region end(Prohibit modification and deletion)
