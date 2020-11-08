# 242. 有效的字母异位词
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 273 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache1 = {}
        cache2 = {}

        # 双边counter一下
        for to_char, cache in zip((s, t), (cache1, cache2)):
            for char in to_char:
                if char in cache:
                    cache[char] += 1
                else:
                    cache[char] = 0
        # print(cache1,cache2)

        # 互为真子集判断
        for key, value in cache1.items():
            if value != cache2.get(key):
                return False

        for key, value in cache2.items():
            if value != cache1.get(key):
                return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
