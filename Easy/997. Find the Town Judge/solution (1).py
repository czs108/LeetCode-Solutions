# 997. Find the Town Judge

# Runtime: 917 ms, faster than 26.97% of Python3 online submissions for Find the Town Judge.

# Memory Usage: 19 MB, less than 61.93% of Python3 online submissions for Find the Town Judge.


class Solution:
    # Directed Edge
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1