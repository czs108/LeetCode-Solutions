# 494. Target Sum


class Solution:
    # Dynamic Programming
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self._nums = nums
        self._memo = [{} for _ in range(len(nums))]
        return self._calc_count(0, target)

    def _calc_count(self, idx: int, remain: int) -> int:
        if idx == len(self._nums):
            return 1 if remain == 0 else 0
        elif remain in self._memo[idx]:
            return self._memo[idx][remain]
        else:
            add = self._calc_count(idx + 1, remain - self._nums[idx])
            sub = self._calc_count(idx + 1, remain + self._nums[idx])
            self._memo[idx][remain] = add + sub
            return self._memo[idx][remain]