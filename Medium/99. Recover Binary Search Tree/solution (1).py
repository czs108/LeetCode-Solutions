# 99. Recover Binary Search Tree

# Runtime: 80 ms, faster than 30.01% of Python3 online submissions for Recover Binary Search Tree.

# Memory Usage: 14.7 MB, less than 57.01% of Python3 online submissions for Recover Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Sort an Almost Sorted Array Where Two Elements Are Swapped
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node: TreeNode) -> list[int]:
            if node is None:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        def find_swapped(nums: list[int]) -> list[int, int]:
            x = y = None
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y

        nums = inorder(root)
        x, y = find_swapped(nums)
        count = 2
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == x or node.val == y:
                node.val = y if node.val == x else x
                count -= 1
                if count == 0:
                    break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)