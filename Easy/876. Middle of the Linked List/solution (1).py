# 876. Middle of the Linked List

# Runtime: 32 ms, faster than 62.48% of Python3 online submissions for Middle of the Linked List.

# Memory Usage: 14.2 MB, less than 43.08% of Python3 online submissions for Middle of the Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Output to Array
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]