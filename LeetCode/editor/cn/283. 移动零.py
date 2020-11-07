# 283. 移动零
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 800 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 异常情况
        if n <= 1:
            return

        # 双指针
        zero, notzero = 0, 1
        # 双条件防索引溢出
        while zero < n and notzero < n:
            # 若零索引不为0,自增寻0
            if nums[zero]:
                zero += 1
                continue
            # 若非零索引值为0或索引值在零值左侧,自增寻非0
            if (not nums[notzero]) or notzero < zero:
                notzero += 1
                continue
            nums[zero], nums[notzero] = nums[notzero], nums[zero]
# leetcode submit region end(Prohibit modification and deletion)
