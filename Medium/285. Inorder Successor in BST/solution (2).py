# 285. Inorder Successor in BST

# Runtime: 68 ms, faster than 85.36% of Python3 online submissions for Inorder Successor in BST.

# Memory Usage: 18.1 MB, less than 79.18% of Python3 online submissions for Inorder Successor in BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Inorder tTraversal
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        stack = []
        find_p = False
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if find_p:
                return node
            elif node == p:
                find_p = True
            root = node.right
        return None