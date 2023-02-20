# 102. Binary Tree Level Order Traversal

# Runtime: 77 ms, faster than 5.20% of Python3 online submissions for Binary Tree Level Order Traversal.

# Memory Usage: 15.4 MB, less than 8.68% of Python3 online submissions for Binary Tree Level Order Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        output = []

        def helper(node: TreeNode, level: int) -> None:
            if level == len(output):
                output.append([])
            output[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return output