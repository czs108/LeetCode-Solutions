# 98. Validate Binary Search Tree

# Runtime: 40 ms, faster than 88.33% of Python3 online submissions for Validate Binary Search Tree.

# Memory Usage: 16.9 MB, less than 28.81% of Python3 online submissions for Validate Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    # Recursive Inorder Traversal
    def isValidBST(self, root: TreeNode) -> bool:
        prev = -math.inf

        def inorder(node: TreeNode) -> bool:
            nonlocal prev
            if node is None:
                return True
            elif not inorder(node.left):
                return False
            elif node.val <= prev:
                return False
            else:
                prev = node.val
                return inorder(node.right)

        return inorder(root)