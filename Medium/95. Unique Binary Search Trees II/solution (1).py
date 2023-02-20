# 95. Unique Binary Search Trees II

# Runtime: 88 ms, faster than 28.14% of Python3 online submissions for Unique Binary Search Trees II.

# Memory Usage: 15.6 MB, less than 53.69% of Python3 online submissions for Unique Binary Search Trees II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:

        def generate(start: int, end: int) -> list[TreeNode]:
            if start > end:
                return [None]

            trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(i, left, right))
            return trees

        return generate(1, n)