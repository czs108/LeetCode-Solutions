# 744. Find Smallest Letter Greater Than Target

# Runtime: 204 ms, faster than 5.78% of Python3 online submissions for Find Smallest Letter Greater Than Target.

# Memory Usage: 14.7 MB, less than 31.28% of Python3 online submissions for Find Smallest Letter Greater Than Target.


class Solution:
    # Binary Search
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (letters[mid]) <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]