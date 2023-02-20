# 61. Rotate List

# Runtime: 36 ms, faster than 66.43% of Python3 online submissions for Rotate List.

# Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Rotate List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        def get_tail_length(head: ListNode) -> tuple[int, ListNode]:
                if not head:
                    return 0, None
                n = 1
                while head.next:
                    head = head.next
                    n += 1
                return n, head

        n, tail = get_tail_length(head)
        if n == 0:
            return head
        k %= n
        if k == 0:
            return head

        before_new_head = head
        for _ in range(n - k - 1):
            before_new_head = before_new_head.next
        new_head = before_new_head.next
        before_new_head.next = None
        tail.next = head
        return new_head