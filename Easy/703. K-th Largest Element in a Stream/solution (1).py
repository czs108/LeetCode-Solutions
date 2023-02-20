# 703. K-th Largest Element in a Stream


import heapq

class KthLargest:
    # Heap
    def __init__(self, k: int, nums: list[int]) -> None:
        self._k: int = k
        self._heap: list[int] = nums
        heapq.heapify(self._heap)

        while len(self._heap) > self._k:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self._k:
            heapq.heappop(self._heap)
        return self._heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)