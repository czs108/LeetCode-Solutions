# 96. Unique Binary Search Trees

# Runtime: 47 ms, faster than 14.41% of Python3 online submissions for Unique Binary Search Trees.

# Memory Usage: 14.2 MB, less than 74.34% of Python3 online submissions for Unique Binary Search Trees.


class Solution:
    # Dynamic Programming
    def numTrees(self, n: int) -> int:
        # The number of unique BST for a sequence of length `n`.
        count = [0] * (n + 1)
        count[0], count[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                count[i] += count[j - 1] * count[i - j]

        return count[-1]