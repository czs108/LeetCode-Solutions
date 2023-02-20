# 169. Majority Element


class Solution:
    # Brute Force
    def majorityElement(self, nums: list[int]) -> int:
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

        assert False, "No solution"