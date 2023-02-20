# 323. Number of Connected Components in an Undirected Graph

# Runtime: 316 ms, faster than 6.20% of Python3 online submissions for Number of Connected Components in an Undirected Graph.

# Memory Usage: 15.4 MB, less than 90.86% of Python3 online submissions for Number of Connected Components in an Undirected Graph.


class Solution:
    # Disjoint Set Union
    def __init__(self) -> None:
        self._roots: list[int] = None

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        self._roots = [-1] * n
        for a, b in edges:
            self._union(a, b)

        count = 0
        for i in range(n):
            if self._roots[i] < 0:
                count += 1
        return count

    def _find(self, node: int) -> int:
        while self._roots[node] >= 0:
            node = self._roots[node]
        return node

    def _union(self, x: int, y: int) -> None:
        root_x, root_y = self._find(x), self._find(y)
        if root_x != root_y:
            self._roots[root_x] = root_y