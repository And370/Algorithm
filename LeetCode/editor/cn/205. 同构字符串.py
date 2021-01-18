# 205. 同构字符串
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。 
# 
#  每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：s = "egg", t = "add"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "foo", t = "bar"
# 输出：false 
# 
#  示例 3： 
# 
#  
# 输入：s = "paper", t = "title"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  可以假设 s 和 t 长度相同。 
#  
#  Related Topics 哈希表 
#  👍 321 👎 0


"""
解:
同构的本质是将内容信息本身去除
仅保留位置信息

则将二者实现成仅记录位置信息的对象
此处的不匹配情况在迭代过程中即可发现,可及时返回结果
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cache_s, cache_t = {}, {}
        index = 0
        for sub_s, sub_t in zip(s, t):
            # 获取历史索引
            sub_s_index, sub_t_index = cache_s.get(sub_s), cache_t.get(sub_t)
            # 若索引不相同,则False
            # 相同下,若不存在,则建立索引
            if sub_s_index == sub_t_index:
                if not sub_s_index:
                    cache_s[sub_s] = index
                    cache_t[sub_t] = index
            else:
                return False
            index += 1
        # print(cache_s,cache_t)
        return True
# leetcode submit region end(Prohibit modification and deletion)
