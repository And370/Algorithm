# 350. 两个数组的交集 II
#
# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 
#  我们可以不考虑输出结果的顺序。 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 414 👎 0


"""
解:

"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
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

        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                result.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
