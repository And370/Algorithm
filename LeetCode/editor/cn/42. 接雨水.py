# 42. 接雨水
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1751 👎 0
"""
TODO
逐层取结果，效率不高
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        cache = {}
        h_max = 0
        if not height:
            return 0
        # 获得每层高度的索引
        for index, h in enumerate(height):
            if h in cache:
                cache[h].append(index)
            else:
                cache[h] = [index]
                h_max = max(h_max, h)
        # print(cache)
        lower = h_max
        rains = 0
        min_left, max_right = len(height) - 1, 0
        while lower > 0:
            # 当无值时跳过该层
            if not cache.get(lower):
                # print("not get:",lower)
                rains += rain
            # 有值时
            else:
                # 取当前层最大边界(包括更高层的)
                min_left, max_right = min(min_left, cache[lower][0], cache[h_max][0]), \
                                      max(max_right, cache[lower][-1], cache[h_max][-1])
                # print(min_left, max_right)
                # 排除最高层层的情况，最高层无更高层，不需要取累加数量
                if h_max != lower:
                    cache[lower] += cache[h_max]
                rain = max_right - min_left + 1 - len(cache[lower])
                # print("rain:", lower, rain)
                rains += rain
                h_max = lower
            # 逐渐放低
            lower -= 1
        return rains
# leetcode submit region end(Prohibit modification and deletion)
