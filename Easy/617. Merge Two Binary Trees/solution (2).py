# 617. Merge Two Binary Trees

# Runtime: 119 ms, faster than 17.48% of Python3 online submissions for Merge Two Binary Trees.

# Memory Usage: 15.2 MB, less than 91.85% of Python3 online submissions for Merge Two Binary Trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Method
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1

        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val
            if node1.right is None:
                node1.right = node2.right
            elif node2.right is not None:
                stack.append((node1.right, node2.right))

            if node1.left is None:
                node1.left = node2.left
            elif node2.left is not None:
                stack.append((node1.left, node2.left))
        return root1