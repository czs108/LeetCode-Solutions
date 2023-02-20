# 354. Russian Doll Envelopes

# Runtime: 7020 ms, faster than 13.36% of Python3 online submissions for Russian Doll Envelopes.

# Memory Usage: 16.5 MB, less than 21.36% of Python3 online submissions for Russian Doll Envelopes.


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:

        def lis_len(nums: list[int]) -> int:
            if len(nums) == 0:
                return 0

            counts = [1 for _ in nums]
            max_len = 1
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        counts[i] = max(counts[i], counts[j] + 1)
                max_len = max(max_len, counts[i])
            return max_len

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return lis_len([env[1] for env in envelopes])