# 92. Reverse Linked List II

# Runtime: 64 ms, faster than 5.80% of Python3 online submissions for Reverse Linked List II.

# Memory Usage: 14.7 MB, less than 5.82% of Python3 online submissions for Reverse Linked List II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Reverse first N nodes
    def __init__(self) -> None:
        self._successor: ListNode = None

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if right - left == 0:
            return head
        elif left == 1:
            return self._reverseN(head, right - left + 1)
        else:
            head.next = self.reverseBetween(head.next, left - 1, right - 1)
            return head

    def _reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self._successor = head.next
            return head
        else:
            last = self._reverseN(head.next, n - 1)
            head.next.next = head
            head.next = self._successor
            return last