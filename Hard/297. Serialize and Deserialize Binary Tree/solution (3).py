# 297. Serialize and Deserialize Binary Tree

# Runtime: 290 ms, faster than 25.00% of Python3 online submissions for Serialize and Deserialize Binary Tree.

# Memory Usage: 19.2 MB, less than 34.69% of Python3 online submissions for Serialize and Deserialize Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    # Level Order Traversal
    def serialize(self, root: TreeNode) -> str:
        data = ""

        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                data += "None,"
            else:
                data += f"{node.val},"
                stack.append(node.left)
                stack.append(node.right)
        return data[:-1]

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split(',')
        if nodes[0] == "None":
            return None

        root = TreeNode(nodes[0])
        stack = [root]
        i = 1
        # Or
        # while stack:
        while i != len(nodes):
            parent = stack.pop(0)

            left = nodes[i]
            i += 1
            if left != "None":
                parent.left = TreeNode(left)
                stack.append(parent.left)

            right = nodes[i]
            i += 1
            if right != "None":
                parent.right = TreeNode(right)
                stack.append(parent.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))