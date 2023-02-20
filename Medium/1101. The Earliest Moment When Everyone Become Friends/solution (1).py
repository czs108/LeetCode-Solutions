# 1101. The Earliest Moment When Everyone Become Friends


class Solution:
    # Union Find
    def __init__(self) -> None:
        self._roots: list[int] = None
        self._set_count: int = 0

    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        # Reorder timestamps.
        logs.sort(key=lambda x: x[0])

        self._roots = [-1] * n
        self._set_count = n
        for time, x, y in logs:
            self._union(x, y)
            if self._set_count == 1:
                return time
        return -1

    def _find(self, n: int) -> int:
        while self._roots[n] >= 0:
            n = self._roots[n]
        return n

    def _union(self, x: int, y: int) -> None:
        root_x, root_y = self._find(x), self._find(y)
        if root_x != root_y:
            self._set_count -= 1
            self._roots[root_x] = root_y


Solution().earliestAcq([[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], 4)

