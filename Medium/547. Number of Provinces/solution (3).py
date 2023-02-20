# 547. Number of Provinces

# Runtime: 446 ms, faster than 5.74% of Python3 online submissions for Number of Provinces.

# Memory Usage: 15 MB, less than 23.50% of Python3 online submissions for Number of Provinces.


class Solution:
    # Depth First Search
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = [False] * len(isConnected)

        def dfs(start: int) -> None:
            for i in range(len(isConnected)):
                if isConnected[i][start] and not visited[i]:
                    visited[i] = True
                    dfs(i)

        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count += 1
        return count