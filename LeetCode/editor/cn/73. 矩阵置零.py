# 73. 矩阵置零
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。 
# 
#  示例 1: 
# 
#  输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#  
# 
#  示例 2: 
# 
#  输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ] 
# 
#  进阶: 
# 
#  
#  一个直接的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。 
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。 
#  你能想出一个常数空间的解决方案吗？ 
#  
#  Related Topics 数组 
#  👍 337 👎 0


"""
解:
1.记录所有0点的xy轴,统一更新


2.每次遇0即刻更新

"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not (matrix and matrix[0]):
            return

        # # 1.记录历史0值的坐标
        # # O(k)复杂度,k为0的数量
        #
        # xs = set()
        # ys = set()
        #
        # # 查找0值点并将坐标加入
        # for x in range(len(matrix)):
        #     for y in range(len(matrix[0])):
        #         if matrix[x][y] == 0:
        #             xs.add(x)
        #             ys.add(y)
        #
        # # 将涉及0的坐标点数据全部更新为0
        # for x in range(len(matrix)):
        #     for y in range(len(matrix[0])):
        #         if x in xs or y in ys:
        #             matrix[x][y] = 0

        # 2.每次遇0即刻更新矩阵横纵值

        # 查找0值点
        # 若为0值则沿坐标点x及y轴进行遍历
        # 非原点的非0点赋值为False
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    matrix[x][y] = 'tag'
                    for x_tmp in range(len(matrix)):
                        if not matrix[x_tmp][y]:
                            break
                        else:
                            matrix[x_tmp][y] = 'tag'
                    for y_tmp in range(len(matrix[0])):
                        if not matrix[x][y_tmp]:
                            break
                        else:
                            matrix[x][y_tmp] = 'tag'
        # print(matrix)
        # 将涉及0的坐标点数据全部更新为0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] =="tag":
                    matrix[x][y] = 0

# leetcode submit region end(Prohibit modification and deletion)
