# 226. Invert Binary Tree

# Runtime: 41 ms, faster than 20.91% of Python3 online submissions for Invert Binary Tree.

# Memory Usage: 14.2 MB, less than 74.11% of Python3 online submissions for Invert Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root