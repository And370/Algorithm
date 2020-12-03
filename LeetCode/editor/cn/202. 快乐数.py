# 202. 快乐数
#
# 编写一个算法来判断一个数 n 是不是快乐数。 
# 
#  「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为 1，那么这个数就是快乐数。 
# 
#  如果 n 是快乐数就返回 True ；不是，则返回 False 。 
# 
#  
# 
#  示例： 
# 
#  输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
#  Related Topics 哈希表 数学 
#  👍 492 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        to_check = False
        n_next = n
        # 检测是否存在历史值,若存在则进入死循环
        while to_check not in cache:
            # 增加历史值
            cache.add(to_check)
            # 各数位平方和
            n_next = sum([int(i) ** 2 for i in str(n_next)])
            # 平方和为1则为快乐数
            if n_next == 1:
                return True
            # 生成新检查值
            to_check = tuple(sorted(list(str(n_next))))
        return False
# leetcode submit region end(Prohibit modification and deletion)
