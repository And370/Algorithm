# 40. 组合总和 II
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  说明： 
# 
#  
#  所有数字（包括目标数）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ] 
#  Related Topics 数组 回溯算法 
#  👍 451 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        elif sum(candidates) == target:
            return [candidates]

        def backtrace(rest, target):
            if not target:
                results.add(tuple(sorted(result)))
            else:
                used = set()
                rest_copy = rest[:]
                for index, value in enumerate(rest):
                    # 同层相同值跳过【剪枝】
                    if value in used:
                        continue

                    rest_copy.pop(index)
                    result.append(value)
                    used.add(value)
                    target -= value

                    if target >= 0:
                        backtrace(rest_copy, target)
                        rest_copy.insert(index, value)
                        result.pop()
                        target += value
                    # 同层,剩余值不足【剪枝】
                    else:
                        rest_copy.insert(index, value)
                        result.pop()
                        target += value
                        break



        results = set()
        result = []
        candidates = sorted([n for n in candidates if n <= target], reverse=False)
        backtrace(candidates, target)

        return [list(res) for res in results]

# leetcode submit region end(Prohibit modification and deletion)
