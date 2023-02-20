# 98. Validate Binary Search Tree

# Runtime: 40 ms, faster than 88.33% of Python3 online submissions for Validate Binary Search Tree.

# Memory Usage: 16.4 MB, less than 80.40% of Python3 online submissions for Validate Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    # Iterative Inorder Traversal
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal is smaller than the previous one,
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True