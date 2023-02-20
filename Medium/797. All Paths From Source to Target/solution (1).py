# 797. All Paths From Source to Target

# Runtime: 96 ms, faster than 90.54% of Python3 online submissions for All Paths From Source to Target.

# Memory Usage: 15.5 MB, less than 75.90% of Python3 online submissions for All Paths From Source to Target.


class Solution:
    # Backtracking
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []

        def backtrack(start: int, path: list[int]) -> None:
            if start == target:
                res.append(list(path))
            else:
                for next in graph[start]:
                    path.append(next)
                    backtrack(next, path)
                    path.pop()

        backtrack(0, [0])
        return res