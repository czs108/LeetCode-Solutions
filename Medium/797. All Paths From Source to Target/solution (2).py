# 797. All Paths From Source to Target

# Runtime: 82 ms, faster than 99.68% of Python3 online submissions for All Paths From Source to Target.

# Memory Usage: 17.4 MB, less than 5.14% of Python3 online submissions for All Paths From Source to Target.


from functools import lru_cache

class Solution:
    # Top-Down Dynamic Programming
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def paths_to_target(i: int) -> list[list[int]]:
            if i == target:
                return [[i]]

            res = []
            for next in graph[i]:
                for path in paths_to_target(next):
                    res.append([i] + path)
            return res

        return paths_to_target(0)