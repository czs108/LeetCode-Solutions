# 295. Find Median from Data Stream

# Runtime: 5707 ms, faster than 5.01% of Python3 online submissions for Find Median from Data Stream.

# Memory Usage: 35.4 MB, less than 89.18% of Python3 online submissions for Find Median from Data Stream.


class MedianFinder:
    # Simple Sorting
    def __init__(self) -> None:
        self._vals: list[int] = []

    def addNum(self, num: int) -> None:
        self._vals.append(num)

    def findMedian(self) -> float:
        self._vals.sort()
        n = len(self._vals)
        if n % 2 == 0:
            return (self._vals[n // 2] + self._vals[n // 2 - 1]) / 2
        else:
            return self._vals[n // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()