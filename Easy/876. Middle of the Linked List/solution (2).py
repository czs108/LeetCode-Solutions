# 876. Middle of the Linked List

# Runtime: 70 ms, faster than 5.33% of Python3 online submissions for Middle of the Linked List.

# Memory Usage: 14.1 MB, less than 72.28% of Python3 online submissions for Middle of the Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Fast and Slow Pointer
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow