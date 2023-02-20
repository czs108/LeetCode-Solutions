# 145. Binary Tree Postorder Traversal

# Runtime: 32 ms, faster than 63.25% of Python3 online submissions for Binary Tree Postorder Traversal.

# Memory Usage: 14.3 MB, less than 13.58% of Python3 online submissions for Binary Tree Postorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        output = []

        def postorder(node: TreeNode) -> None:
            if node:
                postorder(node.left)
                postorder(node.right)
                output.append(node.val)

        postorder(root)
        return output