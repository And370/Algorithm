# 49. 字母异位词分组
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 531 👎 0


"""
解:
1.质数哈希函数
    利用26位质数,构建哈希函数,此函数结果取决于元素含量,而与元素顺序无关
    每个字母组成一致的word其哈希值一致
2.利用Python现成的字典结合元组(元祖为不可变对象所以可直接序列化)
    将每个word的字幕占位表统一序列化
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # 1.质数哈希函数
        # def hash_prime(word):
        #     primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        #               101]
        #     hash_value = 1
        #     for char in word:
        #         hash_value = hash_value * primes[ord(char) - ord("a")]
        #     return hash_value
        #
        # results = {}
        # for word in strs:
        #     result = hash_prime(word)
        #     if results.get(result):
        #         results[result].append(word)
        #     else:
        #         results[result] = [word]
        # return list(results.values())

        # 2.元祖字典
        cache = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            if tuple(count) in cache:
                cache[tuple(count)].append(word)
            else:
                cache[tuple(count)] = [word]
        return list(cache.values())

# leetcode submit region end(Prohibit modification and deletion)
