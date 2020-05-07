# 104. Maximum Depth of Binary Tree

# Runtime: 40 ms, faster than 70.85% of Python3 online submissions for Maximum Depth of Binary Tree.

# Memory Usage: 15 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_depth = 0
        stack = []
        stack.append((root, 1))
        while len(stack) != 0:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth