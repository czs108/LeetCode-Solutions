# 169. Majority Element


import random

class Solution:
    # Randomization
    def majorityElement(self, nums: list[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
        assert False, "No solution"