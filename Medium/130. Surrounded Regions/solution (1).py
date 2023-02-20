# 130. Surrounded Regions

# Runtime: 193 ms, faster than 41.67% of Python3 online submissions for Surrounded Regions.

# Memory Usage: 16.2 MB, less than 40.88% of Python3 online submissions for Surrounded Regions.


from itertools import product

class Solution:
    # Depth-First Search
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        def dfs(i: int, j: int) -> None:
            if board[i][j] != 'O':
                return
            # Mark the "escaped" cells.
            board[i][j] = 'E'
            if i - 1 >= 0:
                dfs(i - 1, j)
            if i + 1 < len(board):
                dfs(i + 1, j)
            if j - 1 >= 0:
                dfs(i, j - 1)
            if j + 1 < len(board[0]):
                dfs(i, j + 1)

        # Retrieve all border cells.
        borders = list(product(range(len(board)), [0, len(board[0]) - 1])) \
                + list(product([0, len(board) - 1], range(len(board[0]))))
        for i, j in borders:
            dfs(i, j)

        # Flip the captured cells ('O'->'X') and the escaped one ('E'->'O').
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'