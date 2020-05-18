# 13. Roman to Integer

# Runtime: 48 ms, faster than 52.35% of Python3 online submissions for Roman to Integer.

# Memory Usage: 13.8 MB, less than 5.38% of Python3 online submissions for Roman to Integer.


class Solution:
    _NUM_MAP = { "I": 1,\
                 "V": 5,\
                 "X": 10,\
                 "L": 50,\
                 "C": 100,\
                 "D": 500,\
                 "M": 1000 }

    def romanToInt(self, s: str) -> int:
        prev = 0
        sum = 0
        for i in s:
            curr = Solution._NUM_MAP[i]
            # Roman numerals are usually written largest to smallest from left to right.
            if curr <= prev:
                sum += curr
            else:
                sum += curr - 2 * prev
            prev = curr
        return sum