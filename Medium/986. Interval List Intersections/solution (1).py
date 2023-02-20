# 986. Interval List Intersections

# Runtime: 148 ms, faster than 73.86% of Python3 online submissions for Interval List Intersections.

# Memory Usage: 14.9 MB, less than 92.34% of Python3 online submissions for Interval List Intersections.


class Solution:
    # Two Pointers
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

        def intersection(first: list[int], second: list[int]) -> list[int]:
            if first[0] > second[0]:
                first, second = second, first
            if first[1] >= second[0]:
                merge = [first[0], first[1], second[0], second[1]]
                merge.sort()
                return [merge[1], merge[2]]
            else:
                return []

        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            itr = intersection(firstList[i], secondList[j])
            if itr:
                ans.append(itr)
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans