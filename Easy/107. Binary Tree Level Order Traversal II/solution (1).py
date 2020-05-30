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
    def __init__(self):
        self._dict = {}

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self._dfs(root, 0)
        return list(self._dict.values())[::-1]

    def _dfs(self, node: TreeNode, deep: int) -> None:
        if not node:
            return
        elif deep in self._dict:
            self._dict[deep].append(node.val)
        else:
            self._dict[deep] = [node.val]
        self._dfs(node.left, deep + 1)
        self._dfs(node.right, deep + 1)