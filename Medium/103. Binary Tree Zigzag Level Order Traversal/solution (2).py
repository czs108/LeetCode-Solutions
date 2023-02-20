# 103. Binary Tree Zigzag Level Order Traversal

# Runtime: 28 ms, faster than 91.36% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# Memory Usage: 14.5 MB, less than 42.40% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth-First Search
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        def dfs(node: TreeNode, lvl: int) -> None:
            if lvl >= len(ans):
                ans.append([node.val])
            elif lvl % 2 == 0:
                ans[lvl].append(node.val)
            else:
                ans[lvl].insert(0, node.val)

            for next in [node.left, node.right]:
                if next:
                    dfs(next, lvl + 1)

        dfs(root, 0)
        return ans