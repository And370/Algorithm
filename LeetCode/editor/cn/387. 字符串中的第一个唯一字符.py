# 387. 字符串中的第一个唯一字符
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 283 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1.集合法
        cache = {}
        for char in s:
            if char in cache:
                cache[char] += 1
            else:
                cache[char] = 1
        for index, char in enumerate(s):
            if cache[char] == 1:
                return index
        return -1
        # # 2.数组法
        # cache = [0] * 26
        # for char in s:
        #     cache[ord(char) - 97] += 1
        # for index, char in enumerate(s):
        #     if cache[ord(char) - 97] == 1:
        #         return index
        # return -1

# leetcode submit region end(Prohibit modification and deletion)
