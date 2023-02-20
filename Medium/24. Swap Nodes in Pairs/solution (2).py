# 24. Swap Nodes in Pairs

# Runtime: 32 ms, faster than 65.71% of Python3 online submissions for Swap Nodes in Pairs.

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
            first, second = head, head.next
            # Cannot swap the following two lines, otherwise there will be a circle in the list.
            first.next = self.swapPairs(head.next.next)
            second.next = first
            return second