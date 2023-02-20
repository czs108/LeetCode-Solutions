# 392. Is Subsequence

# Time Limit Exceeded


class Solution:
    # Dynamic Programming
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif len(s) == len(t):
            return s == t

        match = [[0] * len(t) for _ in range(len(t))]
        for i in range(len(t)):
            if t[i] == s[0]:
                match[i][i] = 1

        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                matched = match[i][j - 1]
                if t[j] == s[matched]:
                    match[i][j] = matched + 1
                else:
                    match[i][j] = matched
                if match[i][j] == len(s):
                    return True
        return False