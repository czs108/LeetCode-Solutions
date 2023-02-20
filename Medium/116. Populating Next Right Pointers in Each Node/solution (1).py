# 116. Populating Next Right Pointers in Each Node

# Runtime: 56 ms, faster than 93.66% of Python3 online submissions for Populating Next Right Pointers in Each Node.

# Memory Usage: 15.6 MB, less than 70.06% of Python3 online submissions for Populating Next Right Pointers in Each Node.


"""
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None) -> Node:
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