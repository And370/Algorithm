# 56. 合并区间
#
# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 714 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # 根据左区间排序
        intervals = sorted(intervals, key=lambda x: x[0])

        # 初始化第一位
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            # 取当前待比较
            now_inter = results[-1]
            # 取新待比较
            next_inter = intervals[i]

            # 若当前右区间大于等于新待比较的值,则通过二者右界限合并区间并更新当前结果值
            # 否则直接新增下一区间
            if now_inter[1] >= next_inter[0]:
                now_inter[1] = max(now_inter[1], next_inter[1])
                results[-1] = now_inter
            else:
                results.append(next_inter)
        return results
# leetcode submit region end(Prohibit modification and deletion)
