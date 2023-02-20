# 75. Sort Colors

# Runtime: 20 ms, faster than 99.69% of Python3 online submissions for Sort Colors.

# Memory Usage: 14.3 MB, less than 45.17% of Python3 online submissions for Sort Colors.


class Solution:
    # Two Pointers
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                # if curr != p0:
                #     nums[p0], nums[curr] = 0, 1
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1