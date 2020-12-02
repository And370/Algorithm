# 134. 加油站
#
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。 
# 
#  你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。 
# 
#  如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。 
# 
#  说明: 
# 
#  
#  如果题目有解，该答案即为唯一答案。 
#  输入数组均为非空数组，且长度相同。 
#  输入数组中的元素均为非负数。 
#  
# 
#  示例 1: 
# 
#  输入: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 
# 输出: 3
# 
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。 
# 
#  示例 2: 
# 
#  输入: 
# gas  = [2,3,4]
# cost = [3,4,3]
# 
# 输出: -1
# 
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。 
#  Related Topics 贪心算法 
#  👍 541 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 若gas总量小于消耗总量,不成行
        # 排除以后,则都有可行路径
        if sum(gas) < sum(cost):
            return -1

        if len(gas) <= 1:
            return 0

        # 差值
        deltas = [g - c for g, c in zip(gas, cost)]

        n = len(deltas)

        i = 0
        delta_acc = []
        delta_acc_index = []
        # 差值积分
        # 分段为正向与负向积分
        while i < n:
            delta_acc_index.append(i)
            is_same = deltas[i] >= 0
            delta_concat = deltas[i]

            i += 1
            while i < n and (deltas[i] >= 0) == is_same:
                delta_concat += deltas[i]
                i += 1
            delta_acc.append(delta_concat)
            # print(i)

        # 交错列的环形纠正
        # 首项必为正
        if (delta_acc[0] > 0) == (delta_acc[-1] > 0):
            delta_acc[0] += delta_acc.pop()
            delta_acc_index = [delta_acc_index[-1]] + delta_acc_index[1:-1]

        # 此处若细究,则需拆写,切片是O(n)复杂度
        if delta_acc[0] < 0:
            delta_acc = delta_acc[1:] + [delta_acc[0]]
            delta_acc_index = delta_acc_index[1:] + [delta_acc_index[0]]

        # 前后的交错集合
        delta_pre_next = []
        delta_pre_next_index = delta_acc_index[::2]
        i = 0
        n = len(delta_acc)
        while i < n - 1:
            delta_pre_next.append(delta_acc[i] + delta_acc[i + 1])
            i += 2
        # print("deltas", deltas)
        # print("delta_acc", delta_acc)
        # print("delta_pre_next", delta_pre_next)
        # print("delta_pre_next_index", delta_pre_next_index)

        # 剩余单项的情况
        if len(delta_pre_next_index) == 1:
            return delta_pre_next_index[0]
        # 索引最小负值
        res = delta_pre_next.index(min(delta_pre_next))
        # print(res)

        # 最小负值的下一项即一定为起始点
        # 此处做环形纠正
        if res == len(delta_pre_next) - 1:
            res = 0
        else:
            res += 1
        return delta_pre_next_index[res]
# leetcode submit region end(Prohibit modification and deletion)
