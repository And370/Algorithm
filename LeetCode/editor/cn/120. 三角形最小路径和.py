# 120. 三角形最小路径和
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。 
# 
#  
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划 
#  👍 655 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1.回溯思路
        # 时间复杂度过高
        # def dfs(path, row, index):
        #     if row == rows:
        #         if path_min:
        #             path_min[0] = min(path_min[0], path)
        #         else:
        #             path_min.append(path)
        #         print(path_min)
        #     else:
        #         # 每个节点存在2条路
        #         # 此处注意,首行的遍历不要溢出范围
        #         for index in range(index, min(index + 2, len(triangle[row]))):
        #             print(row, index)
        #             path += triangle[row][index]
        #             if path_min and path <= path_min[0]:
        #                 dfs(path, row + 1, index)
        #             if not path_min:
        #                 dfs(path, row + 1, index)
        #             path -= triangle[row][index]
        #
        # rows = len(triangle)
        # path = 0
        # path_min = []
        # dfs(path, 0, 0)
        # return path_min[0]

        # 2.动态规划
        # 仅缓存所需部分
        pre = [triangle[0][0]]
        # 长度为n时
        for row in range(1, len(triangle)):
            aft = []
            # 计算第2行,row=1
            for col in range(row + 1):
                # print(row, col)
                if col == 0:
                    aft.append(triangle[row][col] + pre[col])
                # 第2行的终点处索引为1
                elif col == row:
                    aft.append(triangle[row][col] + pre[col - 1])
                else:

                    aft.append(triangle[row][col] + min(pre[col], pre[col - 1]))
            pre = aft
        return min(pre)

# leetcode submit region end(Prohibit modification and deletion)
