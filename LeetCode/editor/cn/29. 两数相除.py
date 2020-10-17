# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/8

"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2


提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0):
            minus = False
            if dividend < 0:
                dividend = -dividend
                divisor = -divisor
        else:
            minus = True
            if dividend <= 0:
                dividend = -dividend
            else:
                divisor = -divisor

        if dividend < divisor:
            return 0

        multiple = 1
        cache = [(1, divisor)]
        divisor_new = divisor
        while dividend >= divisor_new:
            divisor_new += divisor_new
            multiple += multiple
            cache.append((multiple, divisor_new))

        print(cache)

        count = 0
        index = len(cache) - 2
        while index >= 0:
            if dividend >= cache[index][1]:
                dividend -= cache[index][1]
                count += cache[index][0]
                print(dividend,cache[index])
            index -= 1


        result = -count if minus else count

        return result if result >= -2147483648 and result <= 2147483647 else 2147483647

if __name__ == '__main__':
    solution = Solution()
    dividend,divisor = 2147483647,3
    result = solution.divide(dividend,divisor)
    print(result)


