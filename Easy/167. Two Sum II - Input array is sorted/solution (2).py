# 167. Two Sum II - Input array is sorted

# Runtime: 56 ms, faster than 96.15% of Python3 online submissions for Two Sum II - Input array is sorted.

# Memory Usage: 14.3 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.


class Solution:
    # Two Pointers
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sum_val = numbers[start] + numbers[end]
            if sum_val == target:
                return [start + 1, end + 1]
            elif sum_val < target:
                start += 1
            else:
                end -= 1

        assert False, "No solution"