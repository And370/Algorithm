# 64. 最小路径和
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 728 👎 0


"""
解:
这里约束了只能向下和向右,所以只需要最简单的逐格取前置最小并与当前格求和直到终点.
注意看题,不要陷入过多的情况考虑.
"""


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        M = len(grid)
        N = len(grid[0])

        for x in range(M):
            for y in range(N):
                if x and y:
                    grid[x][y] = min(grid[x-1][y],grid[x][y-1]) + grid[x][y]
                elif (not x) and (not y):
                    pass
                elif not x and y:
                    grid[x][y] = grid[x][y-1] + grid[x][y]
                else:
                    grid[x][y] = grid[x-1][y] + grid[x][y]
        return grid[x][y]

# leetcode submit region end(Prohibit modification and deletion)
