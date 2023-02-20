# 773. Sliding Puzzle

# Runtime: 40 ms, faster than 90.31% of Python3 online submissions for Sliding Puzzle.

# Memory Usage: 14.3 MB, less than 65.62% of Python3 online submissions for Sliding Puzzle.


from collections import deque

State = tuple[tuple[int, int, int], tuple[int, int, int]]

class Solution:
    _END: State = ((1, 2, 3), (4, 5, 0))
    _BLANK: int = 0

    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ((board[0][0], board[0][1], board[0][2]), (board[1][0], board[1][1], board[1][2]))
        if start == self._END:
            return 0

        que = deque()
        visited = {}
        que.append(start)
        visited[start] = 0

        while len(que) > 0:
            curr = que.popleft()
            for neighbor in self._neighbors(curr):
                if neighbor not in visited:
                    visited[neighbor] = visited[curr] + 1
                    que.append(neighbor)
                    if neighbor == self._END:
                        return visited[neighbor]
        return -1

    @classmethod
    def _neighbors(cls, state: State) -> list[State]:
        ((a, b, c), (d, e, f)) = state
        neighbors = []
        if a == cls._BLANK:
            neighbors.append(((b, a, c), (d, e, f)))
            neighbors.append(((d, b, c), (a, e, f)))
        elif b == cls._BLANK:
            neighbors.append(((b, a, c), (d, e, f)))
            neighbors.append(((a, c, b), (d, e, f)))
            neighbors.append(((a, e, c), (d, b, f)))
        elif c == cls._BLANK:
            neighbors.append(((a, c, b), (d, e, f)))
            neighbors.append(((a, b, f), (d, e, c)))
        elif d == cls._BLANK:
            neighbors.append(((d, b, c), (a, e, f)))
            neighbors.append(((a, b, c), (e, d, f)))
        elif e == cls._BLANK:
            neighbors.append(((a, b, c), (e, d, f)))
            neighbors.append(((a, b, c), (d, f, e)))
            neighbors.append(((a, e, c), (d, b, f)))
        else:
            neighbors.append(((a, b, c), (d, f, e)))
            neighbors.append(((a, b, f), (d, e, c)))

        return neighbors