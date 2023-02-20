# 119. Pascal's Triangle II

# Runtime: 24 ms, faster than 92.64% of Python3 online submissions for Pascal's Triangle II.

# Memory Usage: 14 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = []
        for i in range(rowIndex + 1):
            # The first and last row elements are always 1.
            row = [0 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle[-1]