# 202. Happy Number

# Runtime: 24 ms, faster than 97.93% of Python3 online submissions for Happy Number.

# Memory Usage: 14.2 MB, less than 6.83% of Python3 online submissions for Happy Number.


class Solution:
    # HashSet
    def isHappy(self, n: int) -> bool:

        def calc_digit_sqr_sum(n: int) -> int:
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
            return sum

        prev_sums = set()
        while n != 1:
            n = calc_digit_sqr_sum(n)
            if n in prev_sums:
                return False
            else:
                prev_sums.add(n)
        return True