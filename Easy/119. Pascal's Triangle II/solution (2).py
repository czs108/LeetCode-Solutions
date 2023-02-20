# 119. Pascal's Triangle II

# Runtime: 28 ms, faster than 76.97% of Python3 online submissions for Pascal's Triangle II.

# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for _ in range(1, rowIndex + 1):
            for j in range(len(row) - 1, 0, -1):
                row[j] = row[j - 1] + row[j]
            row.append(1)
        return row