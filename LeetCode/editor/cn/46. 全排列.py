# 46. 全排列
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 956 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(result,nums_set):
            # 所有数都填完了
            if not nums_set:
                res.append(result[:])
            for num in nums_set:
                # 动态维护数组
                result.append(num)
                nums_set_copy = set(nums_set)
                nums_set_copy.remove(num)
                # 继续递归填下一个数
                backtrack(result,nums_set_copy)
                # 撤销操作
                result.pop()
                nums_set_copy.add(num)
        res = []
        result = []
        nums_set = set(nums)
        backtrack(result,nums_set)
        return res
# leetcode submit region end(Prohibit modification and deletion)
