# 68. 文本左右对齐
#
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  说明: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  示例: 
# 
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
#  Related Topics 字符串 
#  👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 初始化最终结果与每行局部变量
        results = []

        result = []
        first = True
        width = 0
        spaces = 0

        words_n = len(words)
        index = 0
        while index < words_n:
            word = words[index]
            word_len = len(word)
            # print(width, word, word_len)

            # 本行加词中
            # * 特别注意词长和句长一样的情况
            if first and word_len == maxWidth:
                results.append(word)
                index += 1
            elif width + 1 + word_len <= maxWidth:
                if width:
                    result.extend([" ", word])
                    width = width + 1 + word_len
                    spaces += 1
                else:
                    result.append(word)
                    width = width + word_len
                index += 1
                first = False
            # 本行结束
            # 注意若加入新单词超长了则该单词应该在下一行再次处理
            else:
                # 剩余空格
                space_delta_all = maxWidth - width
                # 若添加过word
                if spaces:
                    # 均分剩余空格
                    to_plus = space_delta_all // spaces
                    # 无法均分的剩余空格
                    space_delta = space_delta_all % spaces

                    to_replace = " " * (1 + to_plus)
                    result = [to_replace if value == " " else value for value in result]

                    # 剩余空格从左开始平铺
                    for i in range(space_delta):
                        result[1 + 2 * i] += " "
                # 未添加过则将剩余空格全部放在右侧
                else:
                    result.append(" " * space_delta_all)
                results.append("".join(result))

                # 局部变量重置
                result = []
                first = True
                width = 0
                spaces = 0
        # 增加判断,避免最后一行正好结束的情况
        if result:
            space_delta_all = maxWidth - width
            result.append(" " * space_delta_all)
            results.append("".join(result))
        return results
# leetcode submit region end(Prohibit modification and deletion)
