# 496. Next Greater Element I

# Runtime: 44 ms, faster than 88.07% of Python3 online submissions for Next Greater Element I.

# Memory Usage: 14.5 MB, less than 43.69% of Python3 online submissions for Next Greater Element I.


class Solution:
    # Stack
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        idx = {}
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                idx[stack.pop()] = n
            stack.append(n)

        while stack:
            idx[stack.pop()] = -1

        return [idx[i] for i in nums1]