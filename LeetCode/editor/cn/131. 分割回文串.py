# 131. 分割回文串
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。 
# 
#  返回 s 所有可能的分割方案。 
# 
#  示例: 
# 
#  输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ] 
#  Related Topics 回溯算法 
#  👍 432 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrace(start):
            if start == n:
                results.append(result[:])
            else:
                # 此处需要增加一个回文判断的逻辑
                # 但是整体框架不用变动
                for i in range(start, n):
                    substr = s[start:i + 1]
                    if substr == substr[::-1]:
                        result.append(substr)
                        backtrace(i + 1)
                        result.pop()
        n = len(s)
        results = []
        result = []

        backtrace(0)

        return results

# leetcode submit region end(Prohibit modification and deletion)
