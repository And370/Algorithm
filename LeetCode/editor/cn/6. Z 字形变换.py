# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/25

"""
6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion/
"""

"""
解:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
转置
L E E T
    C
  O
D E I S
    H
  I
R I N G

 0   1   2   3   4   5   6   7   8   9   10
0,0 0,1 0,2 0,3 1,2 2,1 3,0 4,1 4,2 4,3 5,2

1.生成矩阵再拼接得到结果
a.本质是字符的新位置与字符的顺序存在映射关系,首先可以建立二维空串列表来存放字符(后续拼接);
* 此处为了方便,二维列表可使用与图例转置的方式进行存储和计算
b.建立起映射关系函数,逐一放入列表;
c.join拼接列表;

2.公式法   TODO
通过公式直接计算出每个结果串.

"""


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        length = len(s)
        to_join = []

        index = 0
        switch = True
        count = 0
        while index < length:
            if switch:
                # 补全长度
                # a.生成后检测长度,补全
                to_append = list(s[index:index+num_rows])
                to_append.extend([""] * (num_rows - len(to_append)))
                to_join.append(to_append)
                # b.生成时补全
                # to_join.append([s[index + i:index + i + 1]
                #                 if s[index + i:index + i + 1]
                #                 else ""
                #                 for i in range(num_rows)])
                index += num_rows
            else:
                # 这里的num_rows都需要-2的原因是实际上处于斜线的元素只有2(4-2)个
                # 斜线头尾的元素已经在直线上表示了
                for i in range(num_rows - 2):
                    to_join.append([s[index]
                                    if j == num_rows - 2 - count
                                    else ""
                                    for j in range(num_rows)])
                    index += 1
                    if index == length:
                        break
                    count += 1
                count = 0
            switch = not switch
        result = ""
        for i in range(num_rows):
            for j in range(len(to_join)):
                result += to_join[j][i]
        return result


if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 4
    solution = Solution()
    result = solution.convert(s, numRows)
    print(result)
