# 124. Binary Tree Maximum Path Sum

# Runtime: 92 ms, faster than 42.32% of Python3 online submissions for Binary Tree Maximum Path Sum.

# Memory Usage: 21 MB, less than 83.13% of Python3 online submissions for Binary Tree Maximum Path Sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._max = -math.inf

    def maxPathSum(self, root: TreeNode) -> int:
        self._max_gain(root)
        return self._max

    def _max_gain(self, node: TreeNode) -> int:
        if not node:
            return 0

        # Max sum on the left and right sub-trees of node.
        left = max(0, self._max_gain(node.left))
        right = max(0, self._max_gain(node.right))

        # The price to start a new path where `node` is a highest node.
        new_path_val = node.val + left + right

        # Update max_sum if it's better to start a new path.
        self._max = max(self._max, new_path_val)

        # for recursion:
        # return the max gain if continue the same path.
        return node.val + max(left, right)
