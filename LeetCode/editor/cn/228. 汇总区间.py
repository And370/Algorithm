# 228. 汇总区间
#
# 给定一个无重复元素的有序整数数组 nums 。 
# 
#  返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 num
# s 的数字 x 。 
# 
#  列表中的每个区间范围 [a,b] 应该按如下格式输出： 
# 
#  
#  "a->b" ，如果 a != b 
#  "a" ，如果 a == b 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [-1]
# 输出：["-1"]
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [0]
# 输出：["0"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 20 
#  -231 <= nums[i] <= 231 - 1 
#  nums 中的所有值都 互不相同 
#  nums 按升序排列 
#  
#  Related Topics 数组 
#  👍 135 👎 0


"""
解:

1.保持last一定为上节点
2.每次差值不为1即断开连接,此时不忘要重置起点
3.若终点等于起点,直接添加结果

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # 1.双指针
        if not nums:
            return []

        results = []
        start = nums[0]
        last = nums[0]

        # 这里一个trick,用了一个必断开节点作为尾巴
        nums = nums[1:] + [start - 1]
        for num in nums:
            # print(start, last, num)
            # 断开连接
            # 记得每次断开连接时,都要把当前节点设定为开始节点
            if num - last != 1:
                if start == last:
                    results.append(str(last))
                else:
                    results.append("->".join((str(start), str(last))))
                start = num
            # 保证last一直是上节点
            last = num
        return results



# leetcode submit region end(Prohibit modification and deletion)
