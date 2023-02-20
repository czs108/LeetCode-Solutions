# 347. Top K Frequent Elements

# Runtime: 107 ms, faster than 48.77% of Python3 online submissions for Top K Frequent Elements.

# Memory Usage: 18.6 MB, less than 83.55% of Python3 online submissions for Top K Frequent Elements.


from collections import Counter
import heapq

class Solution:
    # Heap
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        else:
            count = Counter(nums)
            return heapq.nlargest(k, count.keys(), key=count.get) 