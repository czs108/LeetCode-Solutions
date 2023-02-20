# 202. Happy Number

# Runtime: 28 ms, faster than 91.76% of Python3 online submissions for Happy Number.

# Memory Usage: 14 MB, less than 67.36% of Python3 online submissions for Happy Number.


class Solution:
    # Two Pointers
    def isHappy(self, n: int) -> bool:

        def calc_digit_sqr_sum(n: int) -> int:
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
            return sum

        slow, fast = n, n
        while True:
            slow = calc_digit_sqr_sum(slow)
            fast = calc_digit_sqr_sum(calc_digit_sqr_sum(fast))
            if fast == slow:
                break
        return slow == 1