# 132. Palindrome Partitioning II

# Runtime: 452 ms, faster than 70.36% of Python3 online submissions for Palindrome Partitioning II.

# Memory Usage: 32.1 MB, less than 26.64% of Python3 online submissions for Palindrome Partitioning II.


import math

class Solution:
    # Dynamic programming
    def minCut(self, s: str) -> int:
        if len(s) == 0:
            return 0

        def find_palin() -> list[list[bool]]:
            is_palin = [[False for _ in range(len(s))] for _ in range(len(s))]

            # Check strings of odd length
            for c in range(len(s)):
                i = j = c
                # Extend to both directions
                while 0 <= i and j < len(s) and s[i] == s[j]:
                    is_palin[i][j] = True
                    i -= 1
                    j += 1

            # Check strings of even length
            for c in range(len(s) - 1):
                i = c
                j = c + 1
                while 0 <= i and j < len(s) and s[i] == s[j]:
                    is_palin[i][j] = True
                    i -= 1
                    j += 1

            return is_palin

        is_palin = find_palin()
        count = [0 for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            count[i] = math.inf
            for j in range(i):
                if is_palin[j][i - 1]:
                    count[i] = min(count[i], count[j] + 1)
        return count[-1] - 1