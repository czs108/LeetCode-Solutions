# 334. Increasing Triplet Subsequence

# Time Limit Exceeded


class Solution:
    # Dynamic Programming
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        match = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    match[i] = max(match[i], match[j] + 1)
                    if match[i] >= 3:
                        return True
        return False