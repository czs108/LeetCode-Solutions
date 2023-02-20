# 199. Binary Tree Right Side View

# Runtime: 24 ms, faster than 98.24% of Python3 online submissions for Binary Tree Right Side View.

# Memory Usage: 14.1 MB, less than 79.56% of Python3 online submissions for Binary Tree Right Side View.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Breadth-First Search
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        stack = [root]
        right = []
        while stack:
            count = len(stack)
            for _ in range(count):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            right.append(node.val)
        return right