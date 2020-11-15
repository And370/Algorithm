# 412. Fizz Buzz
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。 
# 
#  1. 如果 n 是3的倍数，输出“Fizz”； 
# 
#  2. 如果 n 是5的倍数，输出“Buzz”； 
# 
#  3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。 
# 
#  示例： 
# 
#  n = 15,
# 
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#  
#  👍 76 👎 0


"""
解:

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            res3 = not i % 3
            res5 = not i % 5
            if not (res3 or res5):
                result.append(str(i))
            elif res3 and res5:
                result.append("FizzBuzz")
            elif res3:
                result.append("Fizz")
            elif res5:
                result.append("Buzz")
        return result
# leetcode submit region end(Prohibit modification and deletion)
