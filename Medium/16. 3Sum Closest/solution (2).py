# 16. 3Sum Closest

# Runtime: 180 ms, faster than 40.36% of Python3 online submissions for 3Sum Closest.

# Memory Usage: 14.3 MB, less than 43.61% of Python3 online submissions for 3Sum Closest.


import math
from bisect import bisect_right

class Solution:
    # Binary Search
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                remain = target - nums[i] - nums[j]
                high = bisect_right(nums, remain, lo=j + 1)
                low = high - 1
                if low > j and abs(remain - nums[low]) < abs(diff):
                    diff = remain - nums[low]
                if high < len(nums) and abs(remain - nums[high]) < abs(diff):
                    diff = remain - nums[high]
            if diff == 0:
                break
        return target - diff