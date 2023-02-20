# 10. Regular Expression Matching

# Runtime: 1400 ms, faster than 9.60% of Python3 online submissions for Regular Expression Matching.

# Memory Usage: 14.1 MB, less than 97.94% of Python3 online submissions for Regular Expression Matching.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        first_match = len(s) != 0 and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # '*' matches a single character.
            single_match = first_match and self.isMatch(s[1:], p)
            # '*' does not match any character.
            zero_match = self.isMatch(s, p[2:])
            return single_match or zero_match
        else:
            return first_match and self.isMatch(s[1:], p[1:])