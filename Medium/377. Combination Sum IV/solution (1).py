# 377. Combination Sum IV

# Runtime: 40 ms, faster than 74.08% of Python3 online submissions for Combination Sum IV.

# Memory Usage: 14.3 MB, less than 45.92% of Python3 online submissions for Combination Sum IV.


class Solution:
    # Dynamic Programming
    def combinationSum4(self, nums: list[int], target: int) -> int:
        count = [0] * (target + 1)
        count[0] = 1
        for i in range(target + 1):
            for n in nums:
                if n <= i:
                    count[i] += count[i - n]
        return count[-1]