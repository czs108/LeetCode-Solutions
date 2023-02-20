# 560. Subarray Sum Equals K

# Runtime: 432 ms, faster than 9.13% of Python3 online submissions for Subarray Sum Equals K.

# Memory Usage: 16.7 MB, less than 60.40% of Python3 online submissions for Subarray Sum Equals K.


from collections import Counter

class Solution:
    # Hashmap
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum, sum_map = 0, Counter()
        sum_map[0] = 1
        for num in nums:
            sum += num
            if sum - k in sum_map:
                count += sum_map[sum - k]
            sum_map[sum] += 1
        return count 