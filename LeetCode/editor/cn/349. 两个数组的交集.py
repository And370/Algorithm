# 349. 两个数组的交集
#
# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中的每个元素一定是唯一的。 
#  我们可以不考虑输出结果的顺序。 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 290 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 异常情况
        if not all((nums1, nums2)):
            return []

        # 锁定小列表,排序
        nums1, nums2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        nums1.sort(), nums2.sort()
        
        # 无交集
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            return []

        # 结果容器与双指针
        result = []
        index1, index2 = 0, 0
        # 前交集值去重
        pre = None
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                if nums1[index1] != pre:
                    result.append(nums1[index1])
                    pre = nums1[index1]
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
