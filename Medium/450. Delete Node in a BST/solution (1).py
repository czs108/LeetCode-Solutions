# 450. Delete Node in a BST

# Runtime: 76 ms, faster than 71.33% of Python3 online submissions for Delete Node in a BST.

# Memory Usage: 18.4 MB, less than 88.65% of Python3 online submissions for Delete Node in a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(root: TreeNode) -> TreeNode:
            root = root.right
            while root.left:
                root = root.left
            return root.val

        def predecessor(root: TreeNode) -> TreeNode:
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # The node is a leaf.
            if not (root.right or root.left):
                root = None
            # The node is not a leaf and has a right child.
            elif root.right:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # The node is not a leaf, has no right child, and has a left child.
            else:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root