# 348. Design Tic-Tac-Toe

# Time Limit Exceeded


class TicTacToe:
    def __init__(self, n: int) -> None:
        self._grid: list[list[int]] = [[0] * n for _ in range(n)]
        self._n: int = n

    def move(self, row: int, col: int, player: int) -> int:
        self._grid[row][col] = 1 if player == 1 else -1
        return player if self._has_won() else 0

    def _has_won(self) -> bool:
        for row in range(self._n):
            if abs(sum(self._grid[row])) == self._n:
                return True

        for col in range(self._n):
            if abs(sum([self._grid[row][col] for row in range(self._n)])) == self._n:
                return True

        if abs(sum([self._grid[i][i] for i in range(self._n)])) == self._n:
            return True

        if abs(sum([self._grid[i][self._n - i - 1] for i in range(self._n)])) == self._n:
            return True

        return False

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)