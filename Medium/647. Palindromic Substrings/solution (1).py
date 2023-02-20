# 647. Palindromic Substrings

# Runtime: 546 ms, faster than 15.15% of Python3 online submissions for Palindromic Substrings.

# Memory Usage: 22.1 MB, less than 27.60% of Python3 online submissions for Palindromic Substrings.


class Solution:
    # Dynamic Programming
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        # Base case: single letter substrings.
        pln = [[False] * len(s) for _ in s]
        for i in range(len(s)):
            pln[i][i] = True
            count += 1

        # Base case: double letter substrings.
        for i in range(len(s) - 1):
            pln[i][i + 1] = s[i] == s[i + 1]
            count += 1 if pln[i][i + 1] else 0

        # All other cases: substrings of length 3 to `len(s)`.
        for n in range(3, len(s) + 1):
            i = 0
            j = i + n - 1
            while j < len(s):
                pln[i][j] = pln[i + 1][j - 1] and s[i] == s[j]
                count += 1 if pln[i][j] else 0
                i += 1
                j += 1

        return count