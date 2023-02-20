# 258. Add Digits

# Runtime: 54 ms, faster than 26.55% of Python3 online submissions for Add Digits.

# Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.


class Solution:
    def addDigits(self, num: int) -> int:
        if 0 <= num <= 9:
            return num
        else:
            dig_sum = 0
            while num > 0:
                dig_sum += num % 10
                num = num // 10
            return self.addDigits(dig_sum)