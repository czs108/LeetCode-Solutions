# 24. Swap Nodes in Pairs

# Runtime: 24 ms, faster than 96.60% of Python3 online submissions for Swap Nodes in Pairs.

# Memory Usage: 14 MB, less than 92.32% of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive Approach
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)
            return head