# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/22
"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
"""
"""
解:
最长回文子串,从回文的定义出发:
1.一段子串的中心两侧互为逆序;
2.回文是套娃,回文子串删去头尾同等的长度,内部也是回文;
3.回文需要考虑中心点是单点中心还是双点中心,类似于求中位数.
4.初始状态为单字符为回文,双字符左右相等为回文

解法:
1.暴力法,遍历所有子串(大于当前最大子串的部分)
2.动态规划,借助初始状态逐步填充缓存矩阵避免重复计算
3.中心点扩展法,逐步假设每个点为中心,获取其最大回文距离
"""


class Solution:
    # TODO 写太乱了
    def longestPalindrome(self, s: str) -> str:
        # i,j,len,max_s
        self.max_pal = (0, 0, 0, "")
        self.cache = [[False] * len(s) for i in range(len(s))]
        for i, j in zip(range(1, len(s) + 1), range(1, len(s) + 1)):
            self.cache[i - 1][j - 1] = self.check(s, i, j)
        return self.max_pal[3]

    def is_palindrome(self, s):
        return True if s[:len(s) // 2:-1] == s[:-len(s) // 2] else False

    def check(self, s, i, j):
        if self.cache[i - 1][j - 1]:
            print("cached")
            return self.cache[i - 1][j - 1]
        if j - i <= self.max_pal[2]:
            print(1)
            return False
        else:
            if self.is_palindrome(s[i:j]):
                print("2.1")
                self.max_pal = i, j, j - i, s[i:j]
                self.cache[i - 1][j - 1] = s[i:j]
            else:
                print("2.2")
                self.check(s, i, j - 1)
                self.check(s, i + 1, j)


# DP法
class Solution():
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start_index = 0
        max_length = 1
        # 初始化DP缓存
        dp = [[False] * length for i in range(length)]

        for i in range(length):
            # 单中心点
            dp[i][i] = True
            # 双中心点
            if i < length - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start_index = i
                max_length = 2

        # 由初始缓存矩阵向更长距离推导缓存矩阵值
        delta = 2
        while delta <= length - 1:
            i = 0
            while i <= length - 1 - delta:
                j = i + delta
                print(delta, i, s[i], j, s[j], s[i:j + 1])
                # 根据子串头尾相等且内子串为回文串的特性递推
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_length = delta + 1
                    start_index = i
                    print("True", s[i:j + 1])
                i += 1
            delta += 1
        print(start_index, max_length)
        return s[start_index:start_index + max_length]


# 中心点拓展法
class Solution():
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start_index = 0
        max_length = 1
        for i in range(length):
            distance_1 = self.expand_from_center(s, i, i)
            distance_2 = self.expand_from_center(s, i, i + 1)
            # print(max_length, distance_1,distance_2,)
            if max(distance_1, distance_2) > max_length:
                # 取最大间隔
                max_length = max(distance_1, distance_2)
                # 单点间隔为单数,起始值为
                # 双点间隔为双数
                # (间隔 - 1)地板除2,为与中心店(左侧)的单侧间隔
                start_index = i - (max_length - 1) // 2
        return s[start_index:start_index + max_length]

    def expand_from_center(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    s = "123srf1234567654321dfw12345678987654321"
    solution = Solution()
    res = solution.longestPalindrome(s)
    print(res)
