# 92. Reverse Linked List II

# Runtime: 59 ms, faster than 5.80% of Python3 online submissions for Reverse Linked List II.

# Memory Usage: 14.7 MB, less than 5.82% of Python3 online submissions for Reverse Linked List II.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    def __init__(self) -> None:
        self._left_node: ListNode = None
        self._stop: bool = False

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return None
        self._left_node = head
        self._recurse_reverse(head, left, right)
        return head

    def _recurse_reverse(self, right_node: ListNode, left: int, right: int) -> None:
        # Base case. Don't proceed any further.
        if right == 1:
            return

        # Keep moving the right pointer one step forward.
        right_node = right_node.next

        # Keep moving left pointer to the right until we reach the proper node from where the reversal is to start.
        if left > 1:
            self._left_node = self._left_node.next

        self._recurse_reverse(right_node, left - 1, right - 1)

        # In case both the pointers cross each other or become equal, we stop i.e. don't swap data any further.
        if self._left_node == right_node or right_node.next == self._left_node:
            self._stop = True

        if not self._stop:
            right_node.val, self._left_node.val = self._left_node.val, right_node.val
            # Move left one step to the right. The right pointer moves one step back via backtracking.
            self._left_node = self._left_node.next