# 80. Remove Duplicates from Sorted Array II

# Runtime: 83 ms, faster than 37.11% of Python3 online submissions for Remove Duplicates from Sorted Array II.

# Memory Usage: 13.9 MB, less than 96.82% of Python3 online submissions for Remove Duplicates from Sorted Array II.


class Solution:
    # Two Pointers
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        curr_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[k]:
                if curr_count < 2:
                    curr_count += 1
                    k += 1
                    nums[k] = nums[i]
            else:
                curr_count = 1
                k += 1
                nums[k] = nums[i]
        return k + 1