# 938. Range Sum of BST

# Runtime: 206 ms, faster than 72.17% of Python3 online submissions for Range Sum of BST.

# Memory Usage: 22.3 MB, less than 59.19% of Python3 online submissions for Range Sum of BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Search | Iteration
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            curr = node.val
            if low <= curr <= high:
                sum += curr
            if curr < high:
                stack.append(node.right)
            if low < curr:
                stack.append(node.left)
        return sum