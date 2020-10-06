# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/6

"""
67. 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。



示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"


提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary/
"""
"""
解:
这里利用Python的语法糖的话会被快速求解,但那样就没有意义了.
所以这里应该老老实实选择逐位相加与进位的处理方式.
位运算也是可以的,但做题时可以选择更易读的方式表达思路.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        a, b = (a, b) if len_a > len_b else (b, a)
        a, b = list(a), list(b)
        if len(a) - len(b):
            b = ["0"] * (len(a) - len(b)) + b
        result = []
        carry = 0
        divisor = 2
        # print(a, b)
        for i in range(len(a) - 1, -1, -1):
            now = carry + int(a[i]) + int(b[i])
            carry, remainder = now // divisor, now % divisor
            # print("i", i,
            #       "now", now,
            #       "carry", carry,
            #       "remainder", remainder)
            result.append(remainder)
        result.append(carry)
        if not any(result):
            return "0"
        result.reverse()
        for char in result:
            if char:
                break
            else:
                result = result[1:]
        result = "".join(map(str, result))
        return result


if __name__ == '__main__':
    solution = Solution()
    a = "1"
    b = "111"
    result = solution.addBinary(a, b)
    print(result)
