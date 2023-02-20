# 399. Evaluate Division

# Runtime: 44 ms, faster than 17.58% of Python3 online submissions for Evaluate Division.

# Memory Usage: 14.1 MB, less than 92.49% of Python3 online submissions for Evaluate Division.


from collections import defaultdict

class Solution:
    # Path Search in Graph
    def __init__(self) -> None:
        self._graph: dict = None

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        self._build(equations, values)

        ans = []
        for dividend, divisor in queries:
            if dividend not in self._graph or divisor not in self._graph:
                ret = -1.0
            elif dividend == divisor:
                ret = 1.0
            else:
                ret = self._calc(dividend, divisor)
            ans.append(ret)
        return ans

    def _build(self, equations: list[list[str]], values: list[float]) -> None:
        self._graph = defaultdict(defaultdict)
        for (dividend, divisor), value in zip(equations, values):
            self._graph[dividend][divisor] = value
            self._graph[divisor][dividend] = 1 / value

    def _calc(self, dividend: str, divisor: str) -> float:
        visited = set()

        def backtrack(curr: str, target: str, acc_product: float) -> float:
            visited.add(curr)
            ret = -1.0
            neighbors = self._graph[curr]
            if target in neighbors:
                ret = acc_product * neighbors[target]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor not in visited:
                        ret = backtrack(neighbor, target, acc_product * val)
                        if ret != -1.0:
                            break
            visited.remove(curr)
            return ret

        return backtrack(dividend, divisor, 1)