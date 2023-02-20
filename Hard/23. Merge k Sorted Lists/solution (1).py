# 23. Merge k Sorted Lists

# Time Limit Exceeded


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    # Compare one by one
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None

        nodes = [None] * len(lists)
        end = [False] * len(lists)
        for i in range(len(lists)):
            if lists[i]:
                nodes[i] = lists[i]
            else:
                end[i] = True

        head = ListNode()
        curr = head
        while not all(end):
            curr_min = (ListNode(math.inf), None)
            # Compare the first node of each list and find the smallest one.
            for i in range(len(nodes)):
                if not end[i]:
                    if nodes[i].val < curr_min[0].val:
                        curr_min = (nodes[i], i)

            node, idx = curr_min
            curr.next = node
            curr = node

            nodes[idx] = nodes[idx].next
            if not nodes[idx]:
                end[idx] = True
        return head.next