# 1120. Maximum Average Subtree

# Runtime: 60 ms, faster than 44.70% of Python3 online submissions for Maximum Average Subtree.

# Memory Usage: 17.1 MB, less than 11.35% of Python3 online submissions for Maximum Average Subtree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class State:
    def __init__(self, count: int, sum: float, max_avg: float) -> None:
        self.count: int = count
        self.sum: float = sum
        self.max_avg: float = max_avg


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:

        def traverse(root: TreeNode) -> State:
            if root is None:
                return State(0, 0, 0)
            else:
                left = traverse(root.left)
                right = traverse(root.right)

                count = left.count + right.count + 1
                sum = left.sum + right.sum + root.val
                max_avg = max(sum / count, left.max_avg, right.max_avg)
                return State(count, sum, max_avg)

        return traverse(root).max_avg