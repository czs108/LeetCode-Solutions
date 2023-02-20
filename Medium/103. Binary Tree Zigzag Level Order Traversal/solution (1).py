# 103. Binary Tree Zigzag Level Order Traversal

# Runtime: 32 ms, faster than 74.87% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# Memory Usage: 14.6 MB, less than 11.29% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Breadth-First Search
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        ans, curr_lvl = [], []
        nodes = [root]
        left_to_right = True
        while nodes:
            size = len(nodes)
            for _ in range(size):
                node = nodes.pop(0)
                if left_to_right:
                    curr_lvl.append(node.val)
                else:
                    curr_lvl.insert(0, node.val)

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            ans.append(curr_lvl)
            curr_lvl = []
            left_to_right = not left_to_right
        return ans