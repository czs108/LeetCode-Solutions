# 261. Graph Valid Tree

# Runtime: 111 ms, faster than 26.45% of Python3 online submissions for Graph Valid Tree.

# Memory Usage: 15.9 MB, less than 35.64% of Python3 online submissions for Graph Valid Tree.


class Solution:
    # Depth-First Search | Recursion
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        seen = set()

        def dfs(node: int, parent: int) -> bool:
            seen.add(node)
            for next in adjacency[node]:
                if next == parent:
                    continue
                elif next in seen:
                    return False
                else:
                    if not dfs(next, node):
                        return False
            return True

        return dfs(0, -1) and len(seen) == n