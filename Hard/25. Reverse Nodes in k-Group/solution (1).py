# 25. Reverse Nodes in k-Group

# Runtime: 52 ms, faster than 49.86% of Python3 online submissions for Reverse Nodes in k-Group.

# Memory Usage: 15 MB, less than 99.22% of Python3 online submissions for Reverse Nodes in k-Group.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head

        def reverseN(head: ListNode, n: int) -> ListNode:
            curr, prev = head, None
            for _ in range(n):
                next = curr.next
                curr.next = prev
                curr, prev = next, curr
            return prev

        final_head, prev_group_tail = None, None
        curr = head
        while curr:
            i = 0
            while i != k and curr:
                curr = curr.next
                i += 1
            if i == k:
                new_head = reverseN(head, k)
                if final_head is None:
                    final_head = new_head
                if prev_group_tail:
                    prev_group_tail.next = new_head
                prev_group_tail = head
                head = curr

        if prev_group_tail:
            prev_group_tail.next = head
        return final_head if final_head else head