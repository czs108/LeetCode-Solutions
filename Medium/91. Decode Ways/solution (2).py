# 91. Decode Ways

# Runtime: 28 ms, faster than 87.93% of Python3 online submissions for Decode Ways.

# Memory Usage: 14.1 MB, less than 84.49% of Python3 online submissions for Decode Ways.


class Solution:
    # Recursive Approach with Memoization
    def __init__(self) -> None:
        self._counts: list[int] = None

    def numDecodings(self, s: str) -> int:
        self._counts = [-1] * len(s)
        return self._decode(s, 0)

    def _decode(self, s: str, start: int) -> int:
        if start == len(s):
            # If you reach the end of the string, return 1 for success.
            return 1
        elif s[start] == "0":
            return 0
        elif start == len(s) - 1:
            return 1
        elif self._counts[start] >= 0:
            return self._counts[start]

        ans = self._decode(s, start + 1)
        if int(s[start:start + 2]) <= 26:
            ans += self._decode(s, start + 2)
        self._counts[start] = ans
        return ans