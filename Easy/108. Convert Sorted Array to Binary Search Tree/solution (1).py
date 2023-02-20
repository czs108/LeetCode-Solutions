# 108. Convert Sorted Array to Binary Search Tree

# Runtime: 72 ms, faster than 80.62% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Memory Usage: 16.2 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            else:
                mid = left + (right - left) // 2
                root = TreeNode(nums[mid])
                root.left = build(left, mid - 1)
                root.right = build(mid + 1, right)
                return root

        return build(0, len(nums) - 1)