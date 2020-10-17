# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/28

"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，
用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses/
"""

"""
解:
考虑到括号需要是有效的,其实可以将"()"看成一个整体,
之后用其对空串s=""进行不断的插入操作,
注意"()"仅在待插入的时候当做整体,一旦其已经存在于字符串s之后,即不再看做整体.
如:
"()"插入到4个字符的"()()"中存在4+1=5种可能性,当然其中 有部分排列是重复的.
这道题的生成逻辑及代码有部分与17题的电话号码字母组合相通.

result = [""]
# 遍历字符串
for digit in digits:
    tmp = [result] * len(maps[digit])
    result = []
    # print(digit,tmp)
    # 遍历每个字符的笛卡尔积可能性
    for index, char in enumerate(maps[digit]):
        result.extend(list(map(lambda x: x + char, tmp[index])))
        
        
1.[""]
2.[[""]]

start 
1.["()"] 

map str -> list 
2.[["(",")"]]

* (len(result) + 1)
3.[["(",")"],["(",")"],["(",")"]]

insert
4.[["()","(",")"],["(","()",")"]]

str join
5.["()()","(())"]

set
6.["()()","(())"] -> {"()()","(())"}
end
"""


class Solution:
    def generateParenthesis(self, n: int) -> list:
        if n == 1:
            return ["()"]

        def generater(s):
            results = set()
            for i in range(len(s) + 1):
                s_list = list(s)
                s_list.insert(i, "()")
                results.add("".join(s_list))
            return list(results)

        pre = ["()"]
        aft = []
        for i in range(n - 1):
            for pre_son in pre:
                aft.extend(generater(pre_son))
            pre = list(set(aft))
            aft = []
        return pre


if __name__ == '__main__':
    solution = Solution()
    n = 4
    result = solution.generateParenthesis(n)
    print(result)
