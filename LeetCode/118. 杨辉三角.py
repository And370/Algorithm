# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/16

"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle/
"""


class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if not numRows:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        for i in range(1, numRows):
            left = result[i - 1] + [0]
            right = [0] + result[i - 1]
            result.append([l + r for l, r in zip(left, right)])
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 3
    result = solution.generate(n)
    print(result)
