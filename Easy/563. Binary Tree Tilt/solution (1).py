# 563. Binary Tree Tilt

# Runtime: 65 ms, faster than 36.41% of Python3 online submissions for Binary Tree Tilt.

# Memory Usage: 16.4 MB, less than 24.41% of Python3 online submissions for Binary Tree Tilt.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Post-Order Depth-First Traversal
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def calc_sum(node: TreeNode) -> int:
            nonlocal total_tilt
            if not node:
                return 0
            left = calc_sum(node.left)
            right = calc_sum(node.right)
            tilt = abs(right - left)
            total_tilt += tilt
            return left + right + node.val

        calc_sum(root)
        return total_tilt