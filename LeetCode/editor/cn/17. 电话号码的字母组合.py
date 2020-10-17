# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/27

"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""

"""
解:
先给出基本字典
maps = {"2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"}
a.第二个字符的结果是基于第一个结果的笛卡尔积.
b.处理的过程重点在于生成式等list的解包等
"""


class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        maps = {"2": "abc", "3": "def", "4": "ghi",
                "5": "jkl", "6": "mno", "7": "pqrs",
                "8": "tuv", "9": "wxyz"}
        result = [""]
        # 遍历字符串
        for digit in digits:
            tmp = [result] * len(maps[digit])
            result = []
            # print(digit,tmp)
            # 遍历每个字符的笛卡尔积可能性
            for index, char in enumerate(maps[digit]):
                result.extend(list(map(lambda x: x + char, tmp[index])))
        return result


if __name__ == '__main__':
    solution = Solution()
    digits = "2345"
    result = solution.letterCombinations(digits)
    print(result)
