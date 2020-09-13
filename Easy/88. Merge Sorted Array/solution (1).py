# 88. Merge Sorted Array

# Runtime: 32 ms, faster than 87.47% of Python3 online submissions for Merge Sorted Array.

# Memory Usage: 13.8 MB, less than 6.15% of Python3 online submissions for Merge Sorted Array.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify `nums1` in-place instead.
        """
		# Compare two arrays one by one each time, put the larger one into the opening from the back to front.
        for i in range(m + n - 1, -1, -1):
            if n <= 0:
                nums1[i] = nums1[m - 1]
                m -= 1
            elif m <= 0:
                nums1[i] = nums2[n - 1]
                n -= 1
            elif nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1