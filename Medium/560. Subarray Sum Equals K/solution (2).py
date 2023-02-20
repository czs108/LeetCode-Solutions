# 560. Subarray Sum Equals K

# Time Limit Exceeded


class Solution:
    # Cumulative Sum Without Space
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum += nums[end]
                if sum == k:
                    count += 1
        return count 