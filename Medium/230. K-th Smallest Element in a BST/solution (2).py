# 230. Kth Smallest Element in a BST

# Runtime: 56 ms, faster than 59.70% of Python3 online submissions for Kth Smallest Element in a BST.

# Memory Usage: 17.7 MB, less than 99.54% of Python3 online submissions for Kth Smallest Element in a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Inorder Traversal
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right

        return inorder[k - 1]