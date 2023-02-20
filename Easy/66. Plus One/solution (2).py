# 66. Plus One

# Runtime: 32 ms, faster than 78.18% of Python3 online submissions for Plus One.

# Memory Usage: 14.2 MB, less than 47.53% of Python3 online submissions for Plus One.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits