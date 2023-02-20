# 250. Count Univalue Subtrees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Depth First Search
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        def is_unival(node: TreeNode) -> bool:
            nonlocal count
            if not node.left and not node.right:
                count += 1
                return True
            else:
                unival = True
                if node.left:
                    unival = is_unival(node.left) and unival and node.left.val == node.val
                if node.right:
                    unival = is_unival(node.right) and unival and node.right.val == node.val
                count += unival
                return unival

        is_unival(root)
        return count