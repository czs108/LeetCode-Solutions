# 136. Single Number

# Runtime: 88 ms, faster than 64.02% of Python3 online submissions for Single Number.

# Memory Usage: 16.2 MB, less than 6.56% of Python3 online submissions for Single Number.


from collections import defaultdict

class Solution:
    # Hash Table
    def singleNumber(self, nums: list[int]) -> int:
        # Iterate through all elements in `nums` and set up key/value pair.
        hash_tab = defaultdict(int)
        for i in nums:
            hash_tab[i] += 1

        # Return the element which appeared only once.
        for i in hash_tab:
            if hash_tab[i] == 1:
                return i