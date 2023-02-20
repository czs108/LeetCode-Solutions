# 254. Factor Combinations

# Runtime: 162 ms, faster than 24.27% of Python3 online submissions for Factor Combinations.

# Memory Usage: 15.3 MB, less than 17.68% of Python3 online submissions for Factor Combinations.


from math import sqrt

class Solution:
    # Depth-first Search
    def getFactors(self, n: int) -> list[list[int]]:
        ans = []

        def dfs(num: int, factor: int, path: list[int]) -> None:
            if len(path) > 0:
                ans.append(path + [num])

            for i in range(factor, int(sqrt(num)) + 1):
                if num % i == 0:
                    dfs(num // i, i, path + [i])


        dfs(n, 2, [])
        return ans