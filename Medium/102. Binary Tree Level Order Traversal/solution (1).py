# 102. Binary Tree Level Order Traversal

# Runtime: 32 ms, faster than 85.10% of Python3 online submissions for Binary Tree Level Order Traversal.

# Memory Usage: 14.6 MB, less than 67.10% of Python3 online submissions for Binary Tree Level Order Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iteration
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        que, output = [root], []
        while que:
            size = len(que)
            curr_lvl = []
            for _ in range(size):
                node = que.pop(0)
                curr_lvl.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            output.append(curr_lvl)
                       return output