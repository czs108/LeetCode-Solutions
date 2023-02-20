# 367. Valid Perfect Square


class Solution:
    # Binary Search
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            sqr = mid ** 2
            if sqr == num:
                return True
            elif sqr < num:
                left = mid + 1
            else:
                right = mid - 1
        return False