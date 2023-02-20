# 1971. Find if Path Exists in Graph


from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            a, b = edge
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n

        def dfs(v: int) -> bool:
            visited[v] = True
            if v == end:
                return True

            for next in adj[v]:
                if not visited[next]:
                    if dfs(next):
                        return True
            return False

        return dfs(start)