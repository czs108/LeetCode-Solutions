# 297. Serialize and Deserialize Binary Tree

# Runtime: 112 ms, faster than 90.06% of Python3 online submissions for Serialize and Deserialize Binary Tree.

# Memory Usage: 18.9 MB, less than 52.26% of Python3 online submissions for Serialize and Deserialize Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    # Depth-First Search | Postorder
    def serialize(self, root: TreeNode) -> str:
        data = ""

        def postorder(root: TreeNode) -> None:
            nonlocal data
            if not root:
                data += "None,"
            else:
                postorder(root.left)
                postorder(root.right)
                data += f"{root.val},"

        postorder(root)
        return data[:-1]

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(',')

        def postorder() -> None:
            if nodes[-1] == "None":
                nodes.pop(-1)
                return None
            else:
                root = TreeNode(nodes[-1])
                nodes.pop(-1)
                root.right = postorder()
                root.left = postorder()
            return root

        return postorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))