# 142. Linked List Cycle II

# Runtime: 57 ms, faster than 28.23% of Python3 online submissions for Linked List Cycle II.

# Memory Usage: 17.2 MB, less than 54.91% of Python3 online submissions for Linked List Cycle II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # Two Pointers
    def getIntersect(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        # A fast pointer will either loop around a cycle and meet the slow pointer or reach the `null` at the end of a non-cyclic list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some node.
        # Otherwise, there is no cycle, so we cannot find an entrance to a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at the same speed:
        # one from the front of the list, and the other from the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1