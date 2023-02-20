# 547. Number of Provinces

# Runtime: 513 ms, faster than 5.02% of Python3 online submissions for Number of Provinces.

# Memory Usage: 14.6 MB, less than 88.35% of Python3 online submissions for Number of Provinces.


class Solution:
    # Union-Find
    def __init__(self) -> None:
        self._parents: list[int] = None

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        self._parents = [-1] * len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] and i != j:
                    self._union(i, j)

        count = 0
        for i in range(len(self._parents)):
            if self._parents[i] < 0:
                count += 1
        return count

    def _root(self, i: int) -> int:
        if self._parents[i] < 0:
            return i
        else:
            return self._root(self._parents[i])

    def _union(self, i: int, j: int) -> None:
        root_i, root_j = self._root(i), self._root(j)
        if root_i != root_j:
            self._parents[root_i] = root_j