# 113. Path Sum II

# Runtime: 40 ms, faster than 94.30% of Python3 online submissions for Path Sum II.

# Memory Usage: 15.7 MB, less than 63.80% of Python3 online submissions for Path Sum II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Traversal | Recursion
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        ans = []

        def dfs(root: TreeNode, remain: int, path: list[int]) -> None:
            if not root:
                return

            path.append(root.val)
            if remain == root.val and not root.left and not root.right:
                ans.append(list(path))
            else:
                dfs(root.left, remain - root.val, path)
                dfs(root.right, remain - root.val, path)
            path.pop()

        dfs(root, targetSum, [])
        return ans