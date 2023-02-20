# 673. Number of Longest Increasing Subsequence

# Runtime: 1240 ms, faster than 84.16% of Python3 online submissions for Number of Longest Increasing Subsequence.

# Memory Usage: 14.4 MB, less than 83.39% of Python3 online submissions for Number of Longest Increasing Subsequence.


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        lens, counts = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    new_len = lens[j] + 1
                    if new_len > lens[i]:
                        lens[i] = new_len
                        counts[i] = counts[j]
                    elif new_len == lens[i]:
                        counts[i] += counts[j]

        max_len = max(lens)
        total_count = 0
        for i in range(len(lens)):
            if lens[i] == max_len:
                total_count += counts[i]
        return total_count