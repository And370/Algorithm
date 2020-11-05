# 189. 旋转数组
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 727 👎 0


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
