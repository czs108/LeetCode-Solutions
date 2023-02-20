# 203. Remove Linked List Elements

# Runtime: 72 ms, faster than 53.32% of Python3 online submissions for Remove Linked List Elements.

# Memory Usage: 17.3 MB, less than 26.09% of Python3 online submissions for Remove Linked List Elements.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Sentinel Node
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return dummy.next