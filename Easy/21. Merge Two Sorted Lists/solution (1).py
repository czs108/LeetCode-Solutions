# 21. Merge Two Sorted Lists

# Runtime: 36 ms, faster than 64.43% of Python3 online submissions for Merge Two Sorted Lists.

# Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.


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

        result = None
        if l1.val < l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
        return result