# 66. Plus One

# Runtime: 24 ms, faster than 95.29% of Python3 online submissions for Plus One.

# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Plus One.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Convert the array into a integer
        num = 0
        for i in digits:
            num = num * 10 + i
        num += 1

        # Convert the integer back into an array
        result = []
        while num != 0:
            result.insert(0, num % 10)
            num = num // 10
        return result