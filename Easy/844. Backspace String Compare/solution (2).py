# 844. Backspace String Compare

# Runtime: 20 ms, faster than 99.32% of Python3 online submissions for Backspace String Compare.

# Memory Usage: 14.4 MB, less than 18.72% of Python3 online submissions for Backspace String Compare.


class Solution:
    # Two Pointers
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            elif (i >= 0) != (j >= 0):
                return False
            else:
                i -= 1
                j -= 1

        return True