# 206. Reverse Linked List

# Runtime: 36 ms, faster than 68.82% of Python3 online submissions for Reverse Linked List.

# Memory Usage: 15.6 MB, less than 46.12% of Python3 online submissions for Reverse Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            curr, prev = next, curr
        return prev