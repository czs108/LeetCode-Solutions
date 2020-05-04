# 28. Implement strStr()

# Runtime: 32 ms, faster than 49.21% of Python3 online submissions for Implement strStr().

# Memory Usage: 14.1 MB, less than 12.31% of Python3 online submissions for Implement strStr().


class Solution:
    # Brute Force
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        n = len(needle)
        for i in range(len(haystack) - n + 1):
            # Can not use `range(n)`
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                else:
                    j += 1
            if j == n:
                return i
        return -1