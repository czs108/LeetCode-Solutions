# 707. Design Linked List

# Runtime: 256 ms, faster than 67.19% of Python3 online submissions for Design Linked List.

# Memory Usage: 15.2 MB, less than 36.23% of Python3 online submissions for Design Linked List.


class ListNode:
    # Singly Linked List
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: ListNode = None


class MyLinkedList:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self._head: ListNode = ListNode(0)
        self._size: int = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get(index + 1)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self._size:
            return
        else:
            prev = self._get(index)
            node = ListNode(val)
            node.next = prev.next
            prev.next = node
            self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self._size:
            return
        else:
            prev = self._get(index)
            prev.next = prev.next.next
            self._size -= 1

    def _get(self, index: int) -> ListNode:
        if 0 <= index and index <= self._size:
            node = self._head
            for _ in range(index):
                node = node.next
            return node
        else:
            return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)