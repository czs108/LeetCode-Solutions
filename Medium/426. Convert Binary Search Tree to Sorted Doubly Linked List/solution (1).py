# 426. Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    # Recursion
    def treeToDoublyList(self, root: Node) -> Node:
        first, prev = None, None

        def dfs(node: Node) -> None:
            nonlocal first, prev
            if not node:
                return

            dfs(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                first = node
            prev = node
            dfs(node.right)

        if not root:
            return None
        else:
            dfs(root)
            first.left = prev
            prev.right = first
            return first