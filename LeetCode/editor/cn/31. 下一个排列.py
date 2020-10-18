# 31. 下一个排列
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组 
#  👍 696 👎 0
"""
解:
1.从右向左,找到第一个峰点(right)
* 查找峰点时注意边界条件
2.将峰点左侧一位值(left)与峰点右侧中大于左侧值的最小值(to_exchange)进行交换
* 注意此处的to_exchange的索引是nums[left+1:]的而不是nums的,如果有重复数字则可能产生错误
3.将left右侧的所有值进行排序
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        right = n - 1
        left = right - 1
        while left >= 0:
            if nums[right] > nums[left]:
                to_exchange = left + 1 + nums[left + 1:].index(min(filter(lambda x: x > nums[left], nums[left + 1:])))
                nums[left], nums[to_exchange] = nums[to_exchange], nums[left]
                nums[left + 1:] = sorted(nums[left + 1:])
                return
            else:
                right -= 1
                left -= 1
        nums.sort()

# leetcode submit region end(Prohibit modification and deletion)
