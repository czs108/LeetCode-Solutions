# 111. Minimum Depth of Binary Tree

# Runtime: 652 ms, faster than 16.32% of Python3 online submissions for Minimum Depth of Binary Tree.

# Memory Usage: 49.4 MB, less than 62.27% of Python3 online submissions for Minimum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS Iteration
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(1, root)]
        min_depth = math.inf
        while len(stack) > 0:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for node in children:
                if node:
                    stack.append((depth + 1, node))

        return min_depth