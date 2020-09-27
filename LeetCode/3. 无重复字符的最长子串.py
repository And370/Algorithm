# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/26

"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

"""
解:
这道题由于结果值只需要遍历一次字符串就可以得到,
故要重点处理的细节在于索引、长度、缓存字符集。

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res, char_dict = 0, 0, {}
        for index, char in enumerate(s):
            # 此处需要限定在当前的子串字符集里(char_dict[char] >= left)
            if char in char_dict and char_dict[char] >= left:
                # 重复则从其下一字符开始
                left = char_dict[char] + 1
                # print(index, char, "left", left)
            else:
                # 当前子串与历史最长子串取最大长度
                res = max(res, index - left + 1)
            char_dict[char] = index
            # print(index, char, "left:", left, 'res:', res, "delta:", index - left + 1)
        return res

