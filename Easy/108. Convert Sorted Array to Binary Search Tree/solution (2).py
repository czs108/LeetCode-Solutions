# 108. Convert Sorted Array to Binary Search Tree

# Runtime: 80 ms, faster than 32.78% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Memory Usage: 16.1 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            return TreeNode(nums[mid],
                    self.sortedArrayToBST(nums[:mid]),
                    self.sortedArrayToBST(nums[mid + 1:]))