# 15. 3Sum

# Runtime: 692 ms, faster than 92.30% of Python3 online submissions for 3Sum.

# Memory Usage: 17.5 MB, less than 49.47% of Python3 online submissions for 3Sum.


class Solution:
    # Two Pointers
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def two_sum(i: int) -> None:
            low, high = i + 1, len(nums) - 1
            while (low < high):
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                two_sum(i)
        return res