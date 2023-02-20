# 171. Excel Sheet Column Number

# Runtime: 28 ms, faster than 85.73% of Python3 online submissions for Excel Sheet Column Number.

# Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for Excel Sheet Column Number.


class Solution:
    _BASE = 26

    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for c in columnTitle:
            num = num * self._BASE + (ord(c) - ord('A') + 1)
        return num