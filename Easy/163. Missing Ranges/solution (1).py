# 163. Missing Ranges


class Solution:
    # Linear Scan
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:

        def format_range(lower: int, upper: int) -> str:
            return f"{lower}" if lower == upper else f"{lower}->{upper}"

        ans = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if curr - prev > 1:
                ans.append(format_range(prev + 1, curr - 1))
            prev = curr
        return ans