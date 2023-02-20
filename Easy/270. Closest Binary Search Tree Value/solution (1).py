# 270. Closest Binary Search Tree Value

# Runtime: 45 ms, faster than 29.11% of Python3 online submissions for Closest Binary Search Tree Value.

# Memory Usage: 16.1 MB, less than 59.89% of Python3 online submissions for Closest Binary Search Tree Value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Binary Search
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest