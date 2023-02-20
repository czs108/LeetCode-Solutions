# 51. N-Queens

# Runtime: 40 ms, faster than 99.70% of Python3 online submissions for N-Queens.

# Memory Usage: 14.8 MB, less than 56.24% of Python3 online submissions for N-Queens.


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols, digs, anti_digs = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        res = []

        def create_str() -> list[str]:
            str_board = []
            for row in board:
                str_board.append("".join(row))
            return str_board

        def backtrack(row: int) -> list[str]:
            if row == n:
                res.append(create_str())
                return

            for col in range(n):
                dig = row - col
                anti_dig = row + col
                if col in cols or dig in digs or anti_dig in anti_digs:
                    continue

                cols.add(col)
                digs.add(dig)
                anti_digs.add(anti_dig)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                digs.remove(dig)
                anti_digs.remove(anti_dig)
                board[row][col] = "."

        backtrack(0)
        return res