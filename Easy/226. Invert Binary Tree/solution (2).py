# 226. Invert Binary Tree

# Runtime: 42 ms, faster than 20.11% of Python3 online submissions for Invert Binary Tree.

# Memory Usage: 14.1 MB, less than 91.16% of Python3 online submissions for Invert Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root