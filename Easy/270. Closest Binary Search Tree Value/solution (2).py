# 270. Closest Binary Search Tree Value

# Runtime: 40 ms, faster than 72.19% of Python3 online submissions for Closest Binary Search Tree Value.

# Memory Usage: 16.2 MB, less than 59.89% of Python3 online submissions for Closest Binary Search Tree Value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Inorder | Linear Search
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(root: TreeNode) -> list[int]:
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []

        return min(inorder(root), key=lambda x: abs(target - x))