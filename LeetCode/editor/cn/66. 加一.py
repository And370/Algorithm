# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/5
"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits[-1] += 1
        tag = -1
        while digits[tag] == 10:
            if digits[:tag]:
                digits[tag - 1] += 1
            else:
                digits.insert(0, 1)
            digits[tag] = 0
            tag -= 1
        return digits


if __name__ == '__main__':
    solution = Solution()
    digits = [3,9,9]
    result = solution.plusOne(digits)
    print(result)
