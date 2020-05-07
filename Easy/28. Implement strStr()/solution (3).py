# 28. Implement strStr()

# Runtime: 44 ms, faster than 21.72% of Python3 online submissions for Implement strStr().

# Memory Usage: 15.3 MB, less than 6.15% of Python3 online submissions for Implement strStr().


class Solution:
    # Knuth-Morris-Pratt
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        next = self.__buildNext(needle)
        i, j = 0, 0
        n = len(needle)
        while i < len(haystack) and j < n:
            while j > 0 and needle[j] != haystack[i]:
                j = next[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            i += 1

        if j == n:
            return i - n
        else:
            return -1

    def __buildNext(self, needle: str) -> List[int]:
        assert len(needle) != 0

        n = len(needle)
        next = [0 for _ in range(n)]
        j = 0
        for i in range(1, n):
            while j > 0 and needle[j] != needle[i]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j
        return next