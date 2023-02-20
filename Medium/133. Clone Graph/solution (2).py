# 133. Clone Graph

# Runtime: 32 ms, faster than 94.86% of Python3 online submissions for Clone Graph.

# Memory Usage: 14.7 MB, less than 28.59% of Python3 online submissions for Clone Graph.


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    # Breadth-First Search
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        visited = {}
        que = deque([node])
        visited[node] = Node(node.val, [])
        while que:
            next = que.popleft()
            for neighbor in next.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    que.append(neighbor)
                visited[next].neighbors.append(visited[neighbor])

        return visited[node]