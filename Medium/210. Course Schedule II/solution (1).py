# 210. Course Schedule II

# Runtime: 104 ms, faster than 44.18% of Python3 online submissions for Course Schedule II.

# Memory Usage: 17.2 MB, less than 32.63% of Python3 online submissions for Course Schedule II.


from collections import defaultdict
from enum import Enum, auto


class State(Enum):
    NotProcessed = auto()
    Processing = auto()
    Processed = auto()


class Solution:
    # Depth First Search
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjs = defaultdict(list)
        for dest, src in prerequisites:
            adjs[src].append(dest)

        topological_sorted_order = []
        possible = True
        states = {i: State.NotProcessed for i in range(numCourses)}

        def dfs(i: int) -> None:
            nonlocal possible
            if not possible:
                return

            states[i] = State.Processing
            if i in adjs:
                for next in adjs[i]:
                    if states[next] == State.NotProcessed:
                        dfs(next)
                    elif states[next] == State.Processing:
                        possible = False
            states[i] = State.Processed
            topological_sorted_order.append(i)

        for i in range(numCourses):
            if states[i] == State.NotProcessed:
                dfs(i)
        return topological_sorted_order[::-1] if possible else []