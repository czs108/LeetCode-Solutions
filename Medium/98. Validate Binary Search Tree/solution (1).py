# 98. Validate Binary Search Tree

# Runtime: 44 ms, faster than 69.73% of Python3 online submissions for Validate Binary Search Tree.

# Memory Usage: 16.3 MB, less than 94.54% of Python3 online submissions for Validate Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Traversal with Valid Range
    def isValidBST(self, root: TreeNode) -> bool:

        def is_valid_bst(root: TreeNode, min: TreeNode, max: TreeNode) -> bool:
            if root is None:
                return True
            elif min is not None and root.val <= min.val:
                return False
            elif max is not None and root.val >= max.val:
                return False
            else:
                return is_valid_bst(root.left, min, root) and is_valid_bst(root.right, root, max)

        return is_valid_bst(root, None, None)