# 52. N-Queens II


class Solution:
    # Backtracking
    def totalNQueens(self, n: int) -> int:
        cols, digs, anti_digs = set(), set(), set()

        def backtrack(row: int) -> int:
            if row == n:
                return 1

            count = 0
            for col in range(n):
                dig = row - col
                anti_dig = row + col
                if col in cols or dig in digs or anti_dig in anti_digs:
                    continue

                cols.add(col)
                digs.add(dig)
                anti_digs.add(anti_dig)

                count += backtrack(row + 1)

                cols.remove(col)
                digs.remove(dig)
                anti_digs.remove(anti_dig)
            return count

        return backtrack(0)