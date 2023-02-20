# 107. Binary Tree Level Order Traversal II

# Runtime: 28 ms, faster than 93.24% of Python3 online submissions for Binary Tree Level Order Traversal II.

# Memory Usage: 14 MB, less than 7.41% of Python3 online submissions for Binary Tree Level Order Traversal II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Queue
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        que = [root]
        ret = []
        while len(que) != 0:
            ret.append([node.val for node in que])

            next_que = []
            for node in que:
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            que = next_que
        return ret[::-1]