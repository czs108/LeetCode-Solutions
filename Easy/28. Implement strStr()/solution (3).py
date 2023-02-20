# 28. Implement strStr()

# Runtime: 44 ms, faster than 21.72% of Python3 online submissions for Implement strStr().

# Memory Usage: 15.3 MB, less than 6.15% of Python3 online submissions for Implement strStr().


class Solution:
    # Knuth-Morris-Pratt
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        def build_next(needle: str) -> list[int]:
            next = [0 for _ in range(len(needle))]
            left = 0
            for right in range(1, len(needle)):
                while left > 0 and needle[left] != needle[right]:
                    left = next[left - 1]
                if needle[right] == needle[left]:
                    left += 1
                next[right] = left
            return next

        next = build_next(needle)
        i, match_len = 0, 0
        while i < len(haystack) and match_len < len(needle):
            while match_len > 0 and needle[match_len] != haystack[i]:
                match_len = next[match_len - 1]
            if needle[match_len] == haystack[i]:
                match_len += 1
            i += 1

        if match_len == len(needle):
            return i - len(needle)
        else:
            return -1