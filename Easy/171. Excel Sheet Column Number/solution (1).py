# 171. Excel Sheet Column Number

# Runtime: 28 ms, faster than 85.73% of Python3 online submissions for Excel Sheet Column Number.

# Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for Excel Sheet Column Number.


class Solution:
    _BASE = 26
    _ASCII_A = 65

    def titleToNumber(self, s: str) -> int:
        ret = ord(s[0]) - Solution._ASCII_A + 1
        for i in range(1, len(s)):
            ret = ret * Solution._BASE + (ord(s[i]) - Solution._ASCII_A + 1)
        return ret