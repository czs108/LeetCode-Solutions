# 344. Reverse String

# Runtime: 196 ms, faster than 79.63% of Python3 online submissions for Reverse String.

# Memory Usage: 18.5 MB, less than 60.87% of Python3 online submissions for Reverse String.


class Solution:
    # Two Pointers
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        