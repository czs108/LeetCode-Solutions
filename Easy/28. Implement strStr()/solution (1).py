# 28. Implement strStr()

# Runtime: 32 ms, faster than 49.21% of Python3 online submissions for Implement strStr().

# Memory Usage: 14.1 MB, less than 12.31% of Python3 online submissions for Implement strStr().


class Solution:
    # Brute Force
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            # Can not use `range(len(needle))`
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                else:
                    j += 1
            if j == len(needle):
                return i
        return -1