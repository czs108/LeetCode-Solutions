# 289. Game of Life

# Runtime: 36 ms, faster than 40.78% of Python3 online submissions for Game of Life.

# Memory Usage: 14.1 MB, less than 10.00% of Python3 online submissions for Game of Life.


from collections import Counter


class Solution:
    # If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells.
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def game_of_life_infinite(live: set[tuple[int, int]]) -> set[tuple[int, int]]:
            ctr = Counter((I, J)
                        for i, j in live
                        for I in range(i - 1, i + 2)
                        for J in range(j - 1, j + 2)
                        if I != i or J != j)
            return {ij
                    for ij in ctr
                    if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

        live = {(i, j) for i, row in enumerate(board)
                for j, live in enumerate(row) if live}
        live = game_of_life_infinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)