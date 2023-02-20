# 189. Rotate Array

class Solution:
    # Using Cyclic Replacements
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        start = count = 0
        while count < len(nums):
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % len(nums)
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1