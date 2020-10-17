# 剑指 Offer 05. 替换空格
#
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        chars = []
        to_replace = " "
        for char in s:
            if char != to_replace:
                chars.append(char)
            else:
                chars.append("%20")
        return "".join(chars)
# leetcode submit region end(Prohibit modification and deletion)
