# 24. Swap Nodes in Pairs

# Runtime: 28 ms, faster than 87.12% of Python3 online submissions for Swap Nodes in Pairs.

# Memory Usage: 14.2 MB, less than 76.36% of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative Approach
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head = None
        prev_tail = None
        while head and head.next:
            first, second = head, head.next
            first.next = second.next
            second.next = first
            if new_head is None:
                new_head = second
            if prev_tail:
                prev_tail.next = second
            prev_tail = first
            head = first.next
        return new_head