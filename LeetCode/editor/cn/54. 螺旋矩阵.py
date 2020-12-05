# 54. 螺旋矩阵
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。 
# 
#  示例 1: 
# 
#  输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2: 
# 
#  输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#  
#  Related Topics 数组 
#  👍 555 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 异常处理
        if not matrix or not matrix[0]:
            return []

        result = []

        # 四边分为四类型操作
        # 注意左边底边两边的顺序为逆序
        mode = "top"
        while matrix and matrix[0]:
            # print(result)
            if mode == "top":
                result += matrix.pop(0)
                mode = "right"
            elif mode == "right":
                for m in matrix:
                    result.append(m.pop())
                mode = "bot"
            elif mode == "bot":
                result += matrix.pop()[::-1]
                mode = "left"
            elif mode == "left":
                for m in matrix[::-1]:
                    result.append(m.pop(0))
                mode = "top"
        return result

# leetcode submit region end(Prohibit modification and deletion)
