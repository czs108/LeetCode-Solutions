# 142. Linked List Cycle II

# Runtime: 39 ms, faster than 98.77% of Python3 online submissions for Linked List Cycle II.

# Memory Usage: 17.7 MB, less than 9.80% of Python3 online submissions for Linked List Cycle II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # Hash Table
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None