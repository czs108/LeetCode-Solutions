# 350. Intersection of Two Arrays II

# Runtime: 48 ms, faster than 67.57% of Python3 online submissions for Intersection of Two Arrays II.

# Memory Usage: 14.1 MB, less than 99.75% of Python3 online submissions for Intersection of Two Arrays II.


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        ins = 0
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                nums1[ins] = nums1[p1]
                ins += 1
                p1 += 1
                p2 += 1
        return nums1[:ins]