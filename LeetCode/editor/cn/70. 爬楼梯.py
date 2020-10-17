# -*- coding: utf-8 -*-
# author:And370
# time:2020/10/5

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 -> 1,2 -> 2
        if n <= 2:
            return n
        else:
            calculated = [0, 1, 2]
            for i in range(3, n + 1):
                # N阶的方法数是其前两阶的方法数量和
                calculated.append(sum(calculated[-2:]))
        return calculated[-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(5)
    print(result)
