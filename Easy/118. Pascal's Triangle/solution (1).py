# 118. Pascal's Triangle

# Runtime: 24 ms, faster than 91.61% of Python3 online submissions for Pascal's Triangle.

# Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for Pascal's Triangle.


class Solution:
    # Dynamic Programming
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            # The first and last row elements are always 1.
            row = [0 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle