# 261. Graph Valid Tree

# Runtime: 111 ms, faster than 26.45% of Python3 online submissions for Graph Valid Tree.

# Memory Usage: 15.5 MB, less than 69.44% of Python3 online submissions for Graph Valid Tree.


class Solution:
    # Iterative Depth-First Search
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency = [[] for _ in range(n)]
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        parents = {0: -1}

        stack = [0]
        while stack:
            node = stack.pop()
            for next in adjacency[node]:
                if next == parents[node]:
                    continue
                elif next in parents:
                    return False
                else:
                    parents[next] = node
                    stack.append(next)
        return len(parents) == n