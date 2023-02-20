# 343. Integer Break

# Runtime: 36 ms, faster than 55.89% of Python3 online submissions for Integer Break.

# Memory Usage: 14.3 MB, less than 47.74% of Python3 online submissions for Integer Break.


class Solution:
    # Dynamic Programming
    def integerBreak(self, n: int) -> int:
        prdct = [0] * (n + 1)
        prdct[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                prdct[i] = max(prdct[i], prdct[i - j] * j, j * (i - j))
        return prdct[-1]