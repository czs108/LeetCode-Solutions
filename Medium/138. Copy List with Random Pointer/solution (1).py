# 138. Copy List with Random Pointer


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self) -> None:
        # Old nodes are keys and new nodes are its values.
        self._visited: dict[Node, Node] = {}

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        elif head in self._visited:
            # If we have already processed the current node,
            # then we simply return the cloned version of it.
            return self._visited[head]
        else:
            node = Node(head.val, None, None)
            self._visited[head] = node

            # Recursively copy the remaining linked list
            # starting once from the next pointer and then from the random pointer.
            node.next = self.copyRandomList(head.next)
            node.random = self.copyRandomList(head.random)
            return node