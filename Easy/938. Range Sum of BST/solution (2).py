# 938. Range Sum of BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Search | Recursion
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0

        def dfs(node: TreeNode) -> None:
            nonlocal sum
            if not node:
                return

            curr = node.val
            if low <= curr <= high:
                sum += curr
            if curr < high:
                dfs(node.right)
            if low < curr:
                dfs(node.left)

        dfs(root)
        return sum