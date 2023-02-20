# 740. Delete and Earn

# Runtime: 78 ms, faster than 29.21% of Python3 online submissions for Delete and Earn.

# Memory Usage: 14.5 MB, less than 59.86% of Python3 online submissions for Delete and Earn.


from collections import Counter


class Solution:
    # Dynamic Programming
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        keys = sorted(counts)

        points = [0 for _ in range(len(keys) + 1)]
        points[1] = counts[keys[0]] * keys[0]
        for i in range(2, len(keys) + 1):
            j = i - 1
            if keys[j] == keys[j - 1] + 1:
                points[i] = max(points[i - 1], points[i - 2] + counts[keys[j]] * keys[j])
            else:
                points[i] = points[i - 1] + counts[keys[j]] * keys[j]
        return points[-1]