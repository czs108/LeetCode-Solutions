# 230. Kth Smallest Element in a BST

# Runtime: 44 ms, faster than 94.57% of Python3 online submissions for Kth Smallest Element in a BST.

# Memory Usage: 18 MB, less than 59.57% of Python3 online submissions for Kth Smallest Element in a BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Inorder Traversal
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            else:
                root = root.right

        assert False