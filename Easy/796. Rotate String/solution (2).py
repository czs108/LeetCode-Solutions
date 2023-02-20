# 796. Rotate String

# Runtime: 28 ms, faster than 82.80% of Python3 online submissions for Rotate String.

# Memory Usage: 13.8 MB, less than 64.00% of Python3 online submissions for Rotate String.


class Solution:
    # Simple Check
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A