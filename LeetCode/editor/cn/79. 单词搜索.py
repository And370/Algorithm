# 79. 单词搜索
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 702 👎 0


"""
解:

"""
# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        # 确认原材料数量充足
        word_ct = Counter(word)
        board_flatten = sum(board, [])
        board_ct = Counter(board_flatten)
        for k, v in word_ct.items():
            if v > board_ct.get(k, 0):
                return False

        def next_char(x, y, index):
            # 上下左右的坐标
            # 限定坐标范围
            # 限定未使用过的坐标
            if index >= n:
                return []
            return [loc for loc in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
                    if (0 <= loc[0] < len(board))
                    and (0 <= loc[1] < len(board[0]))
                    and board[loc[0]][loc[1]]
                    and board[loc[0]][loc[1]] == word[index]]

        def backtrace(locs, index):
            if index == n:
                return True
            else:
                for x, y in locs:
                    # print(board[x][y])
                    # 使用过的标记
                    board[x][y] = False
                    # 下一个值的坐标范围
                    locs_new = next_char(x, y, index + 1)
                    # 检测到一个可用即为True
                    if backtrace(locs_new, index + 1):
                        return True
                    # 恢复标记
                    board[x][y] = word[index]

        word = list(word)
        locs = []
        n = len(word)

        # x:range(len(board))
        # y:range(len(board[0]))
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    locs.append((x, y))

        return bool(backtrace(locs, 0))
# leetcode submit region end(Prohibit modification and deletion)
