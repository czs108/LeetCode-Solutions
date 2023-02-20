# 547. Number of Provinces

# Runtime: 312 ms, faster than 23.42% of Python3 online submissions for Number of Provinces.

# Memory Usage: 14.8 MB, less than 35.27% of Python3 online submissions for Number of Provinces.


class Solution:
    # Breadth First Search
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if visited[i]:
                continue
            que = [i]
            while que:
                curr = que.pop()
                visited[curr] = True
                for j in range(len(isConnected)):
                    if isConnected[curr][j] and not visited[j]:
                        que.append(j)
            count += 1
        return count