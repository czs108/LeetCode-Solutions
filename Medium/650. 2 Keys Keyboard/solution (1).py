# 650. 2 Keys Keyboard

# Runtime: 52 ms, faster than 61.81% of Python3 online submissions for 2 Keys Keyboard.

# Memory Usage: 14.2 MB, less than 59.32% of Python3 online submissions for 2 Keys Keyboard.


class Solution:
    # Prime Factorization
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans