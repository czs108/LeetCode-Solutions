# 47. Permutations II

# Runtime: 89 ms, faster than 41.81% of Python3 online submissions for Permutations II.

# Memory Usage: 14.6 MB, less than 60.60% of Python3 online submissions for Permutations II.


from collections import Counter

class Solution:
    # Backtracking with Groups of Numbers
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        counter = Counter(nums)

        def backtrack(prmt: list[int]) -> None:
            if len(prmt) == len(nums):
                ans.append(list(prmt))
                return

            for n in counter:
                if counter[n] > 0:
                    prmt.append(n)
                    counter[n] -= 1
                    backtrack(prmt)
                    prmt.pop()
                    counter[n] += 1

        backtrack([])
        return ans