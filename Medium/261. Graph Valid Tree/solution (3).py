# 261. Graph Valid Tree

# Runtime: 132 ms, faster than 19.13% of Python3 online submissions for Graph Valid Tree.

# Memory Usage: 15.6 MB, less than 46.79% of Python3 online submissions for Graph Valid Tree.


class Solution:
    # Iterative Depth-First Search
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        seen = set()

        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            seen.add(node)
            for next in adjacency[node]:
                if next == parent:
                    continue
                elif next in seen:
                    return False
                else:
                    stack.append((next, node))
        return len(seen) == n