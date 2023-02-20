# 116. Populating Next Right Pointers in Each Node

# Runtime: 74 ms, faster than 28.87% of Python3 online submissions for Populating Next Right Pointers in Each Node.

# Memory Usage: 15.7 MB, less than 31.65% of Python3 online submissions for Populating Next Right Pointers in Each Node.


"""
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None) -> Node:
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

        most_left = root
        while most_left.left:
            head = most_left
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            most_left = most_left.left
        return root