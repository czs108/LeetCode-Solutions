# 199. Binary Tree Right Side View

# Runtime: 36 ms, faster than 56.76% of Python3 online submissions for Binary Tree Right Side View.

# Memory Usage: 14.3 MB, less than 20.76% of Python3 online submissions for Binary Tree Right Side View.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth-First Search
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        right = []

        def dfs(root: TreeNode, lvl: int) -> None:
            if lvl == len(right):
                right.append(root.val)

            for child in [root.right, root.left]:
                if child:
                     dfs(child, lvl + 1)

        dfs(root, 0)
        return right