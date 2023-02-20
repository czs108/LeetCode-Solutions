# 1306. Jump Game III

# Runtime: 360 ms, faster than 25.87% of Python3 online submissions for Jump Game III.

# Memory Usage: 61.8 MB, less than 45.79% of Python3 online submissions for Jump Game III.


class Solution:
    # Depth-First Search
    def canReach(self, arr: list[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            else:
                arr[start] = -arr[start]
                return self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])