# 48. 旋转图像
#
# 给定一个 n × n 的二维矩阵表示一个图像。 
# 
#  将图像顺时针旋转 90 度。 
# 
#  说明： 
# 
#  你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。 
# 
#  示例 1: 
# 
#  给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#  
# 
#  示例 2: 
# 
#  给定 matrix =
# [
#   [ 5][1][9,11],
#   [ 2][4][8,10],
#   [13][3][6][7],
#   [15,14,12,16]
# ]][
# 
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13][2][5],
#   [14][3][4][1],
#   [12][6][8][9],
#   [16][7,10,11]
# ]
#  
#  Related Topics 数组 
#  👍 625 👎 0


"""
解:
n = 4

(0,0) -> (0,3)
(0,3) -> (3,3)
(3,3) -> (3,0)
(3,0) -> (0,0)

(1,1) -> (1,2)
(1,2) -> (2,2)
(2,2) -> (2,1)
(2,1) -> (1,1)

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything][modify matrix in-place instead.
        """

        n = len(matrix) - 1

        # 旋转最外的n//2层
        for boundary in range(n // 2 + 1):
            # 每层边界旋转n-边界次，每次旋转4个值
            for delta in range(boundary, n - boundary):
                # 此处需要写出4个点的坐标,之后左右侧的值进行一个错位
                # 假设boundary = 0,delta = 1
                # 存储左上角
                tmp = matrix[boundary][delta]
                # 左下->左上,[0,1] = [2,0]
                matrix[boundary][delta] = matrix[n - delta][boundary]
                # 右下->左下,[2,0] = [3,2]
                matrix[n - delta][boundary] = matrix[n - boundary][n - delta]
                # 右上->右下,[3,2] = [1,3]
                matrix[n - boundary][n - delta] = matrix[delta][n - boundary]
                # 左上->右上,[1,3] = [0,1]
                matrix[delta][n - boundary] = tmp
                # print(matrix)

# leetcode submit region end(Prohibit modification and deletion)
