# 724. Find Pivot Index


class Solution:
    # Prefix Sum
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum, total_sum = 0, sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            else:
                left_sum += nums[i]
        return -1