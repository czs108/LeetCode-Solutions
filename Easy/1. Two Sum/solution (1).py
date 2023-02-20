# 1. Two Sum

# Runtime: 44 ms, faster than 91.84% of Python3 online submissions for Two Sum.

# Memory Usage: 15.5 MB, less than 5.11% of Python3 online submissions for Two Sum.


class Solution:
    # One-pass Hash Table
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in dict:
                return [dict[remain], i]
            else:
                dict[nums[i]] = i

        assert False, "No solution"