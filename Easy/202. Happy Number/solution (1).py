# 202. Happy Number

# Runtime: 24 ms, faster than 97.93% of Python3 online submissions for Happy Number.

# Memory Usage: 14.2 MB, less than 6.83% of Python3 online submissions for Happy Number.


class Solution:
    # HashSet
    def isHappy(self, n: int) -> bool:
        prevs = set()
        while n != 1:
            n = Solution.calcSum(n)
            if n in prevs:
                return False
            prevs.add(n)
        return True
    
    @staticmethod
    def calcSum(n: int) -> int:
        sum = 0
        while n != 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum