# 270. Closest Binary Search Tree Value

# Runtime: 50 ms, faster than 22.26% of Python3 online submissions for Closest Binary Search Tree Value.

# Memory Usage: 16.2 MB, less than 13.18% of Python3 online submissions for Closest Binary Search Tree Value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import bisect

class Solution:
    # Recursive Inorder | Binary Search
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(root: TreeNode) -> list[int]:
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []

        vals = inorder(root)
        idx = bisect.bisect_left(vals, target)
        if idx == len(vals):
            return vals[-1]
        elif idx == 0:
            return vals[0]
        else:
            return min(vals[idx], vals[idx - 1], key=lambda x: abs(target - x))