# 1026. Maximum Difference Between Node and Ancestor

# Runtime: 67 ms, faster than 13.46% of Python3 online submissions for Maximum Difference Between Node and Ancestor.

# Memory Usage: 20.7 MB, less than 44.74% of Python3 online submissions for Maximum Difference Between Node and Ancestor.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None) -> None:
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    # Recursion
    def maxAncestorDiff(self, root: TreeNode) -> int:
        v = -math.inf

        def dfs(node: TreeNode, min_val: int, max_val: int) -> None:
            nonlocal v
            if not node:
                return

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            v = max(v, max_val - min_val)
            if node.left:
                dfs(node.left, min_val, max_val)
            if node.right:
                dfs(node.right, min_val, max_val)

        dfs(root, math.inf, -math.inf)
        return v