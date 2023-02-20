# 572. Subtree of Another Tree

# Runtime: 190 ms, faster than 26.06% of Python3 online submissions for Subtree of Another Tree.

# Memory Usage: 15.4 MB, less than 29.15% of Python3 online submissions for Subtree of Another Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def dfs(root1: TreeNode, root2: TreeNode) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2 or root1.val != root2.val:
                return False
            else:
                return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        if not root:
            return False
        elif dfs(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)