# 36. Valid Sudoku

# Runtime: 96 ms, faster than 70.39% of Python3 online submissions for Valid Sudoku.

# Memory Usage: 14.4 MB, less than 42.60% of Python3 online submissions for Valid Sudoku.


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        # Use an array to record the status.
        rows = [[False] * N for _ in range(N)]
        cols = [[False] * N for _ in range(N)]
        boxes = [[False] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                # Check if the position is filled with number.
                if board[row][col] == ".":
                    continue

                pos = int(board[row][col]) - 1
                # Check the row.
                if rows[row][pos] == True:
                    return False
                else:
                    rows[row][pos] = True

                # Check the column.
                if cols[col][pos] == True:
                    return False
                else:
                    cols[col][pos] = True

                # Check the box.
                idx = (row // 3) * 3 + col // 3
                if boxes[idx][pos] == True:
                    return False
                else:
                    boxes[idx][pos] = True

        return True