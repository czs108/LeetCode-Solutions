# 124. Binary Tree Maximum Path Sum

# Runtime: 92 ms, faster than 42.32% of Python3 online submissions for Binary Tree Maximum Path Sum.

# Memory Usage: 21 MB, less than 83.13% of Python3 online submissions for Binary Tree Maximum Path Sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    # Recursion
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = -math.inf

        def max_gain(node: TreeNode) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max sum on the left and right sub-trees of node.
            left = max(0, max_gain(node.left))
            right = max(0, max_gain(node.right))

            # The price to start a new path where the current node is the highest node.
            new_path_sum = node.val + left + right

            # Update max path sum if it's better to start a new path.
            max_sum = max(max_sum, new_path_sum)

            # For recursion: return the max gain if continue the same path.
            return node.val + max(left, right)

        max_gain(root)
        return max_sum