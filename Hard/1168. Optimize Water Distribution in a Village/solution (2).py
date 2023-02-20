# 1168. Optimize Water Distribution in a Village

# Runtime: 915 ms, faster than 5.05% of Python3 online submissions for Optimize Water Distribution in a Village.

# Memory Usage: 19.8 MB, less than 83.84% of Python3 online submissions for Optimize Water Distribution in a Village.


from functools import total_ordering

class Solution:
    # Kruskal's Algorithm with Union-Find | Greedy
    #
    # We iterate through all the edges ordered by their costs. For each edge, we decide whether to add it to the final minimum spanning tree.
    # The decision is based on whether this new addition will help to connect more dots (i.e. vertices).
    def __init__(self) -> None:
        self._roots: list[int] = None
        self._ranks: list[int] = None

    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        ordered_edges = []

        # Add a virtual vertex indexed with 0.
        for idx, cost in enumerate(wells):
            ordered_edges.append((cost, 0, idx + 1))

        # Add the existing edges.
        for a, b, cost in pipes:
            ordered_edges.append((cost, a, b))

        # Sort the entire edges by their costs.
        ordered_edges.sort(key=lambda x: x[0])

        self._roots = [-1] * (n + 1)
        self._ranks = [-1] * (n + 1)
        total_cost = 0
        for cost, a, b in ordered_edges:
            # Determine if we should add the new edge.
            if self._union(a, b):
                total_cost += cost
        return total_cost


    def _find(self, x: int) -> None:
        if self._roots[x] < 0:
            return x
        else:
            self._roots[x] = self._find(self._roots[x])
            return self._roots[x]

    def _union(self, x: int, y: int) -> None:
        root_x, root_y = self._find(x), self._find(y)
        if root_x != root_y:
            if self._ranks[root_x] < self._ranks[root_y]:
                self._roots[root_x] = root_y
            elif self._ranks[root_x] > self._ranks[root_y]:
                self._roots[root_y] = root_x
            else:
                self._roots[root_x] = root_y
                self._ranks[root_x] += 1
            return True
        else:
            return False