# 250. Count Univalue Subtrees

# Runtime: 36 ms, faster than 65.50% of Python3 online submissions for Count Univalue Subtrees.

# Memory Usage: 14.5 MB, less than 49.79% of Python3 online submissions for Count Univalue Subtrees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Search | Pass Parent Values
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        def is_unival(node: TreeNode, parent_val: int) -> bool:
            nonlocal count
            if not node:
                return True
            elif not all([is_unival(node.left, node.val), is_unival(node.right, node.val)]):
                return False
            else:
                count += 1
                # At this point we know that this node is a univalue subtree of value `node.val`.
                # Pass a boolean indicating if this is a valid subtree for the parent node.
                return node.val == parent_val

        is_unival(root, 0)
        return count