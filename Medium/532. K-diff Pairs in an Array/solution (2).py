# 532. K-diff Pairs in an Array

# Runtime: 80 ms, faster than 76.16% of Python3 online submissions for K-diff Pairs in an Array.

# Memory Usage: 15.6 MB, less than 84.25% of Python3 online submissions for K-diff Pairs in an Array.


from collections import Counter

class Solution:
    # Hashmap
    def findPairs(self, nums: list[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        for n in counter:
            if (k > 0 and n + k in counter) or (k == 0 and counter[n] > 1):
                count += 1
        return count