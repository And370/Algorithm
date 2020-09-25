# -*- coding: utf-8 -*-
# author:And370
# time:2020/9/14

"""
给定一个表示分数的非负整数数组。
玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：

输入：[1, 5, 2]
输出：False
解释：一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。
 

提示：

1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于 10000000 。
如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解:
这里有一个误区在于会想当然地以为"因为只能取数组头尾端,所以最优策略就是取两端最大(贪心算法)."
实际上数组的信息对于玩家双方是全透明的.
这个游戏更像是下棋,尤其是围棋.需要"看很多步".
"看很多步"就是一个递归的栈思想.

1.递归解法
这里需要考虑机会成本的问题,选择头即代表着自己将剩下尾段的最优解给到对方,选择尾同理.
    a. 头 + 后段最优解
    b. 尾 + 前段最优解
    * c. a与b的差值即为收益,定义为delta

最优收益即为最优解的递归累加收益,从最顶层剥洋葱:
max_delta(a,b) = max_delta(max_delta(a,b),max_delta(a,b)) = ……
以下max_delta简称为F
当选择最上层(a,b)中较大的值,即为赢家.
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 比较左右选择的差值(各自最优解)
        # 设待选择的值左右索引为left和right
        def max_delta(left, right):
            # 当剩唯一值时,直接返回
            if left == right:
                return nums[left]
            # 选择左边时,与右侧最优解的差值进行比较
            choose_left = nums[left] - max_delta(left + 1, right)
            # 选择右边时,同理
            choose_right = nums[right] - max_delta(left, right - 1)
            # 返回最优解的差值,最正值
            return max(choose_left, choose_right)

        return max_delta(0, len(nums) - 1) >= 0


"""
2.增加缓存
考虑到无论最开始选择a还是b,其在求最优解的过程均会求解公共子数组的最优解,如:
[1,2,3,4,5,6]
F(F(1:2~6),F(1~5:6)) = F(F(左边被拆为 F(2:3~6),F(2~5:6) ), F(右边被拆为 F(1:2~5),F(2~4:5)) )
这里会发现,2~5这个子数组是重复的!
增加缓存需要作为一块公共区域被递归函数读取和写入:
    1.未曾计算的,计算后加入缓存
    2.计算过的,直接返回结果
这里的实现通常来说可以用dict或者json进行处理;
但是考虑到公共子数组的的特点是需要由[头,尾]定义区间,则此处使用二维数组(在Python中是二维嵌套列表).
头和尾的取值区间均在[0,len(nums)]
所以其为 len(nums) * len(nums) 的二维数组/矩阵cache.
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 差值缓存
        cache = [[None] * len(nums) for i in range(len(nums))]

        # 比较左右选择的差值(各自最优解)
        # 设待选择的值左右索引为left和right
        def max_delta(left, right):
            # 当剩唯一值时,直接返回
            if left == right:
                return nums[left]
            # 若缓存中存在，则直接返回函数结果
            if cache[left][right] != None:
                # print((left,right,cache[left][right]))
                return cache[left][right]
            else:
                # 选择左边时,与右侧最优解的差值进行比较
                choose_left = nums[left] - max_delta(left + 1, right)
                # 选择右边时,同理
                choose_right = nums[right] - max_delta(left, right - 1)

                cache[left][right] = max(choose_left, choose_right)
                # 返回最优解的差值,最正值
                return cache[left][right]

        return max_delta(0, len(nums) - 1) >= 0


"""
3.动态规划
递归对于形为二位矩阵的缓存的填充顺序不清晰,且栈深大了存在溢出问题(Python栈深默认999,本题限定了数组长度,不会溢出).
如果一开始就可以顺序地计算出矩阵中所有值,则一旦算出cache[0][len(nums)-1]的值,问题本身就解决了.
这里首先对当矩阵出现唯一值的情况进行填充,即[i,i]均为长度为1的子数组值,如:[3].
之后对矩阵一端逐步扩展求值.
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        # 差值缓存
        cache = [[None] * length for i in range(length)]
        # 剩余单数差值存储
        for i in range(length):
            cache[i][i] = nums[i]
        i = length - 2
        j = i + 1
        while i >= 0:
            while j < length:
                choose_left = nums[i] - cache[i + 1][j]
                choose_right = nums[j] - cache[i][j - 1]
                cache[i][j] = max(choose_left, choose_right)
                # print(cache[i][j])
                j += 1
            i -= 1
            j = i + 1
        # print(cache)
        return cache[0][length - 1] >= 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.PredictTheWinner([1, 2, 123, 879, 5, 6, 7, 8, 9, 777, 23, 123, 24, 2144])
    print(result)
