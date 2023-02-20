# 10. Regular Expression Matching

# Runtime: 56 ms, faster than 57.21% of Python3 online submissions for Regular Expression Matching.

# Memory Usage: 14.4 MB, less than 54.80% of Python3 online submissions for Regular Expression Matching.


class Solution:
    # Bottom-Up Dynamic Programming
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        # match[i][j] means whether s[i:] and p[j:] match.
        match = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        match[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    # '*' matches a single character.
                    single_match = first_match and match[i + 1][j]
                    # '*' does not match any character.
                    zero_match = match[i][j + 2]
                    match[i][j] = single_match or zero_match
                else:
                    match[i][j] = first_match and match[i + 1][j + 1]
        return match[0][0]