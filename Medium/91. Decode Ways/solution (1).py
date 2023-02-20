# 91. Decode Ways

# Runtime: 24 ms, faster than 96.27% of Python3 online submissions for Decode Ways.

# Memory Usage: 13.8 MB, less than 16.00% of Python3 online submissions for Decode Ways.


class Solution:
    # Dynamic programming
    def numDecodings(self, s: str) -> int:
        count = [0 for _ in range(len(s) + 1)]
        # Empty strings have 1 way to decode.
        count[0] = 1

        for i in range(1, len(s) + 1):
            # Check if successful single digit decode is possible.
            if s[i - 1] != "0":
                count[i] = count[i - 1]
            if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
                # Check if successful two digit decode is possible.
                count[i] += count[i - 2]
        return count[-1]