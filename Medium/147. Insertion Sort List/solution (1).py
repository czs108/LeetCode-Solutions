# 147. Insertion Sort List

# Runtime: 1972 ms, faster than 31.13% of Python3 online submissions for Insertion Sort List.

# Memory Usage: 16.2 MB, less than 98.51% of Python3 online submissions for Insertion Sort List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
class Solution:
    # Insertion Sort
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curr = head
        while curr:
            # Find the position to insert the current node.
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next = curr.next

            # Insert the current node to the new list.
            curr.next = prev.next
            prev.next = curr

            curr = next
        return dummy.next