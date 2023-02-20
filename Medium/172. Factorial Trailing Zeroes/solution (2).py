# 172. Factorial Trailing Zeroes


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Each 0 on the end of the factorial represents a multiplication by 10.
        count = 0
        for i in range(5, n + 1, 5):
            curr = i
            while curr % 5 == 0:
                count += 1
                curr //= 5
        return count