# 414. Third Maximum Number

# Runtime: 60 ms, faster than 15.32% of Python3 online submissions for Third Maximum Number.

# Memory Usage: 15.1 MB, less than 63.15% of Python3 online submissions for Third Maximum Number.


class Solution:
    # Keep Track of 3 Maximums Using a Set
    def thirdMax(self, nums: list[int]) -> int:
        max_nums = set()
        for num in nums:
            max_nums.add(num)
            if len(max_nums) > 3:
                max_nums.remove(min(max_nums))

        if len(max_nums) == 3:
            return min(max_nums)
        else:
            return max(max_nums)