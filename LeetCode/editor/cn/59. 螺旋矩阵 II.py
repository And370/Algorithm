# 59. 螺旋矩阵 II
#
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。 
# 
#  示例: 
# 
#  输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ] 
#  Related Topics 数组 
#  👍 268 👎 0


"""
解:

"""

# from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        matrix = [[False for i in range(n)] for j in range(n)]

        turn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        turns = 0

        row, col = 0, -1
        index = 1

        while index <= (n ** 2):
            # print(index)
            aft_row = row + turn[turns][0]
            aft_col = col + turn[turns][1]
            if 0 <= aft_row < n and 0 <= aft_col < n and not matrix[aft_row][aft_col]:
                # print("inner")
                matrix[aft_row][aft_col] = index
                row = aft_row
                col = aft_col
                index += 1
            else:
                turns = (turns + 1) % 4

        return matrix
# s = Solution()
# print(s.generateMatrix(3))
# leetcode submit region end(Prohibit modification and deletion)
