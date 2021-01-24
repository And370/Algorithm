# 290. 单词规律
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  示例1: 
# 
#  输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false 
# 
#  示例 4: 
# 
#  输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false 
# 
#  说明: 
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
#  Related Topics 哈希表 
#  👍 304 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        cache_p = {}
        cache_s = {}
        tag_p = 0
        tag_s = 0

        pattern = list(pattern)

        for i in range(len(pattern)):
            if pattern[i] not in cache_p:
                tag_p += 1
                cache_p[pattern[i]] = tag_p
            pattern[i] = cache_p[pattern[i]]

            if s[i] not in cache_s:
                tag_s += 1
                cache_s[s[i]] = tag_s
            s[i] = cache_s[s[i]]

            if s[i] != pattern[i]:
                return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
