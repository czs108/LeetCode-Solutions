# 1035. Uncrossed Lines

# Runtime: 247 ms, faster than 49.44% of Python3 online submissions for Uncrossed Lines.

# Memory Usage: 14.7 MB, less than 44.07% of Python3 online submissions for Uncrossed Lines.


class Solution:
    # Dynamic Programming
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        lines = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    lines[i + 1][j + 1] = lines[i][j] + 1
                else:
                    lines[i + 1][j + 1] = max(lines[i][j + 1], lines[i + 1][j])
        return lines[-1][-1]