# 496. Next Greater Element I

# Runtime: 48 ms, faster than 71.69% of Python3 online submissions for Next Greater Element I.

# Memory Usage: 14.7 MB, less than 14.37% of Python3 online submissions for Next Greater Element I.


class Solution:
    # Brute Force
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        idx = {nums2[i]: i for i in range(len(nums2))}
        res = []
        for n in nums1:
            found = False
            for i in range(idx[n] + 1, len(nums2)):
                if nums2[i] > n:
                    res.append(nums2[i])
                    found = True
                    break
            if not found:
                res.append(-1)
        return res