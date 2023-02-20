# 112. Path Sum

# Runtime: 40 ms, faster than 84.52% of Python3 online submissions for Path Sum.

# Memory Usage: 15.7 MB, less than 5.45% of Python3 online submissions for Path Sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Search | Recursion
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and root.val == targetSum:
            return True
        else:
            res = targetSum - root.val
            return self.hasPathSum(root.left, res) or self.hasPathSum(root.right, res)