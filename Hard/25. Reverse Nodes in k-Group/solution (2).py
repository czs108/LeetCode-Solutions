# 25. Reverse Nodes in k-Group

# Runtime: 48 ms, faster than 76.25% of Python3 online submissions for Reverse Nodes in k-Group.

# Memory Usage: 15.2 MB, less than 76.87% of Python3 online submissions for Reverse Nodes in k-Group.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head

        def reverse_between(left: ListNode, right: ListNode) -> ListNode:
            curr, prev = left, None
            while curr != right:
                next = curr.next
                curr.next = prev
                curr, prev = next, curr
            return prev

        left, right = head, head
        for _ in range(k):
            if right:
                right = right.next
            else:
                return head

        new_head = reverse_between(left, right)
        head.next = self.reverseKGroup(right, k)
        return new_head