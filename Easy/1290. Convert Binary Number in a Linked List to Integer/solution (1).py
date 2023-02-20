# 1290. Convert Binary Number in a Linked List to Integer

# Runtime: 32 ms, faster than 67.63% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Memory Usage: 14.2 MB, less than 69.19% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Binary Representation
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num