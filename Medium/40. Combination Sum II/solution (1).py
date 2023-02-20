# 40. Combination Sum II

# Runtime: 72 ms, faster than 66.85% of Python3 online submissions for Combination Sum II.

# Memory Usage: 14.4 MB, less than 50.42% of Python3 online submissions for Combination Sum II.


class Solution:
    # Backtracking with Index
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(remain: int, start: int, comb: list[int]) -> None:
            if remain == 0:
                res.append(list(comb))
                return

            for next in range(start, len(candidates)):
                if next > start and candidates[next] == candidates[next - 1]:
                    continue
                val = candidates[next]
                if remain - val < 0:
                    break
                else:
                    comb.append(val)
                    backtrack(remain - val, next + 1, comb)
                    comb.pop()

        backtrack(target, 0, [])
        return res