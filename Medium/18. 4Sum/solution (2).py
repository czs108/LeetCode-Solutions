# 18. 4Sum

# Runtime: 81 ms, faster than 98.02% of Python3 online submissions for 4Sum.

# Memory Usage: 14.6 MB, less than 8.35% of Python3 online submissions for 4Sum.


class Solution:
    # Two Pointers
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        def k_sum(nums: list[int], target: int, k: int) -> list[list[int]]:
            if not nums:
                return []

            avg = target // k
            if avg < nums[0] or nums[-1] < avg:
                return []

            if k == 2:
                return two_sum(nums, target)

            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for subset in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def two_sum(nums: list[int], target: int) -> list[list[int]]:
            res = []
            left, right = 0, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            return res

        nums.sort()
        return k_sum(nums, target, 4)