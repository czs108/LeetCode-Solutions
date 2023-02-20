# 348. Design Tic-Tac-Toe


class TicTacToe:
    def __init__(self, n: int) -> None:
        self._rows: list[int] = [0] * n
        self._cols: list[int] = [0] * n
        self._dig: int = 0
        self._anti_dig: int = 0
        self._n: int = n

    def move(self, row: int, col: int, player: int) -> int:
        sig = 1 if player == 1 else -1
        self._rows[row] += sig
        self._cols[col] += sig
        if row == col:
            self._dig += sig
        if row == self._n - col - 1:
            self._anti_dig += sig

        if abs(self._dig) == self._n or abs(self._anti_dig) == self._n or abs(self._rows[row]) == self._n or abs(self._cols[col]) == self._n:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)