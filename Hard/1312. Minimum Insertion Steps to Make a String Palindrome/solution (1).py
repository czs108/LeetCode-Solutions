# 1312. Minimum Insertion Steps to Make a String Palindrome

# Runtime: 732 ms, faster than 81.20% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.

# Memory Usage: 16.3 MB, less than 31.75% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.


class Solution:
    def minInsertions(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        count = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for left in range(len(s) - 1, -1, -1):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    count[left][right] = count[left + 1][right - 1]
                else:
                    count[left][right] = min(count[left + 1][right], count[left][right - 1]) + 1
        return count[0][-1]