# 701. Insert into a Binary Search Tree

# Runtime: 136 ms, faster than 58.91% of Python3 online submissions for Insert into a Binary Search Tree.

# Memory Usage: 16.9 MB, less than 24.13% of Python3 online submissions for Insert into a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iteration
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)