# 902. Numbers At Most N Given Digit Set

# Runtime: 36 ms, faster than 30.56% of Python3 online submissions for Numbers At Most N Given Digit Set.

# Memory Usage: 14.4 MB, less than 50.93% of Python3 online submissions for Numbers At Most N Given Digit Set.


class Solution:
    # Dynamic Programming | Counting
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        s = str(n)
        # `count[i]` is total number of valid integers if N was N[i:].
        count = [0] * len(s) + [1]
        for i in range(len(s) - 1, -1, -1):
            for dig in digits:
                if dig < s[i]:
                    count[i] += len(digits) ** (len(s) - i - 1)
                elif dig == s[i]:
                    count[i] += count[i + 1]
        return count[0] + sum(len(digits) ** i for i in range(1, len(s)))