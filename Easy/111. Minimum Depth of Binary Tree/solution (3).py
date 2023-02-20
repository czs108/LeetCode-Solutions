# 111. Minimum Depth of Binary Tree

# Runtime: 480 ms, faster than 81.56% of Python3 online submissions for Minimum Depth of Binary Tree.

# Memory Usage: 49.5 MB, less than 62.27% of Python3 online submissions for Minimum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS Iteration
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        deq = deque([(1, root)])
        while len(deq) > 0:
            depth, root = deq.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for node in children:
                if node:
                    deq.append((depth + 1, node))