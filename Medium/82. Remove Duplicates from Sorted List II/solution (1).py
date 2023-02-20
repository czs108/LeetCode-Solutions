# 82. Remove Duplicates from Sorted List II

# Runtime: 40 ms, faster than 77.76% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Memory Usage: 14.4 MB, less than 26.40% of Python3 online submissions for Remove Duplicates from Sorted List II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, node = dummy, head
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = prev.next
            node = node.next
        return dummy.next