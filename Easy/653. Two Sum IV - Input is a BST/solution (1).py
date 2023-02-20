# 653. Two Sum IV - Input is a BST

# Runtime: 109 ms, faster than 20.18% of Python3 online submissions for Two Sum IV - Input is a BST.

# Memory Usage: 16.7 MB, less than 72.11% of Python3 online submissions for Two Sum IV - Input is a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Hash Set
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if (k - node.val) in nums:
                return True
            nums.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False