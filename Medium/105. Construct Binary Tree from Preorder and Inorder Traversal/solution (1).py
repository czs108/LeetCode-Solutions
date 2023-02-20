# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Runtime: 60 ms, faster than 81.53% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

# Memory Usage: 18.9 MB, less than 73.14% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        preorder_idx = 0
        inorder_idx_map = {}
        for i, v in enumerate(inorder):
            inorder_idx_map[v] = i

        def build(left: int, right: int) -> TreeNode:
            nonlocal preorder_idx
            if left > right:
                return None

            # Select the `preorder_idx` element as the root and increment it.
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1

            # Build left and right subtree,
            # excluding `inorder_idx_map[root_val]` element because it's the root.
            root.left = build(left, inorder_idx_map[root_val] - 1)
            root.right = build(inorder_idx_map[root_val] + 1, right)
            return root

        return build(0, len(preorder) - 1)