# 50. Pow(x, n)


class Solution:
    # Fast Power Algorithm Recursive
    def myPow(self, x: float, n: int) -> float:

        def fast_pow(x: float, n: int) -> float:
            if n == 0:
                return 1
            else:
                half = fast_pow(x, n // 2)
                if n % 2 == 0:
                    return half**2
                else:
                    return half**2 * x

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)