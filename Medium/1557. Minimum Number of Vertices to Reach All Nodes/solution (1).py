# 1557. Minimum Number of Vertices to Reach All Nodes

# Runtime: 1176 ms, faster than 75.66% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.

# Memory Usage: 52.7 MB, less than 78.92% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indegrees = [0] * n
        for _, dest in edges:
            indegrees[dest] += 1

        ans = []
        for id, degree in enumerate(indegrees):
            # If a node's in-degree is 0, it cannot be reached from others.
            if degree == 0:
                ans.append(id)
        return ans