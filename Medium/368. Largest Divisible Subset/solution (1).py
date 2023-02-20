# 368. Largest Divisible Subset

# Runtime: 316 ms, faster than 90.62% of Python3 online submissions for Largest Divisible Subset.

# Memory Usage: 14.9 MB, less than 12.03% of Python3 online submissions for Largest Divisible Subset.


class Solution:
    # Dynamic Programming with Set
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        subsets = {-1: set()}
        nums.sort()
        for num in sorted(nums):
            possible = [subsets[k] for k in subsets if num % k == 0]
            subsets[num] = max(possible, key=len) | {num}
        return list(max(subsets.values(), key=len))