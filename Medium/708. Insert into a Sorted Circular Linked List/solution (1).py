# 708. Insert into a Sorted Circular Linked List

# Runtime: 36 ms, faster than 83.59% of Python3 online submissions for Insert into a Sorted Circular Linked List.

# Memory Usage: 15.1 MB, less than 41.64% of Python3 online submissions for Insert into a Sorted Circular Linked List.


'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    #  Two Pointers
    def insert(self, head: Node, insertVal: int) -> Node:
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev, curr = head, head.next
        to_insert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                to_insert = True
            elif prev.val > curr.val:
                # `prev` is the tail.
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break

        # Did not insert the node in the loop.
        prev.next = Node(insertVal, curr)
        return head