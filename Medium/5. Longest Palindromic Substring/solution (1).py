# 5. Longest Palindromic Substring

# Runtime: 968 ms, faster than 73.70% of Python3 online submissions for Longest Palindromic Substring.

# Memory Usage: 14.3 MB, less than 81.19% of Python3 online submissions for Longest Palindromic Substring.


class Solution:
    # Expand Around Center
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_around_center(i, i)
            len2 = expand_around_center(i, i + 1)
            curr_max_len = max(len1, len2)
            if curr_max_len > end - start:
                start = i - (curr_max_len - 1) // 2
                end = i + curr_max_len // 2
        return s[start:end + 1]