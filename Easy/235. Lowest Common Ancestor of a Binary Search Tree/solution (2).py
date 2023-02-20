# 235. Lowest Common Ancestor of a Binary Search Tree

# Runtime: 91 ms, faster than 33.28% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

# Memory Usage: 18 MB, less than 99.56% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root