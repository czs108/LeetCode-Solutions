# 647. Palindromic Substrings

# Runtime: 128 ms, faster than 79.15% of Python3 online submissions for Palindromic Substrings.

# Memory Usage: 14.1 MB, less than 85.33% of Python3 online submissions for Palindromic Substrings.


class Solution:
    # Expand Around Possible Centers
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand_around_center(left: int, right: int) -> None:
            nonlocal count
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    count += 1
                    left -= 1
                    right += 1

        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        return count