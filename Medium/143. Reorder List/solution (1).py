# 143. Reorder List

# Runtime: 92 ms, faster than 76.41% of Python3 online submissions for Reorder List.

# Memory Usage: 23.3 MB, less than 78.97% of Python3 online submissions for Reorder List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Reverse the Second Part of the List and Merge Two Sorted Lists
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find the middle of linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part of the list.
        curr, prev = slow, None
        while curr:
            next = curr.next
            curr.next = prev
            curr, prev = next, curr

        # Merge two sorted linked lists.
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp