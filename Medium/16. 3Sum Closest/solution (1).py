# 16. 3Sum Closest


import math

class Solution:
    # Two Pointers
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        for i in range(len(nums)):
            low, high = i + 1, len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                break
        return diff