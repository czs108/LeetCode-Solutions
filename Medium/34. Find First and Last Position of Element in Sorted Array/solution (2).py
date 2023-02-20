# 34. Find First and Last Position of Element in Sorted Array

# Runtime: 93 ms, faster than 27.31% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

# Memory Usage: 15.6 MB, less than 12.09% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.


class Solution:
    # Binary Search
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_left_bound() -> int:
            begin, end = 0, len(nums)
            while begin < end:
                mid = begin + (end - begin) // 2
                if nums[mid] == target:
                    end = mid
                elif nums[mid] > target:
                    end = mid
                else:
                    begin = mid + 1

            if begin >= len(nums) or nums[begin] != target:
                return -1
            else:
                return begin

        def find_right_bound() -> int:
            begin, end = 0, len(nums)
            while begin < end:
                mid = begin + (end - begin) // 2
                if nums[mid] == target:
                    begin = mid + 1
                elif nums[mid] > target:
                    end = mid
                else:
                    begin = mid + 1

            if begin == 0 or nums[begin - 1] != target:
                return -1
            else:
                return begin - 1


        lower_bound = find_left_bound()
        if (lower_bound == -1):
            return [-1, -1]
        else:
            return [lower_bound, find_right_bound()]