# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        postorder_idx = len(postorder) - 1
        inorder_idx_map = {}
        for i, v in enumerate(inorder):
            inorder_idx_map[v] = i

        def build(left: int, right: int) -> TreeNode:
            nonlocal postorder_idx
            if left > right:
                return None

            # Select the `postorder_idx` element as the root and decrement it.
            root_val = postorder[postorder_idx]
            root = TreeNode(root_val)
            postorder_idx -= 1

            # Build right and left subtree,
            # excluding `inorder_idx_map[root_val]` element because it's the root.
            root.right = build(inorder_idx_map[root_val] + 1, right)
            root.left = build(left, inorder_idx_map[root_val] - 1)
            return root

        return build(0, len(postorder) - 1)