# 119. 杨辉三角 II
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 187 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1,1]
        now = [1]
        for i in range(rowIndex):
            left = [0] + now
            right = now + [0]
            now = [l + r for l, r in zip(left, right)]
        return now
# leetcode submit region end(Prohibit modification and deletion)
