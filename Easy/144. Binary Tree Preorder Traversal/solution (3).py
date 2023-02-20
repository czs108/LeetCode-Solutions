# 144. Binary Tree Preorder Traversal

# Runtime: 28 ms, faster than 85.09% of Python3 online submissions for Binary Tree Preorder Traversal.

# Memory Usage: 14.3 MB, less than 12.95% of Python3 online submissions for Binary Tree Preorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterations
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack, output = [], []
        node = root
        while node or stack:
            while node:
                output.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop(-1).right
        return output