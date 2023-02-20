# 844. Backspace String Compare

# Runtime: 24 ms, faster than 96.27% of Python3 online submissions for Backspace String Compare.

# Memory Usage: 14.3 MB, less than 51.80% of Python3 online submissions for Backspace String Compare.


class Solution:
    # Build String
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(input: str) -> str:
            ans = []
            for c in input:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(s) == build(t)