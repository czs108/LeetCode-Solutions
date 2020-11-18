# 202. Happy Number

# Runtime: 28 ms, faster than 91.76% of Python3 online submissions for Happy Number.

# Memory Usage: 14 MB, less than 67.36% of Python3 online submissions for Happy Number.


class Solution:
    # Fast & Slow pointers
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = Solution.calcSum(slow)
            fast = Solution.calcSum(fast)
            fast = Solution.calcSum(fast)
            if fast == slow:
                break
        return slow == 1

    @staticmethod
    def calcSum(n: int) -> int:
        sum = 0
        while n != 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum