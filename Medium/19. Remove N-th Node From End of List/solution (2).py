# 19. Remove N-th Node From End of List

# Runtime: 36 ms, faster than 53.79% of Python3 online submissions for Remove N-th Node From End of List.

# Memory Usage: 14.2 MB, less than 47.85% of Python3 online submissions for Remove N-th Node From End of List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two Pass
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def length(head: ListNode) -> int:
            n = 0
            while head:
                head = head.next
                n += 1
            return n

        dummy = ListNode(0, head)
        p = dummy
        for _ in range(length(head) - n):
            p = p.next
        p.next = p.next.next
        return dummy.next