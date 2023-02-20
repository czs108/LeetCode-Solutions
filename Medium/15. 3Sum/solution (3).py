# 15. 3Sum

# Runtime: 876 ms, faster than 71.20% of Python3 online submissions for 3Sum.

# Memory Usage: 17.4 MB, less than 86.53% of Python3 online submissions for 3Sum.


class Solution:
    # No-Sort Hash Set
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                seen = set()
                for val2 in nums[i + 1:]:
                    complement = -val1 - val2
                    if complement in seen:
                        res.add(tuple(sorted((val1, val2, complement))))
                    else:
                        seen.add(val2)
        return list(res)