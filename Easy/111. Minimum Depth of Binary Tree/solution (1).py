# 111. Minimum Depth of Binary Tree

# Runtime: 48 ms, faster than 42.05% of Python3 online submissions for Minimum Depth of Binary Tree.

# Memory Usage: 15.5 MB, less than 51.35% of Python3 online submissions for Minimum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1