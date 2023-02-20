# 39. Combination Sum

# Runtime: 76 ms, faster than 77.09% of Python3 online submissions for Combination Sum.

# Memory Usage: 14.3 MB, less than 76.75% of Python3 online submissions for Combination Sum.


class Solution:
    # Backtracking
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(remain: int, start: int, comb: list[int]) -> None:
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # Add the number into the combination.
                comb.append(candidates[i])
                # Give the current number another chance, rather than moving on.
                backtrack(remain - candidates[i], i, comb)
                # Backtrack, remove the number from the combination.
                comb.pop()

        backtrack(target, 0, [])
        return res