# 94. Binary Tree Inorder Traversal

# Runtime: 37 ms, faster than 22.46% of Python3 online submissions for Binary Tree Inorder Traversal.

# Memory Usage: 14.2 MB, less than 74.98% of Python3 online submissions for Binary Tree Inorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterations
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack, output = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            output.append(node.val)
            node = node.right
        return output