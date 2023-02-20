# 19. Remove N-th Node From End of List

# Runtime: 44 ms, faster than 18.17% of Python3 online submissions for Remove N-th Node From End of List.

# Memory Usage: 14.3 MB, less than 47.85% of Python3 online submissions for Remove N-th Node From End of List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two Pointers
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next

        # Now both pointers are exactly separated by `n` nodes apart.
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next