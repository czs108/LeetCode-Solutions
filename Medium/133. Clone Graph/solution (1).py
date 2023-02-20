# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Depth-First Search
    def __init__(self) -> None:
        # Save the visited node and it's respective clone.
        self._visited: dict[Node, Node] = {}

    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        elif node in self._visited:
            return self._visited[node]

        cloned = Node(node.val, [])
        self._visited[node] = cloned

        if node.neighbors:
            cloned.neighbors = [self.cloneGraph(next) for next in node.neighbors]

        return cloned