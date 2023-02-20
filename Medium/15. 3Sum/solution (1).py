# 15. 3Sum

# Runtime: 1000 ms, faster than 56.37% of Python3 online submissions for 3Sum.

# Memory Usage: 18 MB, less than 24.32% of Python3 online submissions for 3Sum.


class Solution:
    # Hash Set
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def two_sum(i: int) -> None:
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                        j += 1
                seen.add(nums[j])
                j += 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                two_sum(i)
        return res