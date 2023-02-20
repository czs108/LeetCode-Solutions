# 261. Graph Valid Tree

# Runtime: 170 ms, faster than 8.95% of Python3 online submissions for Graph Valid Tree.

# Memory Usage: 15.8 MB, less than 36.75% of Python3 online submissions for Graph Valid Tree.


class Solution:
    # Depth-First Search | Recursion
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        parents = {0: -1}

        def dfs(node: int) -> bool:
            for next in adjacency[node]:
                if next == parents[node]:
                    continue
                elif next in parents:
                    return False
                else:
                    parents[next] = node
                    if not dfs(next):
                        return False
            return True

        return dfs(0) and len(parents) == n