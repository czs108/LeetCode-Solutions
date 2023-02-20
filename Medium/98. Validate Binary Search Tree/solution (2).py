# 98. Validate Binary Search Tree

# Runtime: 40 ms, faster than 88.33% of Python3 online submissions for Validate Binary Search Tree.

# Memory Usage: 16.3 MB, less than 80.40% of Python3 online submissions for Validate Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    # Iterative Traversal with Valid Range
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, min, max = stack.pop()
            if node is None:
                continue
            val = node.val
            if val <= min or val >= max:
                return False
            stack.append((node.left, min, val))
            stack.append((node.right, val, max))
        return True