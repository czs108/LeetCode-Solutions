# 234. Palindrome Linked List

# Runtime: 1365 ms, faster than 5.07% of Python3 online submissions for Palindrome Linked List.

# Memory Usage: 116.3 MB, less than 5.19% of Python3 online submissions for Palindrome Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Advanced Recursive
    def __init__(self) -> None:
        self._left: ListNode = None

    def isPalindrome(self, head: ListNode) -> bool:
        self._left = head
        return self._recursive(head)

    def _recursive(self, right: ListNode) -> bool:
        if right is None:
            return True
        elif not self._recursive(right.next):
            return False
        else:
            same = self._left.val == right.val
            self._left = self._left.next
            return same