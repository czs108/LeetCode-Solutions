# 337. House Robber III

# Runtime: 48 ms, faster than 79.07% of Python3 online submissions for House Robber III.

# Memory Usage: 16.1 MB, less than 95.79% of Python3 online submissions for House Robber III.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def rob(self, root: TreeNode) -> int:
        # Return (rob this node, not rob this node).
        def helper(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0, 0)
            else:
                left = helper(node.left)
                right = helper(node.right)
                # Rob this.
                robbed = node.val + left[1] + right[1]
                not_robbed = max(left) + max(right)
                return (robbed, not_robbed)

        return max(helper(root))