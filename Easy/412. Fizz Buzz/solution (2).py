# 412. Fizz Buzz

# Runtime: 44 ms, faster than 70.54% of Python3 online submissions for Fizz Buzz.

# Memory Usage: 15 MB, less than 67.88% of Python3 online submissions for Fizz Buzz.


class Solution:
    # String Concatenation
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for n in range(1, n + 1):
            val = ""
            if n % 3 == 0:
                val += "Fizz"
            if n % 5 == 0:
                val += "Buzz"
            if not val:
                val = str(n)
            ans.append(val)
        return ans