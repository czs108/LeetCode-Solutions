# 173. Binary Search Tree Iterator

# Runtime: 72 ms, faster than 85.30% of Python3 online submissions for Binary Search Tree Iterator.

# Memory Usage: 20.8 MB, less than 18.77% of Python3 online submissions for Binary Search Tree Iterator.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Controlled Recursion
    def __init__(self, root: TreeNode) -> None:
        self._stack: list[TreeNode] = []
        self._leftmost_inorder(root)

    def next(self) -> int:
        smallest = self._stack.pop()
        if smallest.right:
            self._leftmost_inorder(smallest.right)
        return smallest.val

    def hasNext(self) -> bool:
        return len(self._stack) > 0

    def _leftmost_inorder(self, root: TreeNode) -> None:
        while root:
            self._stack.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()