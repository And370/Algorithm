# 93. 复原IP地址
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
#  和 "192.168@1.1" 是 无效的 IP 地址。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  输入：s = "1111"
# 输出：["1.1.1.1"]
#  
# 
#  示例 4： 
# 
#  输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#  
# 
#  示例 5： 
# 
#  输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3000 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯算法 
#  👍 464 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrace(start):
            if start == n and len(result) == 4:
                results.append(".".join(result))
            else:
                # 此处限定右区间,因为必须使用全量数据
                # 保证连续性
                for i in range(start, start+3):
                    num = s[start:i + 1]
                    # 1.单结果长度不应该超过3段，若存在第四段则在下一步会被加入结果
                    # 2.num非空
                    # 3.排除非个位数的首位为0的num
                    # 4.num的区间[0,255],此处原本已保证为正数
                    if (len(result) <4) and\
                            num and \
                            not (len(num) >1 and num[0] == "0") \
                            and (int(num) <256):
                        result.append(num)
                        # 记得+1,否则会相同嵌套
                        backtrace(i+1)
                        result.pop()


        n = len(s)
        results = []
        result = []
        backtrace(0)

        return results
# leetcode submit region end(Prohibit modification and deletion)
