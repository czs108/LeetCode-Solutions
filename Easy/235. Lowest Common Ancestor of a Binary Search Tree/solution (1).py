# 235. Lowest Common Ancestor of a Binary Search Tree

# Runtime: 88 ms, faster than 37.11% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

# Memory Usage: 18 MB, less than 94.79% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Iterative
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
        return None