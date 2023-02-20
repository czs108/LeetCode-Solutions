# 412. Fizz Buzz

# Runtime: 44 ms, faster than 70.54% of Python3 online submissions for Fizz Buzz.

# Memory Usage: 15.1 MB, less than 67.88% of Python3 online submissions for Fizz Buzz.


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for n in range(1, n + 1):
            divisible_by_3 = (n % 3 == 0)
            divisible_by_5 = (n % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(n))
        return ans