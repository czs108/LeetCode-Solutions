# 18. 4Sum

# Runtime: 92 ms, faster than 92.71% of Python3 online submissions for 4Sum.

# Memory Usage: 14.3 MB, less than 58.20% of Python3 online submissions for 4Sum.


class Solution:
    # Hash Set
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
            seen = set()
            for i in range(len(nums)):
                if not res or nums[i] != res[-1][1]:
                    remain = target - nums[i]
                    if remain in seen:
                        res.append([remain, nums[i]])
                    seen.add(nums[i])
            return res

        nums.sort()
        return k_sum(nums, target, 4)