# 234. Palindrome Linked List

# Runtime: 1024 ms, faster than 16.14% of Python3 online submissions for Palindrome Linked List.

# Memory Usage: 47.1 MB, less than 51.73% of Python3 online submissions for Palindrome Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]