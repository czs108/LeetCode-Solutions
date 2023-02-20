# 350. Intersection of Two Arrays II

# Runtime: 48 ms, faster than 67.57% of Python3 online submissions for Intersection of Two Arrays II.

# Memory Usage: 14.2 MB, less than 89.92% of Python3 online submissions for Intersection of Two Arrays II.


class Solution:
    # Map
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        map1 = {}
        for i in nums1:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1

        ins = 0
        for i in nums2:
            if i in map1:
                nums1[ins] = i
                ins += 1
                map1[i] -= 1
                if map1[i] == 0:
                    del map1[i]
                    if len(map1) == 0:
                        break
        return nums1[:ins]