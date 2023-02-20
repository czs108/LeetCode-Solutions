# 107. Binary Tree Level Order Traversal II

# Runtime: 32 ms, faster than 79.70% of Python3 online submissions for Binary Tree Level Order Traversal II.

# Memory Usage: 14.3 MB, less than 7.41% of Python3 online submissions for Binary Tree Level Order Traversal II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS & Dictionary
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        dict = {}

        def dfs(node: TreeNode, deep: int) -> None:
            if not node:
                return
            elif deep in dict:
                dict[deep].append(node.val)
            else:
                dict[deep] = [node.val]
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)

        dfs(root, 0)
        return list(dict.values())[::-1]