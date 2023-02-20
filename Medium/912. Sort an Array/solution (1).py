# 912. Sort an Array

# Runtime: 880 ms, faster than 33.75% of Python3 online submissions for Sort an Array.

# Memory Usage: 22.1 MB, less than 38.20% of Python3 online submissions for Sort an Array.


class Solution:
    # Merge Sort
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        def merge(left: list[int], right: list[int]) -> list[int]:
            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return merge(left, right)