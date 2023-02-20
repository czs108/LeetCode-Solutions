# 702. Search in a Sorted Array of Unknown Size


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
class Solution:
    # Binary Search
    def search(self, reader: ArrayReader, target: int) -> int:
        if reader.get(0) == target:
            return 0

        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2

        while left <= right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1