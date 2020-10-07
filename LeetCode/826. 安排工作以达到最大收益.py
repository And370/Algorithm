# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/7

"""
826. 安排工作以达到最大收益
有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。

现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。

每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。

举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。

我们能得到的最大收益是多少？



示例：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。


提示:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  的范围是 [1, 10^5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-profit-assigning-work/
"""

"""
解:
先剔除一部分难度越大收益越低的工作,剩下的工作则为diff_prof_maps.(保证收益与难度单增)
再将工人按其能做的最好收益进行工作分配.
* 计算效率优化
    1.工人的收益查找使用累加索引
    2.对工人数量进行统计(此处统计是离散值,可再优化为分箱统计)
"""


class Solution:
    def maxProfitAssignment(self, difficulty: [int], profit: [int], worker: [int]) -> int:
        diff_prof_maps = [(dif, prof) for dif, prof in zip(difficulty, profit)]
        diff_prof_maps.sort(key=lambda x: x[0])

        max_prof = 0
        index = 0
        while index < len(diff_prof_maps):
            dif, prof = diff_prof_maps[index]
            if prof >= max_prof:
                max_prof = prof
                index += 1
            else:
                diff_prof_maps.pop(index)
        # print(diff_prof_maps)

        # result = 0
        # for work in set(worker):
        # TODO 每个work都重置index会造成重复计算量,每个count(worker)也会增加计算
        #     index = 0
        #     changed = False
        #     while index < len(diff_prof_maps) and diff_prof_maps[index][0] <= work:
        #         index += 1
        #         changed = True
        #     result += worker.count(work) * diff_prof_maps[index - 1][1] if changed else 0
        # return result

        result = 0
        index = 0
        changed = False

        worker.sort()
        work_maps = {}
        # TODO 可优化为分箱统计
        # 目前结合下一步代码类似于二次分箱
        for work in worker:
            if work not in work_maps:
                work_maps[work] = 1
            else:
                work_maps[work] += 1

        for work,count in work_maps.items():
            while index < len(diff_prof_maps) and diff_prof_maps[index][0] <= work:
                index += 1
                changed = True
            result += count * diff_prof_maps[index - 1][1] if changed else 0
        return result


if __name__ == '__main__':
    solution = Solution()
    difficulty = [13, 37, 58]
    profit = [4, 90, 96]
    worker = [34, 45, 73]
    result = solution.maxProfitAssignment(difficulty, profit, worker)
    print(result)
