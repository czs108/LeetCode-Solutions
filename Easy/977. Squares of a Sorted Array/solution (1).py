# 977. Squares of a Sorted Array

# Runtime: 204 ms, faster than 83.47% of Python3 online submissions for Squares of a Sorted Array.


class Solution:
    # Sort
    def sortedSquares(self, A: list[int]) -> list[int]:
        return sorted(x*x for x in A)