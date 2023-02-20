# 700. Search in a Binary Search Tree

# Runtime: 68 ms, faster than 89.53% of Python3 online submissions for Search in a Binary Search Tree.

# Memory Usage: 16.2 MB, less than 70.84% of Python3 online submissions for Search in a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and val != root.val:
            root = root.left if val < root.val else root.right
        return root