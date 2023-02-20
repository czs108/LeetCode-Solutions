# 1295. Find Numbers with Even Number of Digits

# untime: 56 ms, faster than 27.29% of Python3 online submissions for Find Numbers with Even Number of Digits.

# Memory Usage: 14.5 MB, less than 6.23% of Python3 online submissions for Find Numbers with Even Number of Digits.


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            n = 0
            while i != 0:
                i //= 10
                n += 1
            if n % 2 == 0:
                count += 1
        return count