# 878. N-th Magical Number

# Runtime: 32 ms, faster than 72.73% of Python3 online submissions for N-th Magical Number.

# Memory Usage: 14.4 MB, less than 31.31% of Python3 online submissions for N-th Magical Number.


from math import gcd

class Solution:
    # Binary Search
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        least_cmn_mltpl = a // gcd(a, b) * b

        def magic_below_x(x: int) -> int:
            # How many magical numbers are <= x?
            return x // a + x // b - x // least_cmn_mltpl

        low, high = 0, n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            if magic_below_x(mid) < n:
                low = mid + 1
            else:
                high = mid

        return low % MOD