# 88. Merge Sorted Array

# Runtime: 32 ms, faster than 87.47% of Python3 online submissions for Merge Sorted Array.

# Memory Usage: 13.8 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify `nums1` in-place instead.
        """
        p1, p2 = m - 1, n - 1
        for i in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1