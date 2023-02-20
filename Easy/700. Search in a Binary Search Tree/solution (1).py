# 700. Search in a Binary Search Tree

# Runtime: 76 ms, faster than 47.96% of Python3 online submissions for Search in a Binary Search Tree.

# Memory Usage: 16.3 MB, less than 30.61% of Python3 online submissions for Search in a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        else:
            return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)