# 78. 子集
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 900 👎 0


"""
解:

"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(rest):
            # 每次均放入结果集
            # 不做条件限制

            rest_set = set(rest)
            for res in rest:

                rest_set.remove(res)
                result.append(res)

                results.append(result[:])

                # 不放回
                backtrace(rest_set)
                result.pop()

        results = [[]]
        result = []
        nums_set = set(nums)
        backtrace(nums_set)
        return results
# leetcode submit region end(Prohibit modification and deletion)
