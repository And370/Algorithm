# 63. 不同路径 II
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
# 
#  示例 2： 
# 
#  
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] 为 0 或 1 
#  
#  Related Topics 数组 动态规划 
#  👍 456 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # 1.回溯算法
        # # 时间复杂度高
        # if not obstacleGrid or not obstacleGrid[0]:
        #     return 0
        #
        # def dfs(row, col):
        #     # print(row, col)
        #     if row == m - 1 and col == n - 1 and obstacleGrid[row][col] != 1:
        #         result[0] += 1
        #         # print("end")
        #     else:
        #         if row < m - 1 and not obstacleGrid[row + 1][col]:
        #             dfs(row + 1, col)
        #         if col < n - 1 and not obstacleGrid[row][col + 1]:
        #             dfs(row, col + 1)
        #
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # result = [0]
        # if obstacleGrid[0][0]:
        #     return 0
        # else:
        #     dfs(0, 0)
        #     return result[0]

        # 2.动态规划
        # 由于有且只可以向右和向下,则可以将【上/左侧】均看为路径为1
        # 这里尤其像是两侧为1的杨辉三角

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        row = 0
        while row < m and obstacleGrid[row][0] != 1:
            dp[row][0] = 1
            row += 1
        col = 0
        while col < n and obstacleGrid[0][col] != 1:
            dp[0][col] = 1
            col += 1
        # print(dp)

        for row in range(1, m):
            for col in range(1, n):
                # 注意这里是对路径矩阵的判断
                # 别写错成了dp矩阵的判断
                if not obstacleGrid[row][col]:
                    # 每个点的路径数可以是【左/上】点的路径数和
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        # print(dp)
        return dp[m - 1][n - 1]

# leetcode submit region end(Prohibit modification and deletion)
