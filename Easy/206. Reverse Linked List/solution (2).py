# 206. Reverse Linked List

# Runtime: 67 ms, faster than 5.12% of Python3 online submissions for Reverse Linked List.

# Memory Usage: 18.9 MB, less than 16.69% of Python3 online submissions for Reverse Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            last = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return last