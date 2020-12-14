# 47. 全排列 II
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 回溯算法 
#  👍 542 👎 0


"""
解:
1.回溯算法
    给定一个含有重复的队列,队列里每个元素不可重复使用,且结果里不应存在重复的排列
    首先是一个【不放回】的全排列回溯算法
    考虑到不应该存在重复的排列,则有2种做法
        a.每次产出结果以后与当前结果进行set的对比
            此处逻辑简单但是没有剪枝,时间复杂度吃满每种情况,时间复杂度为O(n!)
        b.对于同递归深度中相同的元素进行缓存,不再选择,提前剪枝,
            为了方便,此处可先对nums排序
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def dfs(rest):
            if not rest:
                results.append(result[:])
            else:
                rest_copy = rest[:]
                # 缓存选择,跳过重复元素
                used = None
                for i in range(len(rest)):
                    if rest[i] != used:
                        cache = rest_copy.pop(i)
                        result.append(rest[i])

                        dfs(rest_copy)

                        result.pop()
                        rest_copy.insert(i,cache)
                        used = rest[i]
        results = []
        result = []
        nums.sort()
        dfs(nums)

        return results

# leetcode submit region end(Prohibit modification and deletion)
