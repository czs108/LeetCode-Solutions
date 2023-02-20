# 560. Subarray Sum Equals K

# Time Limit Exceeded


class Solution:
    # Cumulative Sum
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum = [0] * (len(nums) + 1)
        for i in range(len(nums) + 1):
            sum[i] = sum[i - 1] + nums[i - 1]

        count = 0
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if sum[end] - sum[start] == k:
                    count += 1
        return count 