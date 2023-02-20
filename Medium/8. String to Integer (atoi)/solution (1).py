# 8. String to Integer (atoi)

# Runtime: 36 ms, faster than 71.21% of Python3 online submissions for String to Integer (atoi).

# Memory Usage: 14.2 MB, less than 82.38% of Python3 online submissions for String to Integer (atoi).


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        ans = 0
        for dig in s:
            if dig > '9' or dig < '0':
                break
            ans = ans * 10 + ord(dig) - ord('0')

        ans *= sign
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans