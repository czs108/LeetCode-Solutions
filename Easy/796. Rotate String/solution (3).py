# 796. Rotate String

# Runtime: 32 ms, faster than 61.26% of Python3 online submissions for Rotate String.

# Memory Usage: 13.6 MB, less than 92.00% of Python3 online submissions for Rotate String.


class Solution:
    # Knuth-Morris-Pratt
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif len(A) == 0:
            return True

        def build_shift_table() -> list[int]:
            shifts = [1 for _ in range(len(A) + 1)]
            left = -1
            for right in range(len(A)):
                while left >= 0 and B[left] != B[right]:
                    left -= shifts[left]
                shifts[right + 1] = right - left
                left += 1
            return shifts

        shifts = build_shift_table()
        match_len = 0
        for c in A + A:
            while match_len >= 0 and B[match_len] != c:
                match_len -= shifts[match_len]
            match_len += 1
            if match_len == len(A):
                return True
        return False