# 10. Regular Expression Matching

# Runtime: 44 ms, faster than 81.22% of Python3 online submissions for Regular Expression Matching.

# Memory Usage: 14.7 MB, less than 5.61% of Python3 online submissions for Regular Expression Matching.


class Solution:
    # Top-Down Dynamic Programming
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        # match[i, j] means whether s[i:] and p[j:] match.
        match = {}

        def is_match(i: int, j: int) -> bool:
            if (i, j) not in match:
                if j == len(p):
                    ret = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        # '*' matches a single character.
                        single_match = first_match and is_match(i + 1, j)
                        # '*' does not match any character.
                        zero_match = is_match(i, j + 2)
                        ret = single_match or zero_match
                    else:
                        ret = first_match and is_match(i + 1, j + 1)
                match[i, j] = ret
            return match[i, j]

        return is_match(0, 0)