# 532. K-diff Pairs in an Array

# Runtime: 123 ms, faster than 39.47% of Python3 online submissions for K-diff Pairs in an Array.

# Memory Usage: 15.2 MB, less than 99.64% of Python3 online submissions for K-diff Pairs in an Array.


class Solution:
    # Two Pointers
    def findPairs(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)

        left, right = 0, 1
        count = 0
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                count += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
        return count