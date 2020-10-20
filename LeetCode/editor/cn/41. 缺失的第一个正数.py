# 41. 缺失的第一个正数
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,0]
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: [3,4,-1,1]
# 输出: 2
#  
# 
#  示例 3: 
# 
#  输入: [7,8,9,11,12]
# 输出: 1
#  
# 
#  
# 
#  提示： 
# 
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。 
#  Related Topics 数组 
#  👍 821 👎 0
"""
解:
缺失的首个正数,从可以考虑从1->?循环.
那么这个?怎么限定?
考虑到长度为n的数组,其最多只能覆盖1-n的范围,则循环的上限为n或者n+1,稍后识情况而定.
长度为n的数字要找到其缺失的值,则想到的是从1-n进行n桶排序
但是数组为乱序,则若需要查找第1和第2到第n的值所在index,需要每次进行一次遍历
另一种做法是将[当前的值]与[将其作为索引的值进行交换]一直到[当前位置的值]与[其索引值]相等或者其超出索引范围
此处为 value = index + 1
"""
# from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        for index in range(n):
            num = nums[index]
            while 0 < num <= n and nums[num - 1] != num:
                # 存储得已知处未知值
                tmp = nums[num - 1]
                # 将已知值放入对应位置
                nums[num - 1] = num
                # 当前值放入原未知值
                nums[index] = tmp
                # 进行至当前值不在索引范围内
                num = tmp
        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
        return n + 1


# leetcode submit region end(Prohibit modification and deletion)
# if __name__ == '__main__':
#     solution = Solution()
#     solution.firstMissingPositive([3, 4, -1, 1])
