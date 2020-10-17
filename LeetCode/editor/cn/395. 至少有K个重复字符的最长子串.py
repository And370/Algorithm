# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/25

"""
395. 至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
"""
解:
1.暴力法
2.递归解
    a.设定discards为字符串待丢弃的字符集,存储不满足K个重复元素的字符
    b.初始化一个结果列表results,将满足条件的子串进行存储,为的是最终选出最长的子串
    c.若一个子串的discards字符集不存在时,即为满足条件的字符串,加入结果列表results;
    d.若一个子串的discards字符集不存在时,需要利用字符集的字符对当前子串进行split,切割的结果依然进行符合条件的判断,递归进入(c-d).
* 这里容易犯的误区在于,不能在split时,直接选择切割后的最长子串,这样是剪枝条件错误,因为其未对剪枝的子串进行条件判断.
? 每次split时取discards里最小/最大计数的字符,是否会有效率差异?
3.动态规划 TODO
此处考虑到切割字符串的效率较高,递归不会产生较深的递归栈,没有一定使用动态规划的必要.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(results, s, k):
            discards = {i for i in set(s) if s.count(i) < k}
            if not discards:
                print("True:", s)
                results.append(s)
            else:
                print("to_check:", s)
                # to_split =
                for s_sub in s.split(discards.pop()):
                    if s_sub:
                        helper(results, s_sub, k)

        results = []
        helper(results, s, k)
        return max(map(len, results)) if results else 0


if __name__ == '__main__':
    s = "zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee"
    k = 10
    solution = Solution()
    result = solution.longestSubstring(s, k)
    print(result)
