# 92. Reverse Linked List II

# Runtime: 41 ms, faster than 16.72% of Python3 online submissions for Reverse Linked List II.

# Memory Usage: 14.4 MB, less than 70.72% of Python3 online submissions for Reverse Linked List II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative Link Reversal
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return None

        # Move the two pointers until they reach the proper starting point.
        curr, prev = head, None
        while left > 1:
            curr, prev = curr.next, curr
            left -= 1
            right -= 1

        # The two pointers that will fix the final connections.
        tail, con = curr, prev

        # Iteratively reverse the nodes.
        while right > 0:
            next = curr.next
            curr.next = prev
            curr, prev = next, curr
            right -= 1

        if con is not None:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head