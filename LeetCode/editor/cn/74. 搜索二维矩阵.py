# 74. 搜索二维矩阵
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [], target = 0
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  0 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 288 👎 0


"""
解:
1.二分查找(行+列)
2.二分查找(整体)
    使用双指针进行范围缩小
    row,col根据实际的index来计算获得
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # 1.二分查找(行+列)
        # # print("test")
        # if (not matrix) or (not matrix[0]):
        #     return False
        #
        # if target < matrix[0][0] or target > matrix[-1][-1]:
        #     return False
        #
        # m = len(matrix) - 1
        # n = len(matrix[0]) - 1
        #
        # # print("行二分查找")
        # half = max((m + 1) // 2,1)
        # y = (m + 1) // 2
        # ct = 0
        # check = False
        #
        # while (ct <= 1) and (0 <= y <= m):
        #     # print(y,half)
        #     if matrix[y][0] == target or matrix[y][-1] == target:
        #         return True
        #     if matrix[y][0] < target < matrix[y][-1]:
        #         check = True
        #         break
        #     elif matrix[y][0] > target:
        #         half = (half + 1) // 2
        #         y -= half
        #     elif matrix[y][-1] < target:
        #         half = (half + 1) // 2
        #         y += half
        #     if half == 1:
        #         ct += 1
        #
        # if not check:
        #     return False
        #
        # # print("列二分查找")
        # half = max((n + 1) // 2,1)
        # x = (n + 1) // 2
        # ct = 0
        #
        # while (ct <= 1) and (0 <= x <= n):
        #     value = matrix[y][x]
        #     if value == target:
        #         return True
        #     elif value < target:
        #         half = (half + 1) // 2
        #         x += half
        #     elif value > target:
        #         half = (half + 1) // 2
        #         x -= half
        #     if half == 1:
        #         ct += 1
        # return False

        # # 2.二分查找(整体)
        # if not matrix or not matrix[0]:
        #     return False
        #
        # if matrix[0][0] == target or matrix[-1][-1] == target:
        #     return True
        #
        # m = len(matrix)
        # n = len(matrix[0])
        #
        # left = 0
        # right = m * n - 1
        #
        # half = True
        # while left < right and half:
        #     # print(left,right)
        #     half = (right - left) // 2
        #     median = left + half
        #     value = matrix[median // n][median % n]
        #     # print(median,value)
        #     if value == target:
        #         return True
        #     elif value > target:
        #         right = median
        #     else:
        #         left = median
        # return False

        # 官方写法
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # 二分查找
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
