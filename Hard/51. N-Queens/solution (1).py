# 51. N-Queens

# Runtime: 116 ms, faster than 35.72% of Python3 online submissions for N-Queens.

# Memory Usage: 14.3 MB, less than 18.85% of Python3 online submissions for N-Queens.


class Solution:
    def __init__(self):
        self._boards = []
        self._n = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self._n = n
        board = [['.'] * n for _ in range(n)]
        self._backtrack(board, 0)
        return self._boards

    def _backtrack(self, board, row: int):
        if row == self._n:
            self._boards.append(Solution._buildStrBoard(board))
            return

        for col in range(self._n):
            if not Solution._isValid(board, row, col):
                continue
            else:
                board[row][col] = 'Q'
                self._backtrack(board, row + 1)
                board[row][col] = '.'

    @staticmethod
    def _buildStrBoard(board) -> List[str]:
        strBoard = []
        for i in range(len(board)):
            strBoard.append(''.join(board[i]))
        return strBoard

    @staticmethod
    def _isValid(board, row: int, col: int) -> bool:
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        return True