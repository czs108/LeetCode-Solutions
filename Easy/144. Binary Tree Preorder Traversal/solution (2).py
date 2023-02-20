# 144. Binary Tree Preorder Traversal

# Runtime: 20 ms, faster than 99.14% of Python3 online submissions for Binary Tree Preorder Traversal.

# Memory Usage: 14.2 MB, less than 45.31% of Python3 online submissions for Binary Tree Preorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        output = []

        def preorder(node: TreeNode) -> None:
            if node:
                output.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return output