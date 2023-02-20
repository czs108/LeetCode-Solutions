# 40. Combination Sum II

# Runtime: 69 ms, faster than 68.13% of Python3 online submissions for Combination Sum II.

# Memory Usage: 14.5 MB, less than 5.36% of Python3 online submissions for Combination Sum II.


from collections import Counter

class Solution:
    # Backtracking with Counters
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        res = []

        def backtrack(remain: int, start: int, comb: list[int]) -> None:
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return

            for next in range(start, len(counter)):
                val, freq = counter[next]
                if freq <= 0:
                    continue

                comb.append(val)
                counter[next] = (val, freq - 1)
                backtrack(remain - val, next, comb)
                counter[next] = (val, freq)
                comb.pop()

        backtrack(target, 0, [])
        return res