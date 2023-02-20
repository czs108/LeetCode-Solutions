# 295. Find Median from Data Stream

# Runtime: 2710 ms, faster than 5.93% of Python3 online submissions for Find Median from Data Stream.

# Memory Usage: 35.4 MB, less than 94.61% of Python3 online submissions for Find Median from Data Stream.


import bisect

class MedianFinder:
    # Insertion Sort
    def __init__(self) -> None:
        self._vals: list[int] = []

    def addNum(self, num: int) -> None:
        bisect.insort(self._vals, num)

    def findMedian(self) -> float:
        n = len(self._vals)
        if n % 2 == 0:
            return (self._vals[n // 2] + self._vals[n // 2 - 1]) / 2
        else:
            return self._vals[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()