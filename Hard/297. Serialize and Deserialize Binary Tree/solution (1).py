# 297. Serialize and Deserialize Binary Tree

# Runtime: 363 ms, faster than 13.22% of Python3 online submissions for Serialize and Deserialize Binary Tree.

# Memory Usage: 18.6 MB, less than 98.82% of Python3 online submissions for Serialize and Deserialize Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    # Depth-First Search | Preorder
    def serialize(self, root: TreeNode) -> str:
        data = ""

        def preorder(root: TreeNode) -> None:
            nonlocal data
            if not root:
                data += "None,"
            else:
                data += f"{root.val},"
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return data[:-1]

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(',')

        def preorder() -> None:
            if nodes[0] == "None":
                nodes.pop(0)
                return None
            else:
                root = TreeNode(nodes[0])
                nodes.pop(0)
                root.left = preorder()
                root.right = preorder()
            return root

        return preorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))