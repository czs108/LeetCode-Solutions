# 977. Squares of a Sorted Array

# Runtime: 204 ms, faster than 83.47% of Python3 online submissions for Squares of a Sorted Array.


class Solution:
    # Sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)