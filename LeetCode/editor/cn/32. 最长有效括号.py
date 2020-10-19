# 32. 最长有效括号
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 1027 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length_max = 0
        # 若为空也可以,但处理异常会更麻烦
        # 需要一个"垫",又由于长度=索引相减+1,则初始值为-1正好可以简化逻辑,但一眼看过去比较抽象
        stack = [-1]
        for index, value in enumerate(s):
            # 第一层的判断等于括号消消乐
            if value == "(":
                stack.append(index)
            else:
                stack.pop(-1)
                # 若未消耗垫子,则消消乐以后消去的间隔即为长度
                if stack:
                    length_max = max(index - stack[-1], length_max)
                # 否则将当前索引作为垫子加入栈
                else:
                    stack.append(index)
        return length_max
# leetcode submit region end(Prohibit modification and deletion)
