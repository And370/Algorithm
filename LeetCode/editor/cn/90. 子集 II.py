# 90. 子集 II
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ] 
#  Related Topics 数组 回溯算法 
#  👍 349 👎 0


"""
解:

"""
# leetcode submit region begin(Prohibit modification and deletion)
from copy import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        # 每次更新一次结果
        # 直到剩余元素用尽
        def back_track(results:set,rests:list):
            # print(results,rests)
            if not rests:
                return results
            else:
                results_copy = copy(results)
                element = rests.pop()
                results.add(tuple([element]))
                for res in results_copy:
                    # print(results,element)
                    results.add(tuple(sorted(list(res)+[element])))
                return back_track(results,rests)

        results = set([()])
        return list(back_track(results,nums))



# leetcode submit region end(Prohibit modification and deletion)
