# 268. Missing Number


class Solution:
    # HashSet
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)
        for v in range(len(nums) + 1):
            if v not in num_set:
                return v

        assert False