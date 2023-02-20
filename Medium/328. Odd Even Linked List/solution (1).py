# 328. Odd Even Linked List

# Runtime: 36 ms, faster than 95.17% of Python3 online submissions for Odd Even Linked List.

# Memory Usage: 16.5 MB, less than 14.96% of Python3 online submissions for Odd Even Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two Pointers
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd_dummy, even_dummy = ListNode(), ListNode()
        prev_odd, prev_even = odd_dummy, even_dummy

        i = 0
        node = head
        while node:
            if i % 2 == 0:
                prev_odd.next, prev_odd = node, node
            else:
                prev_even.next, prev_even = node, node
            i += 1
            node = node.next
        prev_even.next = None
        prev_odd.next = even_dummy.next
        return odd_dummy.next