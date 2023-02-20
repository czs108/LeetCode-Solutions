# 368. Largest Divisible Subset

# Runtime: 380 ms, faster than 78.59% of Python3 online submissions for Largest Divisible Subset.

# Memory Usage: 14.6 MB, less than 45.25% of Python3 online submissions for Largest Divisible Subset.


class Solution:
    # Dynamic Programming
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return []

        nums.sort()
        counts = [1] * len(nums)
        for i, num in enumerate(nums):
            count = 0
            for j in range(i):
                if num % nums[j] == 0:
                    count = max(count, counts[j])
            counts[i] += count

        # Reconstruct the largest divisible subset.
        max_count, max_idx = max([(n, i) for i, n in enumerate(counts)])
        curr_count, curr_tail = max_count, nums[max_idx]
        ans = []
        for i in range(max_idx, -1, -1):
            if curr_count == counts[i] and curr_tail % nums[i] == 0:
                ans.append(nums[i])
                curr_count -= 1
                curr_tail = nums[i]
        return ans