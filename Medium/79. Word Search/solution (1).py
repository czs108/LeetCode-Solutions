# 79. Word Search

# Runtime: 7879 ms, faster than 22.07% of Python3 online submissions for Word Search.

# Memory Usage: 14.2 MB, less than 89.55% of Python3 online submissions for Word Search.


class Solution:
    # Backtracking
    def exist(self, board: list[list[str]], word: str) -> bool:

        def backtrack(row: int, col: int, suffix: str) -> bool:
            if len(suffix) == 0:
                return True
            elif row < 0 or row == len(board) or col < 0 or col == len(board[0]) \
                or board[row][col] != suffix[0]:
                return False

            board[row][col] = '#'
            match = False
            for row_offset, col_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if backtrack(row + row_offset, col + col_offset, suffix[1:]):
                    match = True
                    break
            board[row][col] = suffix[0]
            return match

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False