# 430. Flatten a Multilevel Doubly Linked List

# Runtime: 36 ms, faster than 65.60% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

# Memory Usage: 15.6 MB, less than 6.30% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.


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
    # DFS by Recursion
    def flatten(self, head: Node) -> Node:
        if not head:
            return head

        def flatten_dfs(prev: Node, curr: Node) -> Node:
            """
            Return the tail of the flatten list.
            """
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            # The `curr.next` would be tempered in the recursive function.
            tmp_next = curr.next
            tail = flatten_dfs(curr, curr.child)
            curr.child = None
            return flatten_dfs(tail, tmp_next)

        # Pseudo head to ensure the `prev` pointer is never `null`.
        pseudo_head = Node(None, None, head, None)
        flatten_dfs(pseudo_head, head)

        # Detach the pseudo head from the real head
        pseudo_head.next.prev = None
        return pseudo_head.next