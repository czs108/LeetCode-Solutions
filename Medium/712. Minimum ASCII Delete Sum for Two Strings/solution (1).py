# 712. Minimum ASCII Delete Sum for Two Strings

# Runtime: 661 ms, faster than 85.11% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.

# Memory Usage: 18.5 MB, less than 68.51% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.


class Solution:
    # Dynamic Programming
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        sum = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            sum[i][0] = sum[i - 1][0] + ord(s1[i - 1])
        for i in range(1, len(s2) + 1):
            sum[0][i] = sum[0][i - 1] + ord(s2[i - 1])

        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    # No need to delete.
                    sum[i + 1][j + 1] = sum[i][j]
                else:
                    sum[i + 1][j + 1] = min(sum[i + 1][j] + ord(s2[j]), sum[i][j + 1] + ord(s1[i]))
        return sum[-1][-1]