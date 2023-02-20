# 285. Inorder Successor in BST

# Runtime: 60 ms, faster than 98.52% of Python3 online submissions for Inorder Successor in BST.

# Memory Usage: 18.2 MB, less than 79.18% of Python3 online submissions for Inorder Successor in BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BST Properties
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor