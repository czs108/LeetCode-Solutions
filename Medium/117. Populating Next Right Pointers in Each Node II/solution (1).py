# 117. Populating Next Right Pointers in Each Node II

# Runtime: 44 ms, faster than 92.87% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

# Memory Usage: 15.5 MB, less than 8.13% of Python3 online submissions for Populating Next Right Pointers in Each Node II.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    # Level Order Traversal
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if i < size - 1:
                    node.next = que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root