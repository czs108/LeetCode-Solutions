# 23. Merge k Sorted Lists

# Runtime: 240 ms, faster than 14.75% of Python3 online submissions for Merge k Sorted Lists.

# Memory Usage: 18.5 MB, less than 19.11% of Python3 online submissions for Merge k Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class NodeWrapper:
    def __init__(self, node: ListNode) -> None:
        self.node: ListNode = node

    def __lt__(self, other: NodeWrapper) -> bool:
        return self.node.val < other.node.val


class Solution:
    # Compare one by one | Priority Queue
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None

        que = PriorityQueue()
        for head in lists:
            if head:
                que.put(NodeWrapper(head))

        head = ListNode()
        curr = head
        while not que.empty():
            node = que.get().node
            curr.next = node
            curr = node
            if curr.next:
                que.put(NodeWrapper(curr.next))
        return head.next