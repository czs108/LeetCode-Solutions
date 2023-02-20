# 4. Median of Two Sorted Arrays


class Solution:
    # Binary Search
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        def k_th(nums1: list[int], low1: int, high1: int, nums2: list[int], low2: int, high2: int, k: int) -> int:
            len1, len2 = high1 - low1 + 1, high2 - low2 + 1
            if len1 > len2:
                return k_th(nums2, low2, high2, nums1, low1, high1, k)
            elif len1 == 0:
                return nums2[low2 + k - 1]
            elif k == 1:
                return min(nums1[low1], nums2[low2])
            else:
                i, j = low1 + min(len1, k // 2) - 1, low2 + min(len2, k // 2) - 1
                if nums1[i] > nums2[j]:
                    return k_th(nums1, low1, high1, nums2, j + 1, high2, k - (j - low2 + 1))
                else:
                    return k_th(nums1, i + 1, high1, nums2, low2, high2, k - (i - low1 + 1))

        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            mid = total // 2
            return (k_th(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, mid) + k_th(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, mid + 1)) / 2
        else:
            mid = total // 2 + 1
            return k_th(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, mid)