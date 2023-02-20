# 658. Find K Closest Elements

# Runtime: 300 ms, faster than 63.26% of Python3 online submissions for Find K Closest Elements.

# Memory Usage: 15.5 MB, less than 67.60% of Python3 online submissions for Find K Closest Elements.


from bisect import bisect_left

class Solution:
    # Binary Search | Sliding Window
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == k:
            return arr

        # Find the closest element and initialize two pointers.
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k.
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]