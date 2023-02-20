# 144. Binary Tree Preorder Traversal

# Runtime: 45 ms, faster than 14.20% of Python3 online submissions for Binary Tree Preorder Traversal.

# Memory Usage: 14.1 MB, less than 74.55% of Python3 online submissions for Binary Tree Preorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterations
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output