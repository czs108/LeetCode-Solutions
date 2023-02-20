# 167. Two Sum II - Input array is sorted

# Runtime: 60 ms, faster than 87.16% of Python3 online submissions for Two Sum II - Input array is sorted.

# Memory Usage: 14.3 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.


class Solution:
    # One-pass Hash Table
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(numbers)):
            remain = target - numbers[i]
            if remain in dict:
                return [dict[remain] + 1, i + 1]
            else:
                dict[numbers[i]] = i

        assert False, "No solution"