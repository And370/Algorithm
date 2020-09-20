# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/15

"""
51. N 皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。


提示：

皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
"""

"""
解:
回溯算法
逐行搜索,若可落子,则进入下一行;
若遍历一行后无法落子,则返回上一行;
若完成对最后一行的落子,则完成一次图,返回上一行; 
"""


class Solution:
    def solveNQueens(self, n: int) -> list:
        if n == 1:
            return [["Q"]]
        self.n = n
        # 结果
        self.results = []
        # 落点
        self.dots = []
        # 初始化禁止规则
        self.ban = {"row": set(),
                    "col": set(),
                    "main": set(),
                    "sub": set()}
        # 初始化原点
        dot = [0, 0]
        """
        逐行搜索,若可落子,则进入下一行;
        若遍历一行后无法落子,则返回上一行;
        若完成对最后一行的落子,则完成一次图,返回上一行; 
        """
        while True:
            # 传入当前点
            dot = self.row_research(dot)
            if dot:
                if dot[0] == self.n - 1:
                    self.results.append(self.generate_board())
                    dot = self.flash_back(2)
                else:
                    dot = [dot[0] + 1, 0]
            else:
                dot = self.flash_back(1)
                if dot == [0, n]:
                    return self.results

    def under_attack(self, dot) -> bool:
        """
        检测当前点是否处于攻击范围.
        :param dot: 点的坐标
        :return:
        """
        row, col = dot
        return col in self.ban["col"] or \
               (col - row) in self.ban["main"] or \
               (col + row) in self.ban["sub"]

    def add_dot(self, dot):
        """
        在棋盘及规则中添加点.
        :param dot:
        :return:
        """
        row, col = dot
        print("添加点:", row, col)
        self.ban["col"].add(col)
        self.ban["main"].add(col - row)
        self.ban["sub"].add(col + row)
        self.dots.append([row, col])

    def flash_back(self, times):
        """
        在棋盘及规则中删除点.
        :param dot:
        :return:
        """
        print("闪回前点位:", self.dots)
        for i in range(times):
            row, col = self.dots.pop(-1)
            print("闪回点:", [row, col])
            self.ban["col"].discard(col)
            self.ban["main"].discard(col - row)
            self.ban["sub"].discard(col + row)
        return [row, col + 1]

    def row_research(self, dot):
        """
        行内遍历
        有可用点则返回点,否则返回空列
        :param dot:
        :return:
        """
        while dot[1] < self.n:
            if self.under_attack(dot):
                print("当前点受攻击:", dot)
                dot[1] += 1
            else:
                print("找到点:", dot)
                self.add_dot(dot)
                return dot
        return []

    def generate_board(self):
        """
        根据当前点位生成棋盘.
        :return:
        """
        print("生成棋盘.")
        graph = [["."] * self.n for i in range(self.n)]
        for row, col in self.dots:
            graph[row][col] = "Q"
        graph = ["".join(i) for i in graph]
        return graph


if __name__ == '__main__':
    solve = Solution()
    results = solve.solveNQueens(5)
    for res in results:
        print(res)
