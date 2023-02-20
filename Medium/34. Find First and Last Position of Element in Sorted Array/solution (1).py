# 34. Find First and Last Position of Element in Sorted Array

# Runtime: 80 ms, faster than 91.46% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

# Memory Usage: 15.5 MB, less than 50.94% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.


class Solution:
    # Binary Search
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_bound(first: bool) -> int:
            begin, end = 0, len(nums) - 1
            while begin <= end:
                mid = begin + (end - begin) // 2
                if nums[mid] == target:
                    if first:
                        # This means we found our lower bound.
                        if mid == begin or nums[mid - 1] != target:
                            return mid
                        else:
                            # Search on the left side for the bound.
                            end = mid - 1
                    else:
                        # This means we found our upper bound.
                        if mid == end or nums[mid + 1] != target:
                            return mid
                        else:
                            # Search on the right side for the bound.
                            begin = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1
            return -1

        lower_bound = find_bound(True)
        if (lower_bound == -1):
            return [-1, -1]
        else:
            return [lower_bound, find_bound(False)]