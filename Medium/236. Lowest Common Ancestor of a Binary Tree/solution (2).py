# 236. Lowest Common Ancestor of a Binary Tree

# Runtime: 72 ms, faster than 66.64% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

# Memory Usage: 18.2 MB, less than 90.52% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Iterative using parent pointers
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p == root or q == root:
            return root

        # Stack for tree traversal.
        stack = [root]

        # Dictionary for parent pointers.
        parent = {root: None}

        # Iterate until we find both the nodes `p` and `q`.
        while p not in parent or q not in parent:
            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

         # Ancestor set for node `p`.
        ancestors = set()

         # Process all ancestors for node `p` using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of `q` which appears in
        # `p`'s ancestor set is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q