# 169. Majority Element

# Runtime: 168 ms, faster than 86.74% of Python3 online submissions for Majority Element.

# Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.


class Solution:
    # Sorting
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]