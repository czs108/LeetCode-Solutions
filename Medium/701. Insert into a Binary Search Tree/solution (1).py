# 701. Insert into a Binary Search Tree

# Runtime: 140 ms, faster than 33.28% of Python3 online submissions for Insert into a Binary Search Tree.

# Memory Usage: 16.7 MB, less than 82.35% of Python3 online submissions for Insert into a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root