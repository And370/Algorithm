# 77. 组合
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 450 👎 0


"""
解:
1.常规回溯
    此处与全排列有2个区别在于:
    1.k!=n,则results的添加条件需要修改
    2.不可以重复,[1,2]和[2,1]是一样的,所以此处的撤回操作需要修改
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # 1.常规回溯
        # def backtrack(results, result, rest, count):
        #     if count == k:
        #         results.append(result[:])
        #     else:
        #         rest_copy = set(rest)
        #         for num in rest:
        #             result.append(num)
        #             rest_copy.remove(num)
        #             count += 1
        #             backtrack(results,result,rest_copy,count)
        #             # 注意此处不要撤销rest的remove操作
        #             result.pop()
        #             count-=1
        #
        #
        # rest = set(range(1, n + 1))
        # results = []
        # result = []
        # backtrack(results,result,rest,0)
        # return results

        # 2.使用双指针回溯
        def backtrack(start, end):
            if len(result) == k:
                results.append(result[:])
            else:
                # 此处注意剪枝
                # 剩余元素数量end-i+1(包含当前元素) 小于所需的个数k-len(result)
                # 再无计算必要
                for i in range(start, end):
                    if (end - i + 1) <= (k - len(result)):
                        break

                    result.append(i)
                    backtrack(i + 1, end)
                    result.pop()

        results = []
        result = []
        backtrack(1, n + 1)
        return results

# leetcode submit region end(Prohibit modification and deletion)
