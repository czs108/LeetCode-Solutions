# 215. K-th Largest Element in an Array


import heapq

class Solution:
    # Heap
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]