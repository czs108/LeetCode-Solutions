# 99. Recover Binary Search Tree

# Runtime: 64 ms, faster than 95.92% of Python3 online submissions for Recover Binary Search Tree.

# Memory Usage: 14.6 MB, less than 57.01% of Python3 online submissions for Recover Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Inorder Traversal
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = prev = None

        def find_swapped(root: TreeNode) -> None:
            nonlocal x, y, prev
            if root is None:
                return

            find_swapped(root.left)
            if prev and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
                else:
                    return
            prev = root
            find_swapped(root.right)

        find_swapped(root)
        x.val, y.val = y.val, x.val