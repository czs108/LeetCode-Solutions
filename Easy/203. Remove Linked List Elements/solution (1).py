# 203. Remove Linked List Elements

# Runtime: 72 ms, faster than 53.32% of Python3 online submissions for Remove Linked List Elements.

# Memory Usage: 25.7 MB, less than 5.65% of Python3 online submissions for Remove Linked List Elements.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        elif head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head