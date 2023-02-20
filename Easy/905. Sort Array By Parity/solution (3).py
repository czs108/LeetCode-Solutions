# 905. Sort Array By Parity

# Runtime: 108 ms, faster than 5.34% of Python3 online submissions for Sort Array By Parity.

# Memory Usage: 15 MB, less than 5.82% of Python3 online submissions for Sort Array By Parity.


class Solution:
    # In-Place
    def sortArrayByParity(self, A: list[int]) -> list[int]:
        # Everything below `i` has parity 0.
        # Everything above `j` has parity 1.
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A