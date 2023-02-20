# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# def guess(num: int) -> int:
# Return -1 if my number is lower, 1 if my number is higher, otherwise return 0.

class Solution:
    # Binary Search
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                low = mid + 1
            else:
                high = mid - 1

        assert False, "No solution"