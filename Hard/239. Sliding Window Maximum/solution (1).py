# 239. Sliding Window Maximum

# Runtime: 2148 ms, faster than 22.19% of Python3 online submissions for Sliding Window Maximum.

# Memory Usage: 29.9 MB, less than 74.50% of Python3 online submissions for Sliding Window Maximum.


class Solution:
    # Dynamic Programming
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if len(nums) * k == 0:
            return []
        elif k == 1:
            return nums

        left = [0 for _ in range(len(nums))]
        left[0] = nums[0]
        right = [0 for _ in range(len(nums))]
        right[-1] = nums[-1]

        for i in range(1, len(nums)):
            # From left to right.
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            # From right to left.
            j = len(nums) - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(right[i], left[i + k - 1]))
        return res