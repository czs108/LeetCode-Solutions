# 617. Merge Two Binary Trees

# Runtime: 84 ms, faster than 79.23% of Python3 online submissions for Merge Two Binary Trees.

# Memory Usage: 15.4 MB, less than 76.43% of Python3 online submissions for Merge Two Binary Trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            new_root = TreeNode(root1.val + root2.val)
            new_root.right = self.mergeTrees(root1.right, root2.right)
            new_root.left = self.mergeTrees(root1.left, root2.left)
            return new_root