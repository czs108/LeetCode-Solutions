# 21. Merge Two Sorted Lists

# Runtime: 36 ms, faster than 64.43% of Python3 online submissions for Merge Two Sorted Lists.

# Memory Usage: 13.6 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        root = ListNode(None)
        curr = root
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if not l1:
            curr.next = l2
        elif not l2:
            curr.next = l1
        return root.next