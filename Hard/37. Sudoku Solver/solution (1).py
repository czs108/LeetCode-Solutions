# 37. Sudoku Solver

# Runtime: 256 ms, faster than 57.93% of Python3 online submissions for Sudoku Solver.

# Memory Usage: 14.5 MB, less than 47.80% of Python3 online submissions for Sudoku Solver.


from collections import defaultdict

class Solution:
    # Backtracking
    def __init__(self) -> None:
        self._box_side: int = 3
        self._side: int = 9
        self._board: list[list[str]] = None
        self._rows: defaultdict(set) = None
        self._cols: defaultdict(set) = None
        self._boxes: defaultdict(set) = None

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._board = board
        self._rows = defaultdict(set)
        self._cols = defaultdict(set)
        self._boxes = defaultdict(set)

        for r in range(self._side):
            for c in range(self._side):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    self._rows[r].add(num)
                    self._cols[c].add(num)
                    self._boxes[self._box_idx(r, c)].add(num)
        self._backtrack(0, 0)

    def _backtrack(self, row: int, col: int) -> bool:
        if row == self._side - 1 and col == self._side:
            return True

        if col == self._side:
            col = 0
            row += 1

        if self._board[row][col] != ".":
            return self._backtrack(row, col + 1)

        box_idx = self._box_idx(row, col)
        for num in range(1, self._side + 1):
            if not self._can_place(row, col, num):
                continue

            self._board[row][col] = str(num)
            self._rows[row].add(num)
            self._cols[col].add(num)
            self._boxes[box_idx].add(num)
            if self._backtrack(row, col + 1):
                return True

            self._board[row][col] = "."
            self._rows[row].remove(num)
            self._cols[col].remove(num)
            self._boxes[box_idx].remove(num)

        return False

    def _can_place(self, row: int, col: int, num: int) -> bool:
        return num not in self._rows[row] and\
            num not in self._cols[col] and\
            num not in self._boxes[self._box_idx(row, col)]

    def _box_idx(self, row: int, col: int) -> int:
        return row // self._box_side * self._box_side + col // self._box_side