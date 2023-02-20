# 234. Palindrome Linked List

# Runtime: 776 ms, faster than 78.40% of Python3 online submissions for Palindrome Linked List.

# Memory Usage: 39.4 MB, less than 65.28% of Python3 online submissions for Palindrome Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Reverse Second Half In-place
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        def end_of_first_half(head: ListNode) -> ListNode:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow.next if fast else slow

        def reverse_list(head: ListNode) -> ListNode:
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
            return prev

        left = head
        right = reverse_list(end_of_first_half(head))
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True