# 173. Binary Search Tree Iterator

# Runtime: 80 ms, faster than 53.78% of Python3 online submissions for Binary Search Tree Iterator.

# Memory Usage: 20.3 MB, less than 72.21% of Python3 online submissions for Binary Search Tree Iterator.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Flattening the BST
    def __init__(self, root: TreeNode) -> None:
        self._vals: list[int] = []
        self._idx: int = -1

        def inorder(root: TreeNode) -> None:
            if root:
                inorder(root.left)
                self._vals.append(root.val)
                inorder(root.right)

        inorder(root)

    def next(self) -> int:
        self._idx += 1
        return self._vals[self._idx]

    def hasNext(self) -> bool:
        return self._idx + 1 < len(self._vals)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()