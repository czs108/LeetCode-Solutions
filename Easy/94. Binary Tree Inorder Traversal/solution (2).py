# 94. Binary Tree Inorder Traversal

# Runtime: 50 ms, faster than 10.24% of Python3 online submissions for Binary Tree Inorder Traversal.

# Memory Usage: 14.1 MB, less than 91.45% of Python3 online submissions for Binary Tree Inorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        output = []

        def inorder(node: TreeNode) -> None:
            if node:
                inorder(node.left)
                output.append(node.val)
                inorder(node.right)

        inorder(root)
        return output