# 236. Lowest Common Ancestor of a Binary Tree

# Runtime: 56 ms, faster than 99.62% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

# Memory Usage: 25.3 MB, less than 58.65% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p == root or q == root:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right:
                return root
            elif not left and not right:
                return None
            else:
                return left if left else right