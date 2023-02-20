# 110. Balanced Binary Tree

# Runtime: 3232 ms, faster than 5.10% of Python3 online submissions for Balanced Binary Tree.

# Memory Usage: 17.6 MB, less than 100.00% of Python3 online submissions for Balanced Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            def get_depth(node: TreeNode) -> int:
                if not node:
                    return 0
                else:
                    return max(get_depth(node.left), get_depth(node.right)) + 1

            depth_diff = abs(get_depth(root.left) - get_depth(root.right)) <= 1
            balance_child = self.isBalanced(root.left) and self.isBalanced(root.right)
            return depth_diff and balance_child