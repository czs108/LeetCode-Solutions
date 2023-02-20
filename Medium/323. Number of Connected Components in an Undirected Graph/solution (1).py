# 323. Number of Connected Components in an Undirected Graph


class Solution:
    # Depth-First Search
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        count = 0
        visited = [False] * n
        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        def dfs(node: int) -> None:
            visited[node] = True
            for next in adjacency[node]:
                if not visited[next]:
                    dfs(next)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count