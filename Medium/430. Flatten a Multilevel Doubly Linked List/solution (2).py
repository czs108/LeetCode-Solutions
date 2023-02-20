# 430. Flatten a Multilevel Doubly Linked List


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    # DFS by Iteration
    def flatten(self, head: Node) -> Node:
        if not head:
            return

        pseudo_head = Node(0, None, head, None)
        prev = pseudo_head

        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # Don't forget to remove all child pointers.
                curr.child = None

            prev = curr

        # Detach the pseudo head node from the result.
        pseudo_head.next.prev = None
        return pseudo_head.next