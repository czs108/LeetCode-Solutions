# 112. Path Sum

# Runtime: 32 ms, faster than 98.94% of Python3 online submissions for Path Sum.

# Memory Usage: 15.1 MB, less than 81.00% of Python3 online submissions for Path Sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iteration
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]
        while stack:
            node, curr_sum = stack.pop()
            curr_sum -= node.val
            if curr_sum == 0 and not node.left and not node.right:
                return True
            if node.left:
                stack.append((node.left, curr_sum))
            if node.right:
                stack.append((node.right, curr_sum))
        return False