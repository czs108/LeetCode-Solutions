# 169. Majority Element

# Runtime: 168 ms, faster than 86.74% of Python3 online submissions for Majority Element.

# Memory Usage: 15.1 MB, less than 7.14% of Python3 online submissions for Majority Element.


from collections import Counter

class Solution:
    # HashMap
    def majorityElement(self, nums: list[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key = counts.get)