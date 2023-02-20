# 230. K-th Smallest Element in a BST

# Runtime: 60 ms, faster than 46.99% of Python3 online submissions for K-th Smallest Element in a BST.

# Memory Usage: 18.3 MB, less than 16.80% of Python3 online submissions for K-th Smallest Element in a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Inorder Traversal
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root: TreeNode):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        return inorder(root)[k - 1]