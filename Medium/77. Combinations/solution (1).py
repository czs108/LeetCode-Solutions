# 77. Combinations

# Runtime: 596 ms, faster than 26.61% of Python3 online submissions for Combinations.

# Memory Usage: 15.6 MB, less than 92.85% of Python3 online submissions for Combinations.


class Solution:
    # Backtracking
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        def backtrack(start: int, comb: list[int]) -> None:
            if len(comb) == k:
                ans.append(comb)
            else:
                for next in range(start, n + 1):
                    backtrack(next + 1, comb + [next])

        backtrack(1, [])
        return ans