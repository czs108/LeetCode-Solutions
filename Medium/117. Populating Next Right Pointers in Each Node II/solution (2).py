# 117. Populating Next Right Pointers in Each Node II

# Runtime: 70 ms, faster than 26.90% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

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

class Solution:
    # Using previously established next pointers
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        def process_child(child: Node, prev: Node, leftmost: Node) -> tuple[Node, Node]:
            if child:
                if prev:
                    prev.next = child
                else:
                    # Update `leftmost` for the next level.
                    leftmost = child
                prev = child
            return prev, leftmost

        leftmost = root
        while leftmost:
            # `prev` tracks the latest node on the next level.
            # `curr` tracks the latest node on the current level.
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = process_child(curr.left, prev, leftmost)
                prev, leftmost = process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root