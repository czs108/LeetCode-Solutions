# 23. Merge k Sorted Lists

# Runtime: 148 ms, faster than 33.74% of Python3 online submissions for Merge k Sorted Lists.

# Memory Usage: 17.8 MB, less than 82.01% of Python3 online submissions for Merge k Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Merge with Divide And Conquer
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
            head = ListNode()
            curr = head
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            if list1:
                curr.next = list1
            else:
                curr.next = list2
            return head.next

        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists) - 1, 2):
                new_lists.append(merge_two_lists(lists[i], lists[i + 1]))
            if len(lists) % 2 != 0:
                new_lists.append(lists[-1])
            lists = new_lists
        return lists[0] if lists else None