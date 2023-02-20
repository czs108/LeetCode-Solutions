# 69. Sqrt(x)

# Runtime: 64 ms, faster than 17.43% of Python3 online submissions for Sqrt(x).

# Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Sqrt(x).


class Solution:
    # Binary Search
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low, high = 1, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid**2 == x:
                return mid
            elif x < mid**2:
                high = mid - 1
            else:
                low = mid + 1
        return high