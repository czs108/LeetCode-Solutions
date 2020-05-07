# 104. Maximum Depth of Binary Tree

# Runtime: 40 ms, faster than 70.85% of Python3 online submissions for Maximum Depth of Binary Tree.

# Memory Usage: 15.2 MB, less than 88.54% of Python3 online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1