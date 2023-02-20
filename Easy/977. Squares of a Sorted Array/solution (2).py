# 977. Squares of a Sorted Array

# Runtime: 300 ms, faster than 6.84% of Python3 online submissions for Squares of a Sorted Array.

# Memory Usage: 16.2 MB, less than 10.10% of Python3 online submissions for Squares of a Sorted Array.


class Solution:
    # Two Pointer
    def sortedSquares(self, A: list[int]) -> list[int]:
        # i, j: negative, positive parts
        j = 0
        while j < len(A) and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < len(A):
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < len(A):
            ans.append(A[j]**2)
            j += 1

        return ans