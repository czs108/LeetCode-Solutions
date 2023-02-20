# 99. Recover Binary Search Tree

# Runtime: 72 ms, faster than 73.88% of Python3 online submissions for Recover Binary Search Tree.

# Memory Usage: 14.7 MB, less than 24.54% of Python3 online submissions for Recover Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative Inorder Traversal
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
                else:
                    break
            prev = root
            root = root.right

        x.val, y.val = y.val, x.val